from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, BOOLEAN, DATETIME, TEXT
from sqlalchemy.ext.declarative import declarative_base

from blaise_mi_extract_api.extensions import db

Base = declarative_base()


class ApiKey(db.Model, UserMixin):
    # uncomment the tables args for SQL Server schemas
    # __table_args__ = {"schema": "dbo"}
    id = db.Column(db.Integer(), primary_key=True)
    user = db.Column(db.String(255))
    api_key = db.Column(db.String(255))


class Survey(db.Model):
    # uncomment the tables args for SQL Server schemas
    # __table_args__ = {"schema": "dbo"}
    id = db.Column(db.Integer(), primary_key=True)
    tla = db.Column(db.String(3))
    survey_name = db.Column(db.String(255))
    start_date = db.Column(db.Date())
    end_date = db.Column(db.Date())
    allocation_req = db.Column(db.Boolean())
    editing_req = db.Column(db.Boolean())
    allocation_lookup = db.Column(db.String(255))


class DictMixin(object):
    def merge_dict(self, source_dict):
        for key, value in source_dict.items():
            key = key.lower()
            if hasattr(self, key):
                if value == '':
                    setattr(self, key, None)
                else:
                    setattr(self, key, value)


class Case(db.Model, DictMixin):
    id = db.Column(db.Integer(), primary_key=True)
    survey_id = db.Column(db.Integer())
    field_period_id = db.Column(db.Integer())
    sample_id = db.Column(db.Integer(), db.ForeignKey('sample.id'))
    primary_key = db.Column(db.Integer())
    issue_number = db.Column(db.Integer())
    mode = db.Column(db.String(255))
    phase = db.Column(db.String())
    case_status = db.Column(db.String(255))
    allocation_status = db.Column(db.String(255))
    deployment_status = db.Column(db.String(255))
    interviewer_id = db.Column(db.Integer())
    manager_id = db.Column(db.Integer())
    serial_number = db.Column(db.String(255))
    household = db.Column(db.Integer())
    outcome_code = db.Column(db.Integer())
    server_park_id = db.Column(db.Integer())
    instrument_id = db.Column(db.Integer())
    worth_reissue = db.Column(db.Boolean())
    date_created = db.Column(db.DATETIME())
    fed_forward_data = db.Column(db.TEXT())


class CaseResponse(db.Model):
    id = Column(Integer(), primary_key=True)
    case_id = Column(Integer(), db.ForeignKey('case.id'))
    response_data = Column(TEXT())