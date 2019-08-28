"""018_add_deployement_status

Revision ID: 7c1ac077b253
Revises: 54f5ee4556ee
Create Date: 2019-04-12 11:43:52.737364

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c1ac077b253'
down_revision = '54f5ee4556ee'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('case', sa.Column('deployment_status', sa.VARCHAR(length=255)))
    op.add_column('case', sa.Column('allocation_status', sa.VARCHAR(length=255)))


def downgrade():
    op.drop_column('case', 'deployment_status')
    op.drop_column('case', 'allocation_status')
