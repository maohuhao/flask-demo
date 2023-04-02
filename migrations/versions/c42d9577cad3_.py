"""empty message

Revision ID: c42d9577cad3
Revises: 2f78cee33765
Create Date: 2023-03-30 16:58:34.492720

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c42d9577cad3'
down_revision = '2f78cee33765'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('enterprise_rank', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('reg_no', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('credit_no', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('org_no', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('category', sa.String(length=10), nullable=True))
        batch_op.add_column(sa.Column('econ_kind', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('scope', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('term_start', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('term_end', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('check_date', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('belong_org', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('oper_name', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('oper_type', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('oper_name_id', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('start_date', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('end_date', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('status', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('type', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('type_desc', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('title', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('longitude', sa.Float(asdecimal=True), nullable=True))
        batch_op.add_column(sa.Column('latitude', sa.Float(asdecimal=True), nullable=True))
        batch_op.add_column(sa.Column('gd_longitude', sa.Float(asdecimal=True), nullable=True))
        batch_op.add_column(sa.Column('gd_latitude', sa.Float(asdecimal=True), nullable=True))
        batch_op.add_column(sa.Column('obj_id', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('row_update_time', sa.DateTime(), nullable=False))
        batch_op.add_column(sa.Column('province_code', sa.String(length=10), nullable=True))
        batch_op.add_column(sa.Column('district_code', sa.String(length=10), nullable=True))
        batch_op.add_column(sa.Column('title_code', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('econ_kind_code', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('regist_capi_new', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('currency_unit', sa.String(length=10), nullable=True))
        batch_op.add_column(sa.Column('belong_org_code', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('credit_area_code', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('new_status_code', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('type_new', sa.String(length=20), nullable=True))
        batch_op.add_column(sa.Column('category_new', sa.String(length=20), nullable=True))
        batch_op.add_column(sa.Column('out_time', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('diaoxiao_time', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('regist_capi', sa.Float(asdecimal=True), nullable=True))
        batch_op.add_column(sa.Column('created_time', sa.String(length=100), nullable=True))
        batch_op.alter_column('name',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=255),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('enterprise_rank', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=True)
        batch_op.drop_column('created_time')
        batch_op.drop_column('regist_capi')
        batch_op.drop_column('diaoxiao_time')
        batch_op.drop_column('out_time')
        batch_op.drop_column('category_new')
        batch_op.drop_column('type_new')
        batch_op.drop_column('new_status_code')
        batch_op.drop_column('credit_area_code')
        batch_op.drop_column('belong_org_code')
        batch_op.drop_column('currency_unit')
        batch_op.drop_column('regist_capi_new')
        batch_op.drop_column('econ_kind_code')
        batch_op.drop_column('title_code')
        batch_op.drop_column('district_code')
        batch_op.drop_column('province_code')
        batch_op.drop_column('row_update_time')
        batch_op.drop_column('obj_id')
        batch_op.drop_column('gd_latitude')
        batch_op.drop_column('gd_longitude')
        batch_op.drop_column('latitude')
        batch_op.drop_column('longitude')
        batch_op.drop_column('title')
        batch_op.drop_column('type_desc')
        batch_op.drop_column('type')
        batch_op.drop_column('status')
        batch_op.drop_column('end_date')
        batch_op.drop_column('start_date')
        batch_op.drop_column('oper_name_id')
        batch_op.drop_column('oper_type')
        batch_op.drop_column('oper_name')
        batch_op.drop_column('belong_org')
        batch_op.drop_column('check_date')
        batch_op.drop_column('term_end')
        batch_op.drop_column('term_start')
        batch_op.drop_column('scope')
        batch_op.drop_column('econ_kind')
        batch_op.drop_column('category')
        batch_op.drop_column('org_no')
        batch_op.drop_column('credit_no')
        batch_op.drop_column('reg_no')
        batch_op.drop_column('id')

    # ### end Alembic commands ###