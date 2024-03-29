"""empty message

Revision ID: 8b3c40fc3c2f
Revises: 6009643e23d2
Create Date: 2023-02-13 16:14:54.831025

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b3c40fc3c2f'
down_revision = '6009643e23d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.drop_column('created')
        batch_op.drop_column('edited')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('edited', sa.VARCHAR(length=250), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('created', sa.VARCHAR(length=250), autoincrement=False, nullable=True))

    # ### end Alembic commands ###
