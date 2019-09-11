from flask_login import UserMixin
from sqlalchemy import Column, Integer, TEXT
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


class FieldPeriod(db.Model):
    # uncomment the tables args for SQL Server schemas
    # __table_args__ = {"schema": "dbo"}
    id = db.Column(db.Integer(), primary_key=True)
    stage = db.Column(db.String(4))
    live_start_date = db.Column(db.Date())
    live_end_date = db.Column(db.Date())
    interview_start_date = db.Column(db.Date())
    interview_end_date = db.Column(db.Date())
    allocation_date = db.Column(db.Date())
    edit_start_date = db.Column(db.Date())
    data_delivery_start_date = db.Column(db.Date())
    scatter_date = db.Column(db.Date())


class Instrument(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))
    survey_id = db.Column(db.Integer())
    field_period_id = db.Column(db.Integer())
    phase = db.Column(db.String(255))
    description = db.Column(db.String(255))
    questionnaire_deployment_status = db.Column(db.String(255))
    case_deployment_status = db.Column(db.String(255))
    collection_start_date = db.Column(db.DATETIME())
    collection_end_date = db.Column(db.DATETIME())
    validation_rules = db.Column(db.TEXT())
    MI_spec = db.Column(db.TEXT())


class DictMixin(object):
    def merge_dict(self, source_dict):
        for key, value in source_dict.items():
            key = key.lower()
            if hasattr(self, key):
                if value == '':
                    setattr(self, key, None)
                else:
                    setattr(self, key, value)


class Sample(db.Model, DictMixin):
    id = db.Column(db.Integer(), primary_key=True)
    # sample_header_id = db.Column(db.Integer(), db.ForeignKey('sample_header.id'))
    serial = db.Column(db.Integer())
    surveyyear = db.Column(db.String(20))
    tla = db.Column(db.String(3))
    stage = db.Column(db.String(10))
    mode = db.Column(db.String(20))
    phase = db.Column(db.String(50))
    year = db.Column(db.String(4))
    month = db.Column(db.String(2))
    quota = db.Column(db.String(10))
    addressno = db.Column(db.String(10))
    wave = db.Column(db.Integer())
    previous_case_id = db.Column(db.Integer())
    oldserial = db.Column(db.Integer())
    addresskey = db.Column(db.String(255))
    prem1 = db.Column(db.String(255))
    prem2 = db.Column(db.String(255))
    prem3 = db.Column(db.String(255))
    prem4 = db.Column(db.String(255))
    district = db.Column(db.String(255))
    posttown = db.Column(db.String(255))
    postcode = db.Column(db.String(255))
    divaddind = db.Column(db.Integer())
    subsample = db.Column(db.String(25))
    latitude = db.Column(db.String(20))
    longitude = db.Column(db.String(20))
    name = db.Column(db.String(255))
    telno = db.Column(db.String(255))
    databag = db.Column(db.Text)
    date_created = db.Column(db.DATETIME())
    cases = db.relationship('Case', cascade="all, delete, delete-orphan", backref='sample')


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
    quota = db.Column(db.Integer())
    address = db.Column(db.Integer())
    hhold = db.Column(db.Integer())
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
