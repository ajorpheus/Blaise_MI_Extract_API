"""029_Add_feed_forward_column_to_case_table

Revision ID: f7a559e286f3
Revises: 0044ac36af30
Create Date: 2019-06-27 09:15:17.693697

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7a559e286f3'
down_revision = '0044ac36af30'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('case', sa.Column('fed_forward_data', sa.TEXT))


def downgrade():
    op.drop_column('case', 'fed_forward_data')
