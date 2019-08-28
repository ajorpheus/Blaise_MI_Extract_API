"""014_Add_mode_table_and_row_entries

Revision ID: fc94baf2c0c9
Revises: 76ffe3d18bcb
Create Date: 2019-04-05 12:35:18.669208

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc94baf2c0c9'
down_revision = '76ffe3d18bcb'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_table('role')
    role = op.create_table('role'
                    , sa.Column('id', sa.VARCHAR(length=255), primary_key=True, nullable=False)
                    , sa.Column('description', sa.VARCHAR(length=255))
                    )

    op.bulk_insert(
        role,
        [
            {"id": "BDSS", "description": "BDSS Team"},
            {"id": "DST_TECH", "description": "DST Support"},
            {"id": "Sampling", "description": "Sampling team"},
            {"id": "Research", "description": "Research team"},
            {"id": "TO_Planner", "description": "TO Planner role"},
            {"id": "TO_Manager", "description": "TO Manager role"},
            {"id": "Sel_Ops", "description": "TO Enquiry line role"},
            {"id": "TO_Interviewer", "description": "TO Interviewer"},
            {"id": "Field_Office", "description": "Field office HQ"},
            {"id": "Field_Allocation", "description": "Allocations team"},
            {"id": "Field_Manager", "description": "Field Manager"},
            {"id": "Field_Interviewer", "description": "Field Interviewer"},
        ]
    )

    mode = op.create_table('mode'
                    , sa.Column('id', sa.VARCHAR(length=255), primary_key=True, nullable=False)
                    , sa.Column('description', sa.VARCHAR(length=255))
                    )

    op.bulk_insert(
        mode,
        [
            {"id": "FTF", "description": "Face to Face"},
            {"id": "TEL", "description": "Telephone"},
            {"id": "IPS", "description": "IPS"},
            {"id": "WEB", "description": "Web Survey"},
        ]
    )

    op.drop_constraint('fk_server_park', 'user_server_park', type_='foreignkey')
    op.drop_constraint('fk_user', 'user_server_park', type_='foreignkey')

    op.create_foreign_key('fk_user', 'user_server_park', 'user', ['user_id'], ['id'], ondelete="CASCADE")
    op.create_foreign_key('fk_server_park', 'user_server_park', 'server_park', ['server_park_id'], ['id'], ondelete="CASCADE")


def downgrade():
    op.drop_table('mode')
    op.drop_table('role')
    op.create_table('role'
                    , sa.Column('id', sa.INTEGER, primary_key=True, nullable=False)
                    , sa.Column('description', sa.VARCHAR(length=255))
                    )



