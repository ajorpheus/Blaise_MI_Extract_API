"""019_Add_deployment_status_to_instrument

Revision ID: 30f5d54c4f6a
Revises: 7c1ac077b253
Create Date: 2019-04-13 12:02:07.295537

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30f5d54c4f6a'
down_revision = '7c1ac077b253'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('instrument', sa.Column('questionnaire_deployment_status', sa.VARCHAR(length=255)))
    op.add_column('instrument', sa.Column('case_deployment_status', sa.VARCHAR(length=255)))


def downgrade():
    op.drop_column('instrument', 'case_deployment_status')
    op.drop_column('instrument', 'questionnaire_deployment_status')
