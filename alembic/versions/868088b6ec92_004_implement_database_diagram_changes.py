"""004 Implement database diagram changes

Revision ID: 868088b6ec92
Revises: e1d641a2d6f6
Create Date: 2019-03-18 12:42:40.643224

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import DATE
from sqlalchemy.dialects.mysql.types import INTEGER
from sqlalchemy.dialects.mysql.types import VARCHAR
from sqlalchemy.dialects.mysql.types import TINYINT
from sqlalchemy import ForeignKey

# revision identifiers, used by Alembic.
revision = '868088b6ec92'
down_revision = 'e1d641a2d6f6'
branch_labels = None
depends_on = None


def upgrade():
    # region New Tables
    op.create_table('instrument',
                    sa.Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
                    sa.Column('name', VARCHAR(length=255)),
                    sa.Column('survey_id', INTEGER(display_width=11)),
                    sa.Column('field_period_id', INTEGER(display_width=11)),
                    )

    op.create_table('address',
                    sa.Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
                    sa.Column('case_id', INTEGER(display_width=11)),
                    sa.Column('start_date', DATE),
                    sa.Column('prem1', VARCHAR(length=255)),
                    sa.Column('prem2', VARCHAR(length=255)),
                    sa.Column('prem3', VARCHAR(length=255)),
                    sa.Column('prem4', VARCHAR(length=255)),
                    sa.Column('postcode', VARCHAR(length=255)),
                    )

    op.create_table('sample',
                    sa.Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
                    sa.Column('field_period_id', INTEGER(display_width=11)),
                    sa.Column('seial', INTEGER),
                    sa.Column('mode', VARCHAR(length=255)),
                    sa.Column('prev_case_id', INTEGER),
                    sa.Column('old_serial', INTEGER),
                    sa.Column('prem1', VARCHAR(length=255)),
                    sa.Column('prem2', VARCHAR(length=255)),
                    sa.Column('prem3', VARCHAR(length=255)),
                    sa.Column('prem4', VARCHAR(length=255)),
                    sa.Column('postcode', VARCHAR(length=255)),
                    sa.Column('geographies', VARCHAR(length=255)),
                    )

    op.create_table('case',
                    sa.Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
                    sa.Column('survey_id', INTEGER(display_width=11), ForeignKey('survey.id')),
                    sa.Column('field_period_id', INTEGER(display_width=11), ForeignKey('field_period.id')),
                    sa.Column('sample_id', INTEGER(display_width=11), ForeignKey('sample.id')),
                    sa.Column('mode', VARCHAR(length=255)),
                    sa.Column('phase', VARCHAR(length=255)),
                    sa.Column('case_status', VARCHAR(length=255)),
                    sa.Column('interviewer_id', INTEGER(display_width=11), ForeignKey('user.id')),
                    sa.Column('serial_number', VARCHAR(length=255)),
                    sa.Column('household', INTEGER),
                    sa.Column('outcome_code', INTEGER),
                    sa.Column('server_park_id', INTEGER(display_width=11), ForeignKey('server_park.id')),
                    sa.Column('instrument_id', INTEGER(display_width=11), ForeignKey('instrument.id')),
                    )

    # endregion

    # region Field Period

    # New
    op.add_column('field_period', sa.Column('allocation_date', DATE))
    op.add_column('field_period', sa.Column('scatter_data', DATE))
    op.add_column('field_period', sa.Column('edit_start_date', DATE))
    op.add_column('field_period', sa.Column('results_start_date', DATE))

    # Edit
    op.alter_column(table_name='field_period', column_name='start_date', new_column_name='field_start_date',existing_type = DATE)
    op.alter_column(table_name='field_period', column_name='end_date', new_column_name='field_end_date', existing_type = DATE)

    # endregion

    # region Server Park

    # New
    op.add_column('server_park', sa.Column('mode', VARCHAR(length=255)))
    op.add_column('server_park', sa.Column('phase', VARCHAR(length=255)))

    # endregion

    # region Survey

    # New
    op.add_column('survey', sa.Column('allocation_req', TINYINT(display_width=1)))
    op.add_column('survey', sa.Column('editing_req', TINYINT(display_width=1)))

    # Edit
    op.alter_column(table_name='survey', column_name='FTF_Survey', new_column_name='FTF', existing_type=TINYINT)
    op.alter_column(table_name='survey', column_name='TEL_Survey', new_column_name='TEL', existing_type=TINYINT)
    op.alter_column(table_name='survey', column_name='IPS_Survey', new_column_name='IPS', existing_type=TINYINT)
    op.alter_column(table_name='survey', column_name='Web_Survey', new_column_name='WEB', existing_type=TINYINT)

    # endregion

    # region User

    # New
    op.add_column('user', sa.Column('fieldforce', VARCHAR(length=255)))

    # endregion


def downgrade():

    # region User
    op.drop_column('user', 'fieldforce')
    # endregion

    # region Survey
    op.drop_column('survey', 'allocation_req')
    op.drop_column('survey', 'editing_req')

    op.alter_column(table_name='survey', column_name='FTF', new_column_name='FTF_Survey', existing_type=TINYINT)
    op.alter_column(table_name='survey', column_name='TEL', new_column_name='TEL_Survey', existing_type=TINYINT)
    op.alter_column(table_name='survey', column_name='IPS', new_column_name='IPS_Survey', existing_type=TINYINT)
    op.alter_column(table_name='survey', column_name='WEB', new_column_name='Web_Survey', existing_type=TINYINT)
    # endregion

    # region Server Park
    op.drop_column('server_park', 'mode')
    op.drop_column('server_park', 'phase')
    # endregion

    # region Field Period
    op.drop_column('field_period', 'allocation_date')
    op.drop_column('field_period', 'scatter_data')
    op.drop_column('field_period', 'edit_start_date')
    op.drop_column('field_period', 'results_start_date')

    op.alter_column(table_name='field_period', column_name='field_start_date', new_column_name='start_date',existing_type = DATE)
    op.alter_column(table_name='field_period', column_name='field_end_date', new_column_name='end_date',existing_type = DATE)
    # endregion

    op.drop_table('case')
    op.drop_table('sample')
    op.drop_table('address')
    op.drop_table('instrument')
