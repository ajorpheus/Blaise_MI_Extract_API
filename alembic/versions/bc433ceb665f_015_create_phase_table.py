"""015_create_phase_table

Revision ID: bc433ceb665f
Revises: fc94baf2c0c9
Create Date: 2019-04-05 15:45:56.670326

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc433ceb665f'
down_revision = 'fc94baf2c0c9'
branch_labels = None
depends_on = None


def upgrade():
    phase = op.create_table('phase'
                           , sa.Column('id', sa.VARCHAR(length=255), primary_key=True, nullable=False)
                           , sa.Column('description', sa.VARCHAR(length=255))
                           )

    op.bulk_insert(
        phase,
        [
            {"id": "Live", "description": "Live"},
            {"id": "Training", "description": "Training"},
            {"id": "Editing", "description": "Editing"},
        ]
    )


def downgrade():
    op.drop_table('phase')
