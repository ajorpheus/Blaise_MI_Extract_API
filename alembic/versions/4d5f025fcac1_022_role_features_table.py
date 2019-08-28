"""022_role_permissions_features

Revision ID: 4d5f025fcac1
Revises: 165e1a8adec4
Create Date: 2019-05-28 09:39:08.380740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d5f025fcac1'
down_revision = '165e1a8adec4'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_table('role')
    role = op.create_table('role',
                           sa.Column('id', sa.VARCHAR(length=255), primary_key=True, nullable=False),
                           sa.Column('description', sa.VARCHAR(length=255)),
                           sa.Column('features', sa.TEXT())
                    )

    op.bulk_insert(
        role,
        [
            {"id": "DST_TECH", "description": "DST Support", "features": '"interviewing", '
                                                                           '"sample_upload", '
                                                                           '"respondent_search", '
                                                                           '"case_summary", '
                                                                           '"manage_users", '
                                                                           '"manage_surveys", '
                                                                           '"manage_field_periods", '
                                                                           '"manage_server_parks", '
                                                                           '"cati_dashboard"'},
            {"id": "BDSS",  "description": "BDSS Team", "features": '"interviewing",'
                                                                      '"sample_upload",'
                                                                      '"respondent_search",'
                                                                      '"case_summary"'},
            {"id": "Field_Allocation", "description": "Allocations team", "features": '"interviewing"'},
            {"id": "Field_Interviewer", "description": "Field Interviewer", "features": '"interviewing"'},
            {"id": "Field_Manager", "description": "Field Manager", "features": '"interviewing",'
                                                                                  '"respondent_search"'},
            {"id": "Field_Office", "description": "Field office HQ", "features": '"interviewing",'
                                                                                   '"respondent_search",'
                                                                                   '"case_summary"'},
            {"id": "Research", "description": "Research team", "features": '"interviewing","case_summary"'},
            {"id": "Sampling", "description": "Sampling team", "features": '"sample_upload"'},
            {"id": "Sel_Ops", "description": "TO Enquiry line role", "features": '"interviewing",'
                                                                                   '"respondent_search"'},
            {"id": "TO_Interviewer", "description": "TO Interviewer", "features": '"interviewing"'},
            {"id": "TO_Manager", "description": "TO Manager role", "features": '"interviewing",'
                                                                                 '"respondent_search",'
                                                                                 '"cati_dashboard"'},
            {"id": "TO_Planner", "description": "TO Planner role", "features": '"interviewing","cati_dashboard"'},
        ]
    )


def downgrade():
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
