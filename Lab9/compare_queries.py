import sys
from sqlalchemy import event
from sqlalchemy.orm import joinedload, selectinload
from run import app
from app.extensions import db
from app.posts.models import Post
mode=sys.argv[1] if len(sys.argv)>1 else 'lazy'
assert mode in ('lazy','optimized')
with app.app_context():
    db.session.remove()
    count=[0]
    def track(conn,cursor,statement,parameters,context,executemany):
        if statement.lstrip().upper().startswith('SELECT'):
            count[0]+=1
            print('SQL:',statement,parameters)
    engine=db.engine
    event.listen(engine,'before_cursor_execute',track)
    try:
        stmt=db.select(Post).order_by(Post.id)
        if mode=='optimized': stmt=stmt.options(joinedload(Post.author),selectinload(Post.tags))
        for post in db.session.scalars(stmt):
            print(post.title,post.author.username,[t.name for t in post.tags])
        print('SELECT count:',count[0])
    finally:
        event.remove(engine,'before_cursor_execute',track)
        db.session.remove()
