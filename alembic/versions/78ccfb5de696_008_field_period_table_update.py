"""008_field_period_table_update

Revision ID: 78ccfb5de696
Revises: 48751b03cdf1
Create Date: 2019-03-24 01:51:26.821093

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import DATE



# revision identifiers, used by Alembic.
revision = '78ccfb5de696'
down_revision = '48751b03cdf1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('field_period', sa.Column('live_start_date', DATE))
    op.add_column('field_period', sa.Column('live_end_date', DATE))

    op.alter_column(table_name='field_period', column_name='field_start_date'
                    , new_column_name='interview_start_date', existing_type=sa.DATE)
    op.alter_column(table_name='field_period', column_name='field_end_date'
                    , new_column_name='interview_end_date', existing_type=sa.DATE)


def downgrade():
    op.alter_column(table_name='field_period', column_name='interview_start_date'
                    , new_column_name='field_start_date', existing_type=sa.DATE)
    op.alter_column(table_name='field_period', column_name='interview_end_date'
                    , new_column_name='field_end_date', existing_type=sa.DATE)

    op.drop_column('field_period', 'live_start_date')
    op.drop_column('field_period', 'live_end_date')