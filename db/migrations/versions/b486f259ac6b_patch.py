"""patch

Revision ID: b486f259ac6b
Revises: d3de965618f2
Create Date: 2022-02-18 14:50:16.043404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b486f259ac6b'
down_revision = 'd3de965618f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'Categories', ['id'])
    op.create_unique_constraint(None, 'Cities', ['id'])
    op.create_unique_constraint(None, 'Colors', ['id'])
    op.create_unique_constraint(None, 'Customer_addresses', ['id'])
    op.create_unique_constraint(None, 'Customers', ['id'])
    op.create_unique_constraint(None, 'Delivery_types', ['id'])
    op.create_unique_constraint(None, 'Goods', ['id'])
    op.drop_constraint('Goods_material_list_id_fkey', 'Goods', type_='foreignkey')
    op.drop_column('Goods', 'material_list_id')
    op.create_unique_constraint(None, 'Images', ['id'])
    op.add_column('Material_lists', sa.Column('good_id', sa.Integer(), nullable=False))
    op.create_unique_constraint(None, 'Material_lists', ['id'])
    op.create_foreign_key(None, 'Material_lists', 'Goods', ['good_id'], ['id'], ondelete='CASCADE')
    op.create_unique_constraint(None, 'Materials', ['id'])
    op.create_unique_constraint(None, 'Orders', ['id'])
    op.create_unique_constraint(None, 'Regions', ['id'])
    op.create_unique_constraint(None, 'Sizes', ['id'])
    op.create_unique_constraint(None, 'Statuses', ['id'])
    op.create_unique_constraint(None, 'Streets', ['id'])
    op.create_unique_constraint(None, 'Structure', ['id'])
    op.create_unique_constraint(None, 'Users', ['id'])
    op.create_unique_constraint(None, 'Variation_in_order', ['id'])
    op.create_unique_constraint(None, 'Variations', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Variations', type_='unique')
    op.drop_constraint(None, 'Variation_in_order', type_='unique')
    op.drop_constraint(None, 'Users', type_='unique')
    op.drop_constraint(None, 'Structure', type_='unique')
    op.drop_constraint(None, 'Streets', type_='unique')
    op.drop_constraint(None, 'Statuses', type_='unique')
    op.drop_constraint(None, 'Sizes', type_='unique')
    op.drop_constraint(None, 'Regions', type_='unique')
    op.drop_constraint(None, 'Orders', type_='unique')
    op.drop_constraint(None, 'Materials', type_='unique')
    op.drop_constraint(None, 'Material_lists', type_='foreignkey')
    op.drop_constraint(None, 'Material_lists', type_='unique')
    op.drop_column('Material_lists', 'good_id')
    op.drop_constraint(None, 'Images', type_='unique')
    op.add_column('Goods', sa.Column('material_list_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('Goods_material_list_id_fkey', 'Goods', 'Material_lists', ['material_list_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint(None, 'Goods', type_='unique')
    op.drop_constraint(None, 'Delivery_types', type_='unique')
    op.drop_constraint(None, 'Customers', type_='unique')
    op.drop_constraint(None, 'Customer_addresses', type_='unique')
    op.drop_constraint(None, 'Colors', type_='unique')
    op.drop_constraint(None, 'Cities', type_='unique')
    op.drop_constraint(None, 'Categories', type_='unique')
    # ### end Alembic commands ###
