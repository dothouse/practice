"""empty message

Revision ID: 87585821bb21
Revises: 72fe4693532c
Create Date: 2024-01-19 12:46:25.776801

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87585821bb21'
down_revision = '72fe4693532c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('test_data', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('test_data', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'pension', ['pensionID'], ['pensionID'])

    # ### end Alembic commands ###
