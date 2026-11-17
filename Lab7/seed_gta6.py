"""Run after flask db upgrade: python seed_gta6.py"""
from app import create_app
from app.extensions import db
from app.posts.models import Post
app=create_app()
with app.app_context():
    if not db.session.scalar(db.select(Post.id).limit(1)):
        db.session.add(Post(title="Grand Theft Auto VI — гра, на яку я чекаю", content=(
            "Grand Theft Auto VI — одна з ігор, яка найбільше привертає мою увагу. "
            "Мені подобаються великі відкриті світи та атмосфера Vice City. "
            "Я очікую цікавих персонажів, захопливого сюжету та живого міста. "
            "Це мої особисті очікування від гри."), category="publication", is_active=True, author="Євгеній Вербицький"))
        db.session.commit()
