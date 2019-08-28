"""009_api_key_table

Revision ID: 8d9528b2949e
Revises: 78ccfb5de696
Create Date: 2019-03-28 00:27:47.303276

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.mysql.types import INTEGER
from sqlalchemy.dialects.mysql.types import VARCHAR


# revision identifiers, used by Alembic.
revision = '8d9528b2949e'
down_revision = '78ccfb5de696'
branch_labels = None
depends_on = None


def upgrade():
    # new settings table
    op.create_table('api_key',
                    sa.Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
                    sa.Column('user', VARCHAR(length=255)),
                    sa.Column('api_key', VARCHAR(length=255)),
                    )


def downgrade():
    op.drop_table('api_key')
