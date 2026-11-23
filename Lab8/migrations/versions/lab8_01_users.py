from alembic import op
import sqlalchemy as sa
revision = 'lab8_01'
down_revision = '10797be03053'
branch_labels = depends_on = None
def upgrade():
    op.create_table('users', sa.Column('id',sa.Integer(),primary_key=True),sa.Column('username',sa.String(80),nullable=False,unique=True),sa.Column('email',sa.String(120),nullable=False,unique=True),sa.Column('password',sa.String(255),nullable=False))
def downgrade():
    op.drop_table('users')
