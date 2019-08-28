"""028_Add_validation_mode

Revision ID: 0044ac36af30
Revises: a5a30830ee82
Create Date: 2019-06-26 21:30:53.184268

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0044ac36af30'
down_revision = 'a5a30830ee82'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("INSERT INTO mode (id, description) VALUES ('VAL','Validation')")
    op.execute("DELETE FROM phase WHERE id = 'Editing'")


def downgrade():
    op.execute("DELETE FROM mode WHERE id = 'VAL'")
