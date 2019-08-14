from blaise_mi_extract_api.extensions import db
from blaise_mi_extract_api.models import CaseResponse, Survey, Case, FieldPeriod
import json


def get_json():
    with open('examples/message.json', 'r') as f:
        message = json.load(f)
    return message


def search_db():
    info_request_spec = get_json()

    survey_tla = info_request_spec.get('tla')
    field_period = info_request_spec.get('field_period')

    response = db.session.query(Case)\
        .outerjoin(CaseResponse, Case.id == CaseResponse.case_id)\
        .join(Survey, Case.survey_id == Survey.id)\
        .join(FieldPeriod, Case.field_period_id == FieldPeriod.id)\
        .filter(Survey.tla == survey_tla)\
        .filter(FieldPeriod.stage == field_period)\
        .all()

    return
