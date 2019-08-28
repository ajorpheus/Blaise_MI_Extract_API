"""012_Fixed_dates_in_tables

Revision ID: 9cbdc262e129
Revises: 1917ff7bf695
Create Date: 2019-04-01 10:02:50.009582

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9cbdc262e129'
down_revision = '1917ff7bf695'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(table_name='address', column_name='start_date'
                    , new_column_name='start_date', existing_type=sa.DATETIME)
    op.add_column('case', sa.Column('date_created', sa.DATETIME))
    op.drop_column('sample_header', 'mode')


def downgrade():
    op.add_column('sample_header', sa.Column('mode', sa.VARCHAR(20)))
    op.drop_column('case', 'date_created')
    op.alter_column(table_name='address', column_name='start_date'
                    , new_column_name='start_date', existing_type=sa.DATE)
