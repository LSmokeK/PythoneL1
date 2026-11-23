from alembic import op
import sqlalchemy as sa
revision = 'lab8_03'
down_revision = 'lab8_02'
branch_labels = depends_on = None
def upgrade():
    op.create_table('tags',sa.Column('id',sa.Integer(),primary_key=True),sa.Column('name',sa.String(80),nullable=False,unique=True))
    op.create_table('post_tags',sa.Column('post_id',sa.Integer(),sa.ForeignKey('posts.id'),primary_key=True),sa.Column('tag_id',sa.Integer(),sa.ForeignKey('tags.id'),primary_key=True))
def downgrade():
    op.drop_table('post_tags')
    op.drop_table('tags')
