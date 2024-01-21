"""empty message

Revision ID: 51176cf9ae47
Revises: d1ebb7529752
Create Date: 2024-01-21 21:30:35.594497

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51176cf9ae47'
down_revision = 'd1ebb7529752'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tour',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('addr', sa.String(length=200), nullable=False),
    sa.Column('lat', sa.Float(), nullable=False),
    sa.Column('lng', sa.Float(), nullable=False),
    sa.Column('dong', sa.String(length=200), nullable=False),
    sa.Column('detailtype', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tour')
    # ### end Alembic commands ###
