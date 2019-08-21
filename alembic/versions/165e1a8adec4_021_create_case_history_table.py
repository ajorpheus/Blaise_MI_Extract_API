"""create case history table

Revision ID: 165e1a8adec4
Revises: aafa96ed66d2
Create Date: 2019-05-22 11:27:48.556000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.mysql.types import INTEGER
from sqlalchemy.dialects.mysql.types import VARCHAR
from sqlalchemy.dialects.mysql.types import DATETIME


# revision identifiers, used by Alembic.
revision = '165e1a8adec4'
down_revision = 'aafa96ed66d2'
branch_labels = None
depends_on = None


def upgrade():
    # new case history table
    op.create_table('case_history',
                    sa.Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
                    sa.Column('status', VARCHAR(length=255)),
                    sa.Column('description', VARCHAR(length=255)),
                    sa.Column('date_created', DATETIME())
                    )


def downgrade():
    op.drop_table('case_history')
