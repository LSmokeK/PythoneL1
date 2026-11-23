from alembic import op
import sqlalchemy as sa
from werkzeug.security import generate_password_hash
revision = 'lab8_02'
down_revision = 'lab8_01'
branch_labels = depends_on = None
def upgrade():
    conn=op.get_bind()
    for i,name,email in [(1,'Євгеній Вербицький','author1@example.invalid'),(2,'Game Reviewer','author2@example.invalid')]:
        conn.execute(sa.text('INSERT INTO users (id,username,email,password) VALUES (:i,:n,:e,:p)'),dict(i=i,n=name,e=email,p=generate_password_hash(__import__('secrets').token_hex(24))))
    with op.batch_alter_table('posts') as b:
        b.add_column(sa.Column('author_id',sa.Integer(),nullable=True))
        b.add_column(sa.Column('image',sa.String(120),nullable=False,server_default='default.jpg'))
    conn.execute(sa.text('UPDATE posts SET author_id=1'))
    with op.batch_alter_table('posts') as b:
        b.alter_column('author_id',existing_type=sa.Integer(),nullable=False)
        b.create_foreign_key('fk_posts_author_id_users','users',['author_id'],['id'])
        b.drop_column('author')
def downgrade():
    with op.batch_alter_table('posts') as b:
        b.add_column(sa.Column('author',sa.String(20),nullable=False,server_default='Anonymous'))
        b.drop_constraint('fk_posts_author_id_users',type_='foreignkey')
        b.drop_column('author_id')
        b.drop_column('image')
