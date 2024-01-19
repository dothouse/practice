"""empty message

Revision ID: 72fe4693532c
Revises: 18dcaa5c238e
Create Date: 2024-01-19 12:44:12.015564

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72fe4693532c'
down_revision = '18dcaa5c238e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pensionID', sa.String(length=200), nullable=False),
    sa.Column('type', sa.Float(), nullable=False),
    sa.Column('cnt_1km', sa.Float(), nullable=False),
    sa.Column('cnt_2km', sa.Float(), nullable=False),
    sa.Column('cnt_3km', sa.Float(), nullable=False),
    sa.Column('cnt_5km', sa.Float(), nullable=False),
    sa.Column('cnt_10km', sa.Float(), nullable=False),
    sa.Column('cnt_15km', sa.Float(), nullable=False),
    sa.Column('cnt_20km', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['pensionID'], ['pension.pensionID'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('test_data')
    # ### end Alembic commands ###
