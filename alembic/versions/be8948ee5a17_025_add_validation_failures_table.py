"""025_add_validation_failures_table

Revision ID: be8948ee5a17
Revises: b2ffda756f71
Create Date: 2019-06-10 14:20:10.688679

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be8948ee5a17'
down_revision = 'b2ffda756f71'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('validation_failures'
                    , sa.Column('id', sa.Integer(), primary_key=True, nullable=False)
                    , sa.Column('case_id',  sa.Integer())
                    , sa.Column('error_description', sa.VARCHAR(length=255))
                    , sa.Column('date_created', sa.DATETIME())
                    )


def downgrade():
    op.drop_table('validation_failures')
