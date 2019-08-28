"""031 add MI spec

Revision ID: 3986797edd1b
Revises: 31e12ee6c114
Create Date: 2019-07-09 11:35:10.996798

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3986797edd1b'
down_revision = '31e12ee6c114'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('instrument', sa.Column('MI_spec', sa.TEXT))


def downgrade():
    op.drop_column('instrument', sa.Column('MI_spec', sa.TEXT))
