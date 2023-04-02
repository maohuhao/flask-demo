"""empty message

Revision ID: 2877d23c174a
Revises: 22e165bc8e96
Create Date: 2023-03-30 11:49:16.950661

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2877d23c174a'
down_revision = '22e165bc8e96'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('abnormal', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.Integer(), nullable=False))

    with op.batch_alter_table('executedpersons', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ep_count', sa.Integer(), nullable=True))
        batch_op.drop_column('count')

    with op.batch_alter_table('executions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('executions_count', sa.Integer(), nullable=True))
        batch_op.drop_column('count')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('executions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('count', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
        batch_op.drop_column('executions_count')

    with op.batch_alter_table('executedpersons', schema=None) as batch_op:
        batch_op.add_column(sa.Column('count', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
        batch_op.drop_column('ep_count')

    with op.batch_alter_table('abnormal', schema=None) as batch_op:
        batch_op.drop_column('id')

    # ### end Alembic commands ###