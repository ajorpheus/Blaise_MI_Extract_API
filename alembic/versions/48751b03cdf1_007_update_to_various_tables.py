"""007_Update_to_various_tables

Revision ID: 48751b03cdf1
Revises: 32418cc20656
Create Date: 2019-03-23 01:51:00.647217

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.mysql.types import VARCHAR
from sqlalchemy.dialects.mysql.types import TINYINT
from sqlalchemy.dialects.mysql.types import INTEGER
from sqlalchemy import DATE


# revision identifiers, used by Alembic.
revision = '48751b03cdf1'
down_revision = '32418cc20656'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('sample_header'
                    , sa.Column('id', INTEGER, primary_key=True, nullable=False)
                    , sa.Column('date_created', DATE)
                    , sa.Column('status', VARCHAR(length=255))
                    , sa.Column('sample_count', INTEGER)
                    )
    op.add_column('case', sa.Column('primary_key', INTEGER))
    op.add_column('case', sa.Column('manager_id', INTEGER))
    op.add_column('case', sa.Column('issue_number', INTEGER))
    op.add_column('case', sa.Column('worth_reissue', TINYINT))

    op.add_column('sample', sa.Column('sample_header_id', INTEGER))
    op.create_foreign_key('fk_sample_header_id', 'sample', 'sample_header', ['sample_header_id'], ['id'])

    op.add_column('instrument', sa.Column('mode', VARCHAR(length=255)))
    op.add_column('instrument', sa.Column('phase', VARCHAR(length=255)))
    op.add_column('instrument', sa.Column('description', VARCHAR(length=255)))

    op.drop_column('field_period', 'phase')

    op.create_table('manager_lookup_postcode'
                    , sa.Column('postcode', VARCHAR(length=9), primary_key=True, nullable=False)
                    , sa.Column('manager_id', INTEGER)
                    )

    op.create_table('manager_lookup_quota'
                    , sa.Column('quota', VARCHAR(length=9), primary_key=True, nullable=False)
                    , sa.Column('manager_id', INTEGER)
                    )

    op.add_column('survey', sa.Column('allocation_lookup', VARCHAR(length=255)))

    op.alter_column(table_name='field_period', column_name='scatter_data'
                    , new_column_name='scatter_date', existing_type=sa.DATE)

    op.alter_column(table_name='sample', column_name='seial'
                    , new_column_name='serial', existing_type=sa.DATE)


def downgrade():
    op.alter_column(table_name='sample', column_name='serial'
                    , new_column_name='seial', existing_type=sa.DATE)

    op.alter_column(table_name='field_period', column_name='scatter_date'
                    , new_column_name='scatter_data', existing_type=sa.DATE)

    op.drop_column('survey', 'allocation_lookup')
    op.drop_table('manager_lookup_quota')
    op.drop_table('manager_lookup_postcode')

    op.add_column('field_period', sa.Column('phase', VARCHAR(length=255)))

    op.drop_column('instrument', 'description')
    op.drop_column('instrument', 'phase')
    op.drop_column('instrument', 'mode')

    op.drop_constraint('fk_sample_header_id', 'sample', type_='foreignkey')
    op.drop_column('sample', 'sample_header_id')

    op.drop_column('case', 'worth_reissue')
    op.drop_column('case', 'issue_number')
    op.drop_column('case', 'manager_id')
    op.drop_column('case', 'primary_key')

    op.drop_table('sample_header')
