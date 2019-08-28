"""006 db v2 changes

Revision ID: 32418cc20656
Revises: 9c11831d4136
Create Date: 2019-03-21 09:55:23.837474

"""
from alembic import op
from sqlalchemy.dialects.mysql.types import TINYINT
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32418cc20656'
down_revision = '9c11831d4136'
branch_labels = None
depends_on = None


def upgrade():

    op.drop_constraint('case_ibfk_3', 'case', type_='foreignkey')
    op.alter_column(table_name='sample', column_name='id', new_column_name='sample_id', existing_type=sa.INTEGER
                    , nullable=False, autoincrement=True)
    op.create_foreign_key('fk_case_sample', 'case', 'sample', ['sample_id'], ['sample_id'])
    op.alter_column(table_name='sample', column_name='prev_case_id', new_column_name='previous_case_id'
                    , existing_type=sa.INTEGER)
    op.add_column('sample', sa.Column('tla', sa.VARCHAR(length=3)))
    op.add_column('sample', sa.Column('stage', sa.VARCHAR(length=255)))
    op.add_column('sample', sa.Column('phase', sa.VARCHAR(length=255)))
    op.add_column('sample', sa.Column('year', sa.VARCHAR(length=4)))
    op.add_column('sample', sa.Column('month', sa.VARCHAR(length=2)))
    op.add_column('sample', sa.Column('quota', sa.VARCHAR(length=255)))
    op.add_column('sample', sa.Column('address_no', sa.VARCHAR(length=255)))
    op.add_column('sample', sa.Column('wave', sa.INTEGER))
    op.add_column('sample', sa.Column('subsample', sa.INTEGER))
    op.add_column('sample', sa.Column('name', sa.VARCHAR(length=255)))
    op.add_column('sample', sa.Column('telephone_number', sa.VARCHAR(length=255)))
    op.add_column('sample', sa.Column('div_add_ind', sa.INTEGER))
    op.add_column('sample', sa.Column('latitude', sa.FLOAT))
    op.add_column('sample', sa.Column('longitude', sa.FLOAT))
    op.add_column('sample', sa.Column('databag', sa.VARCHAR(length=255)))
    op.add_column('sample', sa.Column('date_created', sa.DATE))
    op.drop_column('sample', 'geographies')

    op.alter_column(table_name='address', column_name='id', new_column_name='address_id', existing_type=sa.INTEGER
                    , nullable=False, autoincrement=True)
    op.create_unique_constraint('uq_address_case', 'address', ['case_id'])
    op.create_foreign_key('fk_case_address', 'case', 'address', ['id'], ['case_id'])

    op.alter_column(table_name='survey', column_name='FTF', new_column_name='ftf', existing_type=TINYINT)
    op.alter_column(table_name='survey', column_name='TEL', new_column_name='tel', existing_type=TINYINT)
    op.alter_column(table_name='survey', column_name='IPS', new_column_name='ips', existing_type=TINYINT)
    op.alter_column(table_name='survey', column_name='WEB', new_column_name='web', existing_type=TINYINT)

    op.drop_constraint('field_period_ibfk_1', 'field_period', type_='foreignkey')
    op.drop_column('field_period', 'survey_id')
    op.drop_column('field_period', 'instrument_name')
    op.drop_column('field_period', 'survey_mode')
    op.drop_column('field_period', 'server_park_id')
    op.alter_column(table_name='field_period', column_name='results_start_date'
                    , new_column_name='data_delivery_start_date', existing_type=sa.DATE)

    op.create_table('role'
                    , sa.Column('id', sa.INTEGER, primary_key=True, nullable=False)
                    , sa.Column('description', sa.VARCHAR(length=255))
                    )

    op.create_table('user_server_park'
                    , sa.Column('user_id', sa.INTEGER, nullable=False)
                    , sa.Column('server_park_id', sa.INTEGER, nullable=False)
                    )


def downgrade():

    op.drop_table('user_server_park')

    op.drop_table('role')

    op.alter_column(table_name='field_period', column_name='data_delivery_start_date'
                    , new_column_name='results_start_date', existing_type=sa.DATE)
    op.add_column('field_period', sa.Column('server_park_id', sa.INTEGER))
    op.add_column('field_period', sa.Column('survey_mode', sa.VARCHAR(length=255)))
    op.add_column('field_period', sa.Column('instrument_name', sa.VARCHAR(length=255)))
    op.add_column('field_period', sa.Column('survey_id', sa.INTEGER))
    op.create_foreign_key('fk_field_period_survey', 'field_period', 'survey', ['survey_id'], ['id'])

    op.alter_column(table_name='survey', column_name='ftf', new_column_name='FTF', existing_type=TINYINT)
    op.alter_column(table_name='survey', column_name='tel', new_column_name='TEL', existing_type=TINYINT)
    op.alter_column(table_name='survey', column_name='ips', new_column_name='IPS', existing_type=TINYINT)
    op.alter_column(table_name='survey', column_name='web', new_column_name='WEB', existing_type=TINYINT)

    op.drop_constraint('fk_case_address', 'case', type_='foreignkey')
    op.drop_constraint('uq_address_case', 'address', type_='unique')
    op.alter_column(table_name='address', column_name='address_id', new_column_name='id', existing_type=sa.INTEGER
                    , nullable=False, autoincrement=True)

    op.add_column('sample', sa.Column('geographies', sa.VARCHAR(length=255)))
    op.drop_column('sample', 'date_created')
    op.drop_column('sample', 'databag')
    op.drop_column('sample', 'longitude')
    op.drop_column('sample', 'latitude')
    op.drop_column('sample', 'div_add_ind')
    op.drop_column('sample', 'telephone_number')
    op.drop_column('sample', 'name')
    op.drop_column('sample', 'subsample')
    op.drop_column('sample', 'wave')
    op.drop_column('sample', 'address_no')
    op.drop_column('sample', 'quota')
    op.drop_column('sample', 'month')
    op.drop_column('sample', 'year')
    op.drop_column('sample', 'phase')
    op.drop_column('sample', 'stage')
    op.drop_column('sample', 'tla')
    op.alter_column(table_name='sample', column_name='previous_case_id', new_column_name='prev_case_id'
                    , existing_type=sa.INTEGER)
    op.drop_constraint('fk_case_sample', 'case', type_='foreignkey')
    op.alter_column(table_name='sample', column_name='sample_id', new_column_name='id', existing_type=sa.INTEGER
                    , nullable=False, autoincrement=True)
    op.create_foreign_key('fk_case_sample', 'case', 'sample', ['sample_id'], ['id'])
