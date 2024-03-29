"""empty message

Revision ID: cb3f31f6a6d2
Revises: 81c87bed0219
Create Date: 2023-02-16 21:00:01.875180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb3f31f6a6d2'
down_revision = '81c87bed0219'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.add_column(sa.Column('table', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('table_id', sa.Integer(), nullable=True))
        batch_op.drop_column('people_id')
        batch_op.drop_column('planets_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.add_column(sa.Column('planets_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('people_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_column('table_id')
        batch_op.drop_column('table')

    # ### end Alembic commands ###
