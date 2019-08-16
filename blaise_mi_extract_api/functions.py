from blaise_mi_extract_api.extensions import db
from blaise_mi_extract_api.models import CaseResponse, Survey, Case, FieldPeriod, Instrument
import json
import ast


# Temporary function to get json request for Management Information.
# The actual request will come from rabbitmq?
def get_json():
    with open('examples/message.json', 'r') as f:
        message = json.load(f)
    return message


def query_management_info():
    # Based on the survey and field period requested by json file, a query for matching responses is returned (even
    # if ones for which the response_data is empty)

    info_request_spec = get_json()
    survey_tla = info_request_spec.get('tla')
    field_period = info_request_spec.get('field_period')

    # Collect all cases (with or without response) with their survey three letter acronym (tla) and field period
    response = db.session.query(Case, CaseResponse)\
        .outerjoin(CaseResponse, Case.id == CaseResponse.case_id)\
        .join(Survey, Case.survey_id == Survey.id)\
        .join(FieldPeriod, Case.field_period_id == FieldPeriod.id)

    # Filter by tla
    response = response.filter(Survey.tla == survey_tla)

    # Filter by field period
    response = response.filter(FieldPeriod.stage == field_period)

    return response


def gather_management_info():
    # Given a query, returns a dictionary based on mi_spec
    return


def remove_field_from_management_info():
    # Given a dictionary with mi_spec and list of fields to remove, and updated dictionary is returned without those
    # fields
    return


def map_to_management_info(mi_query):
    # Assumes the query
    case_list = mi_query.all()

    # Create dictionary with management information requirements, i.e. output fields required for a given instrument
    if len(case_list) != 0:
        management_info = db.session.query(Instrument.MI_spec) \
            .filter(Instrument.id == case_list[0].Case.instrument_id).first()
    else:
        return

    # Dictionary with management information requirements
    management_info = ast.literal_eval(management_info.MI_spec)
    my_dict = {}

    for i, val in enumerate(case_list):
        serial_number = case_list[i].Case.serial_number
        case_response_block = case_list[i].CaseResponse

        if case_response_block is None:
            my_dict[serial_number] = {key: 'NULL' for key in management_info.keys()}
        else:
            # Dictionary with all response_data for a given case
            case_response_dict = ast.literal_eval(case_response_block.response_data)

            # Find keys in case_response_dict which match values in management_info
            # Create {management_info key : case_response_dict value}
            my_dict[serial_number] = {key: case_response_dict[management_info[key]] for key in management_info.keys()}

    # Output dictionary as json
    with open('test.json', 'w') as f:
        json.dump(my_dict, f)

    return

