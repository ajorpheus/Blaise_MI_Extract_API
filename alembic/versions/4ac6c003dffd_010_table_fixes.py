"""010_table_fixes

Revision ID: 4ac6c003dffd
Revises: 8d9528b2949e
Create Date: 2019-03-29 14:41:56.623491

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import INTEGER
from sqlalchemy import VARCHAR
from sqlalchemy import TEXT


# revision identifiers, used by Alembic.
revision = '4ac6c003dffd'
down_revision = '8d9528b2949e'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_constraint('fk_sample_header_id', 'sample', type_='foreignkey')
    op.drop_constraint('fk_case_sample', 'case', type_='foreignkey')
    op.drop_table('sample')
    op.create_table('sample',
                    sa.Column('id', INTEGER(), primary_key=True, nullable=False),
                    sa.Column('sample_header_id', INTEGER()),
                    sa.Column('field_period_id', INTEGER()),
                    sa.Column('serial', INTEGER),
                    sa.Column('surveyyear', VARCHAR(length=20)),
                    sa.Column('tla', sa.VARCHAR(length=3)),
                    sa.Column('stage', sa.VARCHAR(length=10)),
                    sa.Column('mode', VARCHAR(length=255)),
                    sa.Column('phase', sa.VARCHAR(length=255)),
                    sa.Column('year', sa.VARCHAR(length=4)),
                    sa.Column('month', sa.VARCHAR(length=2)),
                    sa.Column('quota', sa.VARCHAR(length=10)),
                    sa.Column('addressno', sa.VARCHAR(length=10)),
                    sa.Column('wave', sa.INTEGER),
                    sa.Column('previous_case_id', INTEGER),
                    sa.Column('oldserial', VARCHAR(length=255)),
                    sa.Column('addresskey', VARCHAR(length=255)),
                    sa.Column('prem1', VARCHAR(length=255)),
                    sa.Column('prem2', VARCHAR(length=255)),
                    sa.Column('prem3', VARCHAR(length=255)),
                    sa.Column('prem4', VARCHAR(length=255)),
                    sa.Column('district', VARCHAR(length=255)),
                    sa.Column('posttown', VARCHAR(length=255)),
                    sa.Column('postcode', VARCHAR(length=255)),
                    sa.Column('divaddind', sa.VARCHAR(length=20)),
                    sa.Column('subsample', sa.VARCHAR(length=25)),
                    sa.Column('latitude', sa.VARCHAR(length=20)),
                    sa.Column('longitude', sa.VARCHAR(length=20)),
                    sa.Column('name', sa.VARCHAR(length=255)),
                    sa.Column('telno', sa.VARCHAR(length=255)),
                    sa.Column('databag', TEXT),
                    sa.Column('date_created', sa.DATE)
                    )
    op.create_foreign_key('fk_sample_header_id', 'sample', 'sample_header', ['sample_header_id'], ['id'])
    op.create_foreign_key('fk_case_sample', 'case', 'sample', ['sample_id'], ['id'])

    op.drop_constraint('fk_case_address', 'case', type_='foreignkey')
    op.create_foreign_key('fk_case_address', 'address', 'case', ['case_id'], ['id'])

    op.create_foreign_key('fk_user', 'user_server_park', 'user', ['user_id'], ['id'])
    op.create_foreign_key('fk_server_park', 'user_server_park', 'server_park', ['server_park_id'], ['id'])


def downgrade():
    op.drop_constraint('fk_user', 'user_server_park', type_='foreignkey')
    op.drop_constraint('fk_server_park', 'user_server_park', type_='foreignkey')

    op.drop_constraint('fk_case_address', 'address', type_='foreignkey')
    op.create_foreign_key('fk_case_address', 'case', 'address', ['id'], ['case_id'])

    op.drop_constraint('fk_case_sample', 'case', type_='foreignkey')
    op.drop_constraint('fk_sample_header_id', 'sample', type_='foreignkey')
    op.drop_table('sample')
    op.create_table('sample',
                    sa.Column('sample_id', INTEGER(), primary_key=True, nullable=False),
                    sa.Column('field_period_id', INTEGER()),
                    sa.Column('serial', INTEGER),
                    sa.Column('mode', sa.VARCHAR(length=255)),
                    sa.Column('previous_case_id', INTEGER),
                    sa.Column('old_serial', INTEGER),
                    sa.Column('prem1', sa.VARCHAR(length=255)),
                    sa.Column('prem2', sa.VARCHAR(length=255)),
                    sa.Column('prem3', sa.VARCHAR(length=255)),
                    sa.Column('prem4', sa.VARCHAR(length=255)),
                    sa.Column('postcode', sa.VARCHAR(length=255)),
                    sa.Column('tla', sa.VARCHAR(length=3)),
                    sa.Column('stage', sa.VARCHAR(length=255)),
                    sa.Column('phase', sa.VARCHAR(length=255)),
                    sa.Column('year', sa.VARCHAR(length=4)),
                    sa.Column('month', sa.VARCHAR(length=2)),
                    sa.Column('quota', sa.VARCHAR(length=255)),
                    sa.Column('address_no', sa.VARCHAR(length=255)),
                    sa.Column('wave', sa.INTEGER),
                    sa.Column('subsample', sa.INTEGER),
                    sa.Column('name', sa.VARCHAR(length=255)),
                    sa.Column('telephone_number', sa.VARCHAR(length=255)),
                    sa.Column('div_add_ind', sa.INTEGER),
                    sa.Column('latitude', sa.FLOAT),
                    sa.Column('longitude', sa.FLOAT),
                    sa.Column('databag', sa.VARCHAR(length=255)),
                    sa.Column('date_created', sa.DATE),
                    sa.Column('sample_header_id', INTEGER())
                    )
    op.create_foreign_key('fk_sample_header_id', 'sample', 'sample_header', ['sample_header_id'], ['id'])
    op.create_foreign_key('fk_case_sample', 'case', 'sample', ['sample_id'], ['sample_id'])

