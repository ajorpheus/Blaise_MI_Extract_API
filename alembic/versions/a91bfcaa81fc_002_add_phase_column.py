"""002_add phase column

Revision ID: a91bfcaa81fc
Revises: 38752356abd9
Create Date: 2019-03-04 12:48:39.349767

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.mysql.types import VARCHAR, INTEGER


# revision identifiers, used by Alembic.
revision = 'a91bfcaa81fc'
down_revision = '38752356abd9'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('field_period', sa.Column('phase', VARCHAR(length=255)))
    op.add_column('field_period', sa.Column('survey_mode', VARCHAR(length=255)))
    op.add_column('field_period', sa.Column('server_park_id', INTEGER(display_width=11)))


def downgrade():
    op.drop_column('field_period', 'phase')
    op.drop_column('field_period', 'survey_mode')
    op.drop_column('field_period', 'server_park_id')
