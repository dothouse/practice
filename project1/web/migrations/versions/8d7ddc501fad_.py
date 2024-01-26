"""empty message

Revision ID: 8d7ddc501fad
Revises: 5b477be75e88
Create Date: 2024-01-20 17:11:09.608150

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d7ddc501fad'
down_revision = '5b477be75e88'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('select_data', schema=None) as batch_op:
        batch_op.add_column(sa.Column('month_str', sa.String(length=200), nullable=False))
        batch_op.add_column(sa.Column('spot1_str', sa.String(length=200), nullable=False))
        batch_op.add_column(sa.Column('spot2_str', sa.String(length=200), nullable=False))
        batch_op.add_column(sa.Column('food_str', sa.String(length=200), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('select_data', schema=None) as batch_op:
        batch_op.drop_column('food_str')
        batch_op.drop_column('spot2_str')
        batch_op.drop_column('spot1_str')
        batch_op.drop_column('month_str')

    # ### end Alembic commands ###
