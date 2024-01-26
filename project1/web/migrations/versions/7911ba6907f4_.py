"""empty message

Revision ID: 7911ba6907f4
Revises: f4a4175f9ceb
Create Date: 2024-01-19 20:09:33.013713

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7911ba6907f4'
down_revision = 'f4a4175f9ceb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('parm',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('addr', sa.String(length=200), nullable=False),
    sa.Column('lat', sa.Float(), nullable=False),
    sa.Column('lng', sa.Float(), nullable=False),
    sa.Column('dong', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('sum2')
    with op.batch_alter_table('hospital', schema=None) as batch_op:
        batch_op.alter_column('sat',
               existing_type=sa.FLOAT(),
               type_=sa.Integer(),
               existing_nullable=False)
        batch_op.alter_column('sun',
               existing_type=sa.FLOAT(),
               type_=sa.Integer(),
               existing_nullable=False)
        batch_op.alter_column('holiday',
               existing_type=sa.FLOAT(),
               type_=sa.Integer(),
               existing_nullable=False)
        batch_op.alter_column('type',
               existing_type=sa.FLOAT(),
               type_=sa.Integer(),
               existing_nullable=False)

    with op.batch_alter_table('police', schema=None) as batch_op:
        batch_op.alter_column('type',
               existing_type=sa.FLOAT(),
               type_=sa.Integer(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('police', schema=None) as batch_op:
        batch_op.alter_column('type',
               existing_type=sa.Integer(),
               type_=sa.FLOAT(),
               existing_nullable=False)

    with op.batch_alter_table('hospital', schema=None) as batch_op:
        batch_op.alter_column('type',
               existing_type=sa.Integer(),
               type_=sa.FLOAT(),
               existing_nullable=False)
        batch_op.alter_column('holiday',
               existing_type=sa.Integer(),
               type_=sa.FLOAT(),
               existing_nullable=False)
        batch_op.alter_column('sun',
               existing_type=sa.Integer(),
               type_=sa.FLOAT(),
               existing_nullable=False)
        batch_op.alter_column('sat',
               existing_type=sa.Integer(),
               type_=sa.FLOAT(),
               existing_nullable=False)

    op.create_table('sum2',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=200), nullable=False),
    sa.Column('score', sa.FLOAT(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('parm')
    # ### end Alembic commands ###