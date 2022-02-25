"""patch

Revision ID: 3c5b9da898f1
Revises: 41c77c74df9d
Create Date: 2022-02-25 11:52:45.766081

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c5b9da898f1'
down_revision = '41c77c74df9d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Goods', sa.Column('default_variation', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'Goods', 'Variations', ['default_variation'], ['id'], ondelete='CASCADE')
    op.add_column('Variations', sa.Column('size_id', sa.Integer(), nullable=False))
    op.drop_constraint('Variations_size_fkey', 'Variations', type_='foreignkey')
    op.create_foreign_key(None, 'Variations', 'Sizes', ['size_id'], ['id'], ondelete='CASCADE')
    op.drop_column('Variations', 'size')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Variations', sa.Column('size', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'Variations', type_='foreignkey')
    op.create_foreign_key('Variations_size_fkey', 'Variations', 'Sizes', ['size'], ['id'], ondelete='CASCADE')
    op.drop_column('Variations', 'size_id')
    op.drop_constraint(None, 'Goods', type_='foreignkey')
    op.drop_column('Goods', 'default_variation')
    # ### end Alembic commands ###
