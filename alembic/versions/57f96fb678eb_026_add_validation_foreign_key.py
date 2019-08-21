"""026_add_validation_foreign_key

Revision ID: 57f96fb678eb
Revises: be8948ee5a17
Create Date: 2019-06-10 16:20:02.909917

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57f96fb678eb'
down_revision = 'be8948ee5a17'
branch_labels = None
depends_on = None


def upgrade():
    op.create_foreign_key('fk_validation_failure', 'validation_failures', 'case', ['case_id'], ['id'], ondelete="CASCADE")


def downgrade():
    op.drop_constraint('fk_validation_failure', 'validation_failures', type_='foreignkey')
