import json

from blaise_mi_extract_api.models import db
from blaise_mi_extract_api.models import CaseResponse, Survey, Case, FieldPeriod, Instrument, Sample


def build_query_for_case_list(survey_tla, field_period, phase="Live"):
    """
    Build a query based on the survey_tla and field_period provided. The query will include data for which the
    case_response is empty

    Parameters:
        survey_tla -- Three letter acronym for a survey e.g. 'OPN'
        field_period -- Format yymm e.g. '1901'
        phase -- e.g. 'Live', 'Training' (default: 'Live')
    Returns:
        response_query -- A BaseQuery object

    Example usage:
    - The following call will return all rows with 'Live' cases matching OPN2001
        case_list = build_query_for_case_list('OPN', '2001').all()
    """

    # Collect all cases (with or without response) with their survey three letter acronym (tla) and field period and
    # filter by survey_tla, field_period and phase
    response_query = db.session.query(Case, CaseResponse) \
        .outerjoin(CaseResponse, Case.id == CaseResponse.case_id) \
        .join(Survey, Case.survey_id == Survey.id) \
        .join(FieldPeriod, Case.field_period_id == FieldPeriod.id) \
        .filter(Survey.tla == survey_tla) \
        .filter(FieldPeriod.stage == field_period) \
        .filter(Case.phase == phase)

    return response_query


def gather_management_info_spec(instrument_id, database=None):
    """
    Queries a database to obtain the Management Information specification associated with an instrument.

    Parameters:
        instrument_id -- the id for an instrument
        database -- Database containing the instrument
    Returns:
        management_info -- Dictionary containing the management information specification. If the database is not
        specified, it returns an empty dictionary

    """
    if database is None:
        management_info = {}
        return management_info

    management_info = database.session.query(Instrument.MI_spec) \
        .filter(Instrument.id == instrument_id).first()

    # Dictionary with management information specification
    if not management_info.MI_spec:
        management_info = {}
    else:
        management_info = json.loads(management_info.MI_spec)

    return management_info


def map_to_management_info(survey_tla, field_period):
    """
    Obtains the default Management Information for each case, as well as any other requested by MI_spec (
    gather_management_info_spec()). Each case is identified by a primary_key.

    Parameters:
        survey_tla -- Three letter acronym for a survey e.g. 'OPN'
        field_period -- Format yymm e.g. '1901'
    Returns:
        json.dumps(management_info_out) -- JSON formatted str containing the management information for each case

    """
    # get a list of cases
    case_list = build_query_for_case_list(survey_tla, field_period).all()

    if len(case_list) == 0:
        return None

    # Create dictionary with management information requirements, i.e. output fields required for a given instrument
    management_info_spec = gather_management_info_spec(case_list[0].Case.instrument_id, db)

    management_info_out = []

    for row in case_list:
        # Default output for cases (following CMS
        # https://collaborate2.ons.gov.uk/confluence/display/QSS/Blaise+5+Management+Information+%28MI%29+Extract )
        management_info_record = {"tla": survey_tla,
                                  "field_period": field_period,
                                  "primary_key": row.Case.primary_key}

        if row.CaseResponse and row.CaseResponse.response_data:
            case_response_dict = json.loads(row.CaseResponse.response_data)
        else:
            case_response_dict = dict()

        # Find keys in case_response_dict which match values in management_info
        management_info_record.update({key: case_response_dict.get(management_info_spec[key], None)
                                       for key in management_info_spec.keys()})

        management_info_out.append(management_info_record)

    return json.dumps(management_info_out)
