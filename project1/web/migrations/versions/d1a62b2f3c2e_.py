"""empty message

Revision ID: d1a62b2f3c2e
Revises: 51176cf9ae47
Create Date: 2024-01-21 21:55:17.141223

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1a62b2f3c2e'
down_revision = '51176cf9ae47'
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
    sa.Column('detailtype', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tour')
    # ### end Alembic commands ###