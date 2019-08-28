"""030_add_case_response table

Revision ID: 31e12ee6c114
Revises: f7a559e286f3
Create Date: 2019-07-04 14:02:12.016361

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.mysql.types import INTEGER
from sqlalchemy.dialects.mysql.types import TEXT
from sqlalchemy.dialects.mysql.types import VARCHAR


# revision identifiers, used by Alembic.
revision = '31e12ee6c114'
down_revision = 'f7a559e286f3'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('case_response',
                    sa.Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
                    sa.Column('case_id', INTEGER(display_width=11)),
                    sa.Column('response_data', TEXT()),
                    )
    op.create_foreign_key('fk_case_response', 'case_response', 'case', ['case_id'], ['id'], ondelete="CASCADE")


def downgrade():
    op.drop_constraint('fk_case_response', 'case_response', type_='foreignkey')
    op.drop_table('case_response')
