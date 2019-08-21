"""011-upadte_to_sampe_header

Revision ID: 1917ff7bf695
Revises: 4ac6c003dffd
Create Date: 2019-03-30 01:33:54.266414

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import INTEGER
from sqlalchemy import VARCHAR


# revision identifiers, used by Alembic.
revision = '1917ff7bf695'
down_revision = '4ac6c003dffd'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('sample_header', sa.Column('survey_id', INTEGER))
    op.add_column('sample_header', sa.Column('field_period_id', INTEGER))
    op.add_column('sample_header', sa.Column('mode', VARCHAR(20)))
    op.add_column('sample_header', sa.Column('phase', VARCHAR(50)))
    op.drop_column('sample', 'field_period_id')
    op.alter_column(table_name='sample', column_name='mode'
                    , new_column_name='mode', existing_type=sa.VARCHAR(20))
    op.alter_column(table_name='sample', column_name='phase'
                    , new_column_name='phase', existing_type=sa.VARCHAR(50))
    op.alter_column(table_name='sample_header', column_name='date_created'
                    , new_column_name='date_created', existing_type=sa.DATETIME())


def downgrade():
    op.alter_column(table_name='sample_header', column_name='date_created'
                     , new_column_name='date_created', existing_type=sa.DATE)
    op.alter_column(table_name='sample', column_name='mode'
                    , new_column_name='mode', existing_type=sa.VARCHAR(255))
    op.alter_column(table_name='sample', column_name='phase'
                    , new_column_name='phase', existing_type=sa.VARCHAR(255))
    op.add_column('sample', sa.Column('field_period_id', INTEGER))
    op.drop_column('sample_header', 'survey_id')
    op.drop_column('sample_header', 'field_period_id')
    op.drop_column('sample_header', 'mode')
    op.drop_column('sample_header', 'phase')
