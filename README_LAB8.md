# Lab8 — ORM. Зв’язки

Render: Root Directory `Lab8`; Build Command `pip install -r requirements.txt && flask --app run db upgrade && python seed_lab8.py`; Start Command `gunicorn run:app`. Додайте SECRET_KEY.

Локально: виконайте ті самі команди окремо, потім `flask --app run run`. Сторінки /post, /post/create, /post/1.

## Скріншоти пунктів 7–13
`flask --app run shell`:
```python
from app.posts.models import User, Post, Tag
from app.extensions import db
print([(p.id,p.title) for p in db.session.get(User,2).posts])
print([(p.id,p.title) for p in db.session.get(User,1).posts])
print([t.name for t in db.session.get(Post,1).tags])
print([p.title for p in db.session.get(Tag,1).posts])
```
Пункт 8: форма /post/create, список авторів. Пункт 9: таблиця post_tags у DB Browser. Пункт 10: команди shell вище; приклад append: `post=db.session.get(Post,1); tag=db.session.get(Tag,1); post.tags.append(tag) if tag not in post.tags else None; db.session.commit()`.
Пункт 11: вибір кількох тегів у формі. Пункт 12: детальна сторінка поста.
Пункт 13: окремі запуски `python compare_queries.py lazy` та `python compare_queries.py optimized`. Зробіть скріншоти SQL і підсумку. Очікувано для чистої БД з 5 постами, 2 авторами: 8 SELECT проти 2; фактичні числа внесіть після запуску. `flask --app run db history` — історія міграцій.
Другий автор Game Reviewer — демонстраційний. Автори постів не є новою системою входу. Каталог товарів успадковано з Lab7 (TinyDB окремо від ORM). SQLite на Free Render не гарантує постійного збереження.
