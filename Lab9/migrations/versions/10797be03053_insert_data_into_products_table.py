"""Insert personal example products using a manual data migration"""
from alembic import op
import sqlalchemy as sa
revision = "10797be03053"
down_revision = "9a7e3d28377c"
branch_labels = None
depends_on = None

def upgrade():
    conn = op.get_bind()
    for category in ("Ноутбуки", "Комп’ютерні мишки"):
        conn.execute(sa.text("INSERT INTO categories (name) SELECT :n WHERE NOT EXISTS (SELECT 1 FROM categories WHERE name=:n)"), {"n":category})
    for name, price, category, active in (
        ("Lenovo LOQ 15", 42999.0, "Ноутбуки", 1),
        ("Razer DeathAdder V3", 2499.0, "Комп’ютерні мишки", 1),
    ):
        conn.execute(sa.text("""INSERT INTO products (name,price,category_id,active,created_at)
            SELECT :n,:p,id,:a,CURRENT_TIMESTAMP FROM categories WHERE name=:c
            AND NOT EXISTS (SELECT 1 FROM products WHERE name=:n)"""), {"n":name,"p":price,"c":category,"a":active})

def downgrade():
    conn=op.get_bind()
    conn.execute(sa.text("DELETE FROM products WHERE name IN ('Lenovo LOQ 15','Razer DeathAdder V3')"))
    conn.execute(sa.text("DELETE FROM categories WHERE name IN ('Ноутбуки','Комп’ютерні мишки') AND NOT EXISTS (SELECT 1 FROM products WHERE products.category_id=categories.id)"))
