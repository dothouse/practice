"""empty message

Revision ID: c233c0530e88
Revises: d87879cf4104
Create Date: 2024-01-22 21:16:17.872720

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c233c0530e88'
down_revision = 'd87879cf4104'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pm',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(length=200), nullable=False),
    sa.Column('강정동', sa.Float(), nullable=False),
    sa.Column('남원읍', sa.Float(), nullable=False),
    sa.Column('대정읍', sa.Float(), nullable=False),
    sa.Column('동홍동', sa.Float(), nullable=False),
    sa.Column('성산읍', sa.Float(), nullable=False),
    sa.Column('애월읍', sa.Float(), nullable=False),
    sa.Column('연동', sa.Float(), nullable=False),
    sa.Column('이도동', sa.Float(), nullable=False),
    sa.Column('조천읍', sa.Float(), nullable=False),
    sa.Column('한림읍', sa.Float(), nullable=False),
    sa.Column('화북동', sa.Float(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('month', sa.Integer(), nullable=False),
    sa.Column('day', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pm_point',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('addr', sa.String(length=200), nullable=False),
    sa.Column('lat', sa.Float(), nullable=False),
    sa.Column('lng', sa.Float(), nullable=False),
    sa.Column('location', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pm_point')
    op.drop_table('pm')
    # ### end Alembic commands ###