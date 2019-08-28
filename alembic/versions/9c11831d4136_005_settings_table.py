"""005 settings table

Revision ID: 9c11831d4136
Revises: 868088b6ec92
Create Date: 2019-03-20 21:52:45.669539

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.mysql.types import INTEGER
from sqlalchemy.dialects.mysql.types import VARCHAR

# revision identifiers, used by Alembic.
revision = '9c11831d4136'
down_revision = '868088b6ec92'
branch_labels = None
depends_on = None


def upgrade():
    # new settings table
    op.create_table('settings',
                    sa.Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
                    sa.Column('key', VARCHAR(length=255)),
                    sa.Column('value', VARCHAR(length=255)),
                    )


def downgrade():
    op.drop_table('settings')
