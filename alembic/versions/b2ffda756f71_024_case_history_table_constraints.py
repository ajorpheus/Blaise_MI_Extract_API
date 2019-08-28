"""Case_history_table_constraints

Revision ID: b2ffda756f71
Revises: 82d45ca19e74
Create Date: 2019-06-04 16:37:01.916397

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2ffda756f71'
down_revision = '82d45ca19e74'
branch_labels = None
depends_on = None


def upgrade():
    op.create_foreign_key('fk_case_history', 'case_history', 'case', ['case_id'], ['id'], ondelete="CASCADE")


def downgrade():
    op.drop_constraint('fk_case_history', 'case_history', type_='foreignkey')
