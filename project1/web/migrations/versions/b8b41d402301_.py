"""empty message

Revision ID: b8b41d402301
Revises: 8d7ddc501fad
Create Date: 2024-01-20 17:14:41.633704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8b41d402301'
down_revision = '8d7ddc501fad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('select_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('month', sa.INTEGER(), nullable=False),
    sa.Column('month_str', sa.String(length=200), nullable=False),
    sa.Column('spot1', sa.INTEGER(), nullable=False),
    sa.Column('spot1_str', sa.String(length=200), nullable=False),
    sa.Column('spot2', sa.INTEGER(), nullable=False),
    sa.Column('spot2_str', sa.String(length=200), nullable=False),
    sa.Column('food', sa.INTEGER(), nullable=False),
    sa.Column('food_str', sa.String(length=200), nullable=False),
    sa.Column('pet', sa.INTEGER(), nullable=False),
    sa.Column('pool', sa.INTEGER(), nullable=False),
    sa.Column('garden', sa.INTEGER(), nullable=False),
    sa.Column('sea', sa.INTEGER(), nullable=False),
    sa.Column('nocost', sa.INTEGER(), nullable=False),
    sa.Column('bus', sa.INTEGER(), nullable=False),
    sa.Column('police', sa.INTEGER(), nullable=False),
    sa.Column('hospital', sa.INTEGER(), nullable=False),
    sa.Column('bank', sa.INTEGER(), nullable=False),
    sa.Column('mart', sa.INTEGER(), nullable=False),
    sa.Column('gift', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('select_data')
    # ### end Alembic commands ###