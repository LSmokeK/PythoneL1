"""Add created_at with server_default"""
from alembic import op
import sqlalchemy as sa
revision = "9a7e3d28377c"
down_revision = "d868f908b836"
branch_labels = None
depends_on = None

def upgrade():
    with op.batch_alter_table("products") as batch_op:
        batch_op.add_column(sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")))

def downgrade():
    with op.batch_alter_table("products") as batch_op:
        batch_op.drop_column("created_at")
