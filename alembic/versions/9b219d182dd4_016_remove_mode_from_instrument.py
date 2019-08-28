"""016_remove_mode_from_instrument

Revision ID: 9b219d182dd4
Revises: bc433ceb665f
Create Date: 2019-04-05 18:50:38.039651

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b219d182dd4'
down_revision = 'bc433ceb665f'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column('instrument', 'mode')


def downgrade():
    op.add_column('instrument', sa.Column('mode', sa.VARCHAR(20)))

