from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp, ValidationError
from app.posts.models import User
from app.extensions import db

class RegistrationForm(FlaskForm):
    username = StringField('Ім’я користувача', validators=[DataRequired(), Length(min=4,max=80), Regexp(r'^[A-Za-z][A-Za-z0-9_.]*$', message='Використовуйте латинські літери, цифри, крапку або підкреслення.')])
    email = StringField('Електронна пошта', validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=6,max=72)])
    confirm_password = PasswordField('Підтвердження пароля', validators=[DataRequired(), EqualTo('password', message='Паролі не збігаються.')])
    submit = SubmitField('Зареєструватися')
    def validate_username(self, field):
        if db.session.scalar(db.select(User).filter_by(username=field.data.strip())):
            raise ValidationError('Таке ім’я вже існує.')
    def validate_email(self, field):
        if db.session.scalar(db.select(User).filter_by(email=field.data.strip().lower())):
            raise ValidationError('Така пошта вже зареєстрована.')
    def validate_password(self, field):
        if len(field.data.encode('utf-8')) > 72:
            raise ValidationError('Пароль перевищує 72 байти.')

class LoginForm(FlaskForm):
    email = StringField('Електронна пошта', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember = BooleanField('Запам’ятати мене')
    submit = SubmitField('Увійти')
