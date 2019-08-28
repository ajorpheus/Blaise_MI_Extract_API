"""001_setup inital tables

Revision ID: 38752356abd9
Revises: 
Create Date: 2019-03-04 12:11:09.876897

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.mysql.types import INTEGER
from sqlalchemy.dialects.mysql.types import VARCHAR
from sqlalchemy.dialects.mysql.types import TINYINT
from sqlalchemy import DATE
from sqlalchemy import ForeignKey
from werkzeug.security import generate_password_hash

# revision identifiers, used by Alembic.
revision = '38752356abd9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('survey',
                    sa.Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
                    sa.Column('tla', VARCHAR(length=3)),
                    sa.Column('survey_name', VARCHAR(length=255)),
                    sa.Column('FTF_Survey', TINYINT(display_width=1)),
                    sa.Column('Tel_Survey', TINYINT(display_width=1)),
                    sa.Column('IPS_Survey', TINYINT(display_width=1)),
                    sa.Column('Web_Survey', TINYINT(display_width=1)),
                    )

    op.create_table('field_period',
                    sa.Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
                    sa.Column('stage', VARCHAR(length=4)),
                    sa.Column('instrument_name', VARCHAR(length=255)),
                    sa.Column('start_date', DATE),
                    sa.Column('survey_id', INTEGER(display_width=11), ForeignKey('survey.id')),
                    )

    op.create_table('server_park',
                    sa.Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
                    sa.Column('name', VARCHAR(length=255)),
                    sa.Column('endpoint', VARCHAR(length=255)),
                    )

    user = op.create_table('user',
                           sa.Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
                           sa.Column('username', VARCHAR(length=80)),
                           sa.Column('password', VARCHAR(length=255)),
                           sa.Column('firstname', VARCHAR(length=255)),
                           sa.Column('surname', VARCHAR(length=255)),
                           sa.Column('role', VARCHAR(length=50)),
                           )

    op.bulk_insert(
        user,
        [
            {"username": "admin", "password": generate_password_hash('admin'), "role": "DST_TECH"},
        ]
    )


def downgrade():
    op.drop_table('field_period')
    op.drop_table('server_park')
    op.drop_table('survey')
    op.drop_table('user')

