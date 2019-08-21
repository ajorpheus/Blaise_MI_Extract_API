"""013_Update_table_cascades

Revision ID: 76ffe3d18bcb
Revises: 9cbdc262e129
Create Date: 2019-04-01 16:56:49.196504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76ffe3d18bcb'
down_revision = '9cbdc262e129'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(table_name='sample', column_name='date_created'
                    , new_column_name='date_created', existing_type=sa.DATETIME)

    op.drop_constraint('fk_sample_header_id', 'sample', type_='foreignkey')
    op.drop_constraint('fk_case_sample', 'case', type_='foreignkey')
    op.drop_constraint('fk_case_address', 'address', type_='foreignkey')

    op.create_foreign_key('fk_sample_header_id', 'sample', 'sample_header',
                          ['sample_header_id'], ['id'], ondelete="CASCADE")
    op.create_foreign_key('fk_case_sample', 'case', 'sample', ['sample_id'], ['id'], ondelete="CASCADE")
    op.create_foreign_key('fk_case_address', 'address', 'case', ['case_id'], ['id'], ondelete="CASCADE")


def downgrade():
    op.alter_column(table_name='sample', column_name='date_created'
                    , new_column_name='date_created', existing_type=sa.DATE)
