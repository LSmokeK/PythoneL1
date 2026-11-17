from flask import Flask, render_template

from app.config import configurations
from app.extensions import db, migrate, csrf


def create_app(config_name="development"):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(
        configurations.get(config_name, configurations["development"])
    )

    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    from app import views
    from app.users.views import users_bp
    from app.products.views import products_bp
    from app.posts import post_bp
    from app.posts import models
    from app.posts import views as posts_views

    app.register_blueprint(views.app_bp)
    app.register_blueprint(users_bp, url_prefix="/users")
    app.register_blueprint(products_bp)
    app.register_blueprint(post_bp)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html"), 404

    # Створюємо таблиці та початковий навчальний пост для нового розгортання.
    with app.app_context():
        from app.posts.models import Post
        db.create_all()
        if not db.session.scalar(db.select(Post.id).limit(1)):
            db.session.add(Post(
                title="Grand Theft Auto VI — гра, на яку я чекаю",
                content=(
                    "Grand Theft Auto VI — одна з ігор, яка найбільше привертає мою увагу. "
                    "Мені подобаються проєкти з великим відкритим світом, де можна проходити "
                    "сюжет, досліджувати місто та знаходити цікаві місця.\\n\\n"
                    "Особливо цікава атмосфера Vice City: яскраві вулиці, узбережжя, "
                    "автомобілі та контраст між красивими краєвидами й кримінальним сюжетом. "
                    "На мою думку, увага до деталей робить ігровий світ переконливим.\\n\\n"
                    "Найбільше від GTA VI я очікую живого міста, цікавих персонажів, "
                    "різноманітних завдань і хорошого сюжету. "
                    "Це мої особисті очікування, а не огляд готової гри."
                ),
                category="publication",
                is_active=True,
                author="Євгеній Вербицький"
            ))
            db.session.commit()

    return app