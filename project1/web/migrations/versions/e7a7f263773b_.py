"""empty message

Revision ID: e7a7f263773b
Revises: 944a9acf5cb4
Create Date: 2024-01-21 21:05:16.597628

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7a7f263773b'
down_revision = '944a9acf5cb4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('spot',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('addr', sa.String(length=200), nullable=False),
    sa.Column('lat', sa.Float(), nullable=False),
    sa.Column('lng', sa.Float(), nullable=False),
    sa.Column('dong', sa.String(length=200), nullable=False),
    sa.Column('spottype', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('gift', schema=None) as batch_op:
        batch_op.alter_column('review_rating',
               existing_type=sa.INTEGER(),
               type_=sa.Float(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('gift', schema=None) as batch_op:
        batch_op.alter_column('review_rating',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               existing_nullable=False)

    op.drop_table('spot')
    # ### end Alembic commands ###
