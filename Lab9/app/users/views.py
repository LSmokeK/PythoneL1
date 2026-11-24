
from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash,
    make_response,
)

users_bp = Blueprint(
    "users",
    __name__,
    template_folder="templates"
)

from flask_login import current_user, login_user, logout_user, login_required
from app.extensions import db
from app.posts.models import User
from app.users.forms import RegistrationForm, LoginForm
from sqlalchemy.exc import IntegrityError


@users_bp.route("/hi/<name>")
def greetings(name):
    age = request.args.get("age", "не вказано")
    return render_template(
        "users/hi.html",
        title="Привітання",
        name=name,
        age=age
    )


@users_bp.route("/admin")
def admin():
    return redirect(
        url_for("users.greetings", name="Administrator", age=45)
    )


@users_bp.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('users.account'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data.strip(), email=form.email.data.strip().lower())
        user.set_password(form.password.data)
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            flash('Ім’я або пошта вже зайняті.', 'danger')
        else:
            flash('Реєстрація успішна! Тепер увійдіть.', 'success')
            return redirect(url_for('users.login'))
    return render_template('users/auth.html', form=form, title='Реєстрація')

@users_bp.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('users.account'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(db.select(User).filter_by(email=form.email.data.strip().lower()))
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            session['username'] = user.username
            flash('Вхід успішний!', 'success')
            return redirect(url_for('users.account'))
        flash('Неправильна пошта або пароль.', 'danger')
    return render_template('users/auth.html', form=form, title='Вхід')

@users_bp.route('/profile')
@users_bp.route('/account')
@login_required
def account():
    return render_template('users/account.html')

@users_bp.route('/')
@login_required
def all_users():
    users = db.session.scalars(db.select(User).order_by(User.id)).all()
    return render_template('users/list.html', users=users)

@users_bp.route('/profile/theme', methods=['POST'])
@login_required
def change_theme():
    response = make_response(redirect(url_for('users.account')))
    response.set_cookie('profile_theme', 'dark' if request.form.get('theme') == 'dark' else 'light', max_age=2592000, httponly=True, samesite='Lax')
    return response

@users_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    session.pop('username', None)
    flash('Ви вийшли із системи.', 'info')
    return redirect(url_for('users.login'))
