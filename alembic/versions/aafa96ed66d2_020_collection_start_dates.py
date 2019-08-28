"""020_collection_start_dates

Revision ID: aafa96ed66d2
Revises: 30f5d54c4f6a
Create Date: 2019-05-21 10:04:30.375042

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import DATE


# revision identifiers, used by Alembic.
revision = 'aafa96ed66d2'
down_revision = '30f5d54c4f6a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('instrument', sa.Column('collection_start_date', DATE))
    op.add_column('instrument', sa.Column('collection_end_date', DATE))


def downgrade():
    op.drop_column('instrument', 'collection_start_date')
    op.drop_column('instrument', 'collection_end_date')
