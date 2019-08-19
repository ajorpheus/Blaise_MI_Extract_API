from blaise_mi_extract_api.extensions import db
from blaise_mi_extract_api.models import CaseResponse, Survey, Case, FieldPeriod, Instrument, Sample
import json
import ast


# Temporary function to get json request for Management Information.
# The actual request will come from rabbitmq?
def get_json():
    with open('examples/message.json', 'r') as f:
        message = json.load(f)
    return message


def query_tla_field_period(survey_tla, field_period):
    # Based on the survey and field period provided, a query for matching responses is returned (even
    # if ones for which the response_data is empty)

    # Collect all cases (with or without response) with their survey three letter acronym (tla) and field period
    response_query = db.session.query(Case, CaseResponse) \
        .outerjoin(CaseResponse, Case.id == CaseResponse.case_id) \
        .join(Survey, Case.survey_id == Survey.id) \
        .join(FieldPeriod, Case.field_period_id == FieldPeriod.id)

    # Filter by tla
    response_query = response_query.filter(Survey.tla == survey_tla)

    # Filter by field period
    response_query = response_query.filter(FieldPeriod.stage == field_period)

    return response_query


def gather_management_info_spec(instrument_id):
    # Given an instrument_id, returns a dictionary with the mi_spec (management_info) for that
    # instrument_id

    management_info = db.session.query(Instrument.MI_spec) \
        .filter(Instrument.id == instrument_id).first()

    # Dictionary with management information specification
    management_info = ast.literal_eval(management_info.MI_spec)
    return management_info


def map_to_management_info(management_info_query):
    case_list = management_info_query.all()

    # Create dictionary with management information requirements, i.e. output fields required for a given instrument
    if len(case_list) != 0:
        management_info_spec = gather_management_info_spec(case_list[0].Case.instrument_id)
    else:
        return

    management_info_out = {}

    for i, val in enumerate(case_list):

        case_table = case_list[i]
        serial_number = case_table.Case.serial_number
        case_response_block = case_table.CaseResponse

        sample = db.session.query(Sample) \
            .filter(Sample.id == case_table.Case.sample_id).first()

        # Default output for cases (following CMS
        # https://collaborate2.ons.gov.uk/confluence/display/QSS/Blaise+5+Management+Information+%28MI%29+Extract )
        management_info_out[serial_number] = {"QUOTA": sample.quota,
                                              "ADDRESS": sample.addressno,
                                              "HHOLD": case_table.Case.household,
                                              "INTNUM": case_table.Case.interviewer_id,
                                              "HOUT": case_table.Case.outcome_code}

        if case_response_block is None:
            management_info_out[serial_number].update({key: 'NULL' for key in management_info_spec.keys()})
        else:
            # Dictionary with all response_data for a given case
            case_response_dict = ast.literal_eval(case_response_block.response_data)

            # Find keys in case_response_dict which match values in management_info
            # Create {management_info key : case_response_dict value}
            management_info_out[serial_number].update({key: case_response_dict[management_info_spec[key]]
                                                       for key in management_info_spec.keys()})

    return management_info_out
