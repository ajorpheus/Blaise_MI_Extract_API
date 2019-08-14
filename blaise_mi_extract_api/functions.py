from blaise_mi_extract_api.extensions import db
from blaise_mi_extract_api.models import CaseResponse, Survey, Case
import json


def get_message():
    with open('examples/message.json', 'r') as f:
        message = json.load(f)
    return message


def search_db():
    message = get_message()
    # instrument_id = message.get('instrument_id')
    survey_tla = message.get('tla')
    response = db.session.query(Case)\
        .outerjoin(CaseResponse, Case.id == CaseResponse.case_id)\
        .join(Survey, Case.survey_id == Survey.id)\
        .filter(Survey.tla == survey_tla).all()

    return
