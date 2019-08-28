"""017_add_Survey_Mode_Table

Revision ID: 54f5ee4556ee
Revises: 9b219d182dd4
Create Date: 2019-04-08 14:25:19.525204

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.mysql.types import TINYINT

# revision identifiers, used by Alembic.
revision = '54f5ee4556ee'
down_revision = '9b219d182dd4'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('survey_mode'
                            , sa.Column('survey_id', sa.INTEGER(), nullable=False)
                            , sa.Column('mode', sa.VARCHAR(length=255))
                            )

    op.create_foreign_key('fk_survey_id', 'survey_mode', 'survey', ['survey_id'], ['id'])
    op.create_foreign_key('fk_mode', 'survey_mode', 'mode', ['mode'], ['id'])

    op.drop_column('survey', 'ftf')
    op.drop_column('survey', 'tel')
    op.drop_column('survey', 'ips')
    op.drop_column('survey', 'web')


def downgrade():
    op.add_column('survey', sa.Column('ftf', TINYINT(4)))
    op.add_column('survey', sa.Column('tel', TINYINT(4)))
    op.add_column('survey', sa.Column('ips', TINYINT(4)))
    op.add_column('survey', sa.Column('web', TINYINT(4)))

    op.drop_constraint('fk_mode', 'survey_mode', type_='foreignkey')
    op.drop_constraint('fk_survey_id', 'survey_mode', type_='foreignkey')
    op.drop_table('survey_mode')
