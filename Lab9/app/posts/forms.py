from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    TextAreaField,
    BooleanField,
    SelectField,
    SelectMultipleField,
    SubmitField
)
from wtforms.fields import DateTimeLocalField
from wtforms.validators import DataRequired, Length, Optional


class PostForm(FlaskForm):
    title = StringField(
        "Заголовок",
        validators=[
            DataRequired(message="Введіть заголовок"),
            Length(max=150)
        ]
    )

    content = TextAreaField(
        "Текст поста",
        validators=[
            DataRequired(message="Введіть текст поста")
        ]
    )

    enabled = BooleanField(
        "Активний пост",
        default=True
    )

    publish_date = DateTimeLocalField(
        "Дата публікації",
        format="%Y-%m-%dT%H:%M",
        validators=[Optional()]
    )

    category = SelectField(
        "Категорія",
        choices=[
            ("news", "Новини"),
            ("publication", "Публікації"),
            ("tech", "Технології"),
            ("other", "Інше")
        ],
        validators=[DataRequired()]
    )

    author_id = SelectField("Автор", coerce=int, validators=[DataRequired()])
    tags = SelectMultipleField("Теги", coerce=int)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from app.extensions import db
        from app.posts.models import User, Tag
        self.author_id.choices = [(u.id, u.username) for u in db.session.scalars(db.select(User).order_by(User.id))]
        self.tags.choices = [(t.id, t.name) for t in db.session.scalars(db.select(Tag).order_by(Tag.id))]

    submit = SubmitField("Зберегти")