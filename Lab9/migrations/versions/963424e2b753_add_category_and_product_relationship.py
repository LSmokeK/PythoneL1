"""Add Category and Product relationship"""
from alembic import op
import sqlalchemy as sa
revision = "963424e2b753"
down_revision = "90ca3068bf89"
branch_labels = None
depends_on = None

def upgrade():
    op.create_table("categories",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=128), nullable=False),
        sa.PrimaryKeyConstraint("id", name="pk_categories"),
        sa.UniqueConstraint("name", name="uq_categories_name"))
    with op.batch_alter_table("products") as batch_op:
        batch_op.add_column(sa.Column("category_id", sa.Integer(), nullable=True))
        batch_op.create_foreign_key("fk_products_category_id_categories", "categories", ["category_id"], ["id"])

def downgrade():
    with op.batch_alter_table("products") as batch_op:
        batch_op.drop_constraint("fk_products_category_id_categories", type_="foreignkey")
        batch_op.drop_column("category_id")
    op.drop_table("categories")
