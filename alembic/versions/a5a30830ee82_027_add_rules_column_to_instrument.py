"""027_Add_rules_column_To_Instrument

Revision ID: a5a30830ee82
Revises: 57f96fb678eb
Create Date: 2019-06-17 15:19:15.368741

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5a30830ee82'
down_revision = '57f96fb678eb'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('instrument', sa.Column('validation_rules', sa.TEXT()))


def downgrade():
    op.drop_column('instrument', 'validation_rules')
