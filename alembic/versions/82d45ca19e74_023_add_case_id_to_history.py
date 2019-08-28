"""add_case_id_to_history

Revision ID: 82d45ca19e74
Revises: 4d5f025fcac1
Create Date: 2019-05-30 14:57:12.051874

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82d45ca19e74'
down_revision = '4d5f025fcac1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('case_history', sa.Column('case_id', sa.INTEGER))


def downgrade():
    op.drop_column('case_history', 'case_id')
