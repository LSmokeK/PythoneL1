from datetime import datetime, timezone
from sqlalchemy import String, Text, Boolean, DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from app.extensions import db, bcrypt, login_manager
from flask_login import UserMixin


class Post(db.Model):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    posted: Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(timezone.utc).replace(tzinfo=None)
    )

    category: Mapped[str] = mapped_column(
        Enum("news", "publication", "tech", "other", name="post_category"),
        nullable=False,
        default="other"
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    author: Mapped["User"] = relationship(back_populates="posts")
    tags: Mapped[list["Tag"]] = relationship(secondary="post_tags", back_populates="posts")
    image: Mapped[str] = mapped_column(String(120), default="default.jpg")

    def __repr__(self):
        return f"<Post {self.id}: {self.title}>"

post_tags = db.Table("post_tags", db.Column("post_id", ForeignKey("posts.id"), primary_key=True), db.Column("tag_id", ForeignKey("tags.id"), primary_key=True))

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(80), unique=True)
    email: Mapped[str] = mapped_column(String(120), unique=True)
    password: Mapped[str] = mapped_column(String(255))
    posts: Mapped[list[Post]] = relationship(back_populates="author")

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        try:
            return bcrypt.check_password_hash(self.password, password)
        except (ValueError, TypeError):
            return False

@login_manager.user_loader
def load_user(user_id):
    try:
        return db.session.get(User, int(user_id))
    except (ValueError, TypeError):
        return None

class Tag(db.Model):
    __tablename__ = "tags"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), unique=True)
    posts: Mapped[list[Post]] = relationship(secondary=post_tags, back_populates="tags")
