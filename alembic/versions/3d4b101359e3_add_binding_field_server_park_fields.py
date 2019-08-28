"""add_binding_field_server_park_fields

Revision ID: 3d4b101359e3
Revises: 3986797edd1b
Create Date: 2019-07-25 22:13:28.123057

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d4b101359e3'
down_revision = '3986797edd1b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('server_park', sa.Column('internal_name', sa.VARCHAR(255)))
    op.add_column('server_park', sa.Column('binding', sa.VARCHAR(255)))


def downgrade():
    op.drop_column('server_park', 'internal_name')
    op.drop_column('server_park', 'binding')
