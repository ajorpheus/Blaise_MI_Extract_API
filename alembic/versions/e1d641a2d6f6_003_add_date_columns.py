"""003_add date columns

Revision ID: e1d641a2d6f6
Revises: a91bfcaa81fc
Create Date: 2019-03-07 12:46:39.751739

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import DATE


# revision identifiers, used by Alembic.
revision = 'e1d641a2d6f6'
down_revision = 'a91bfcaa81fc'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('field_period', sa.Column('end_date', DATE))
    op.add_column('survey', sa.Column('start_date', DATE))
    op.add_column('survey', sa.Column('end_date', DATE))


def downgrade():
    op.drop_column('field_period', 'end_date')
    op.drop_column('survey', 'start_date')
    op.drop_column('survey', 'end_date')
