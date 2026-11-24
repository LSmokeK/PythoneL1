import unittest
from app import create_app
from app.extensions import db
from app.posts.models import User

class AuthTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.ctx = self.app.app_context(); self.ctx.push()
        db.create_all()
        self.client = self.app.test_client()
        self.data = dict(username='TestPlayer', email='player@example.com', password='DemoPass123', confirm_password='DemoPass123')
    def tearDown(self):
        db.session.remove(); db.drop_all(); self.ctx.pop()
    def register(self):
        return self.client.post('/users/register', data=self.data, follow_redirects=True)
    def test_views(self):
        for path in ['/users/register','/users/login']:
            self.assertEqual(self.client.get(path).status_code,200)
    def test_registration(self):
        self.assertIn('Реєстрація успішна'.encode(),self.register().data)
        user = db.session.scalar(db.select(User).filter_by(email=self.data['email']))
        self.assertTrue(user.check_password(self.data['password']))
        self.assertNotEqual(user.password,self.data['password'])
    def test_duplicate(self):
        self.register(); self.assertIn('Така пошта вже зареєстрована'.encode(),self.register().data)
        self.assertEqual(db.session.scalar(db.select(db.func.count(User.id))),1)
    def test_login_logout(self):
        self.register()
        self.assertEqual(self.client.get('/users/account').status_code,302)
        self.assertEqual(self.client.get('/users/').status_code,302)
        self.client.post('/users/login',data={'email':self.data['email'],'password':'wrong'})
        self.assertEqual(self.client.get('/users/account').status_code,302)
        self.client.post('/users/login',data=self.data)
        self.assertEqual(self.client.get('/users/account').status_code,200)
        self.assertEqual(self.client.get('/users/').status_code,200)
        self.assertEqual(self.client.get('/users/register').status_code,302)
        self.client.post('/users/logout')
        self.assertEqual(self.client.get('/users/account').status_code,302)
