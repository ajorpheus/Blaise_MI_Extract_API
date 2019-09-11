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
        .outerjoin(Sample, Case.sample_id == Sample.id) \
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

    Example output:
        If a single case were found, the output would be:
        {"1234": {"QUOTA":"1", "ADDRESS":"2", "HHOLD":"1", "INTNUM": "123"}}
        where 1234 is the primary_key.
    """

    case_list = build_query_for_case_list(survey_tla, field_period).all()

    # Create dictionary with management information requirements, i.e. output fields required for a given instrument
    if len(case_list) != 0:
        management_info_spec = gather_management_info_spec(case_list[0].Case.instrument_id, db)
    else:
        return None

    management_info_out = {}

    for row in case_list:

        primary_key = row.Case.primary_key
        case_response_block = row.CaseResponse

        # Default output for cases (following CMS
        # https://collaborate2.ons.gov.uk/confluence/display/QSS/Blaise+5+Management+Information+%28MI%29+Extract )
        management_info_out[primary_key] = {"QUOTA": row.Case.quota,
                                            "ADDRESS": row.Case.address,
                                            "HHOLD": row.Case.hhold,
                                            "INTNUM": row.Case.interviewer_id}

        if case_response_block is None or case_response_block.response_data is None:
            management_info_out[primary_key].update({key: None for key in management_info_spec.keys()})
        else:
            # Dictionary with all response_data for a given case
            case_response_dict = json.loads(case_response_block.response_data)

            # Find keys in case_response_dict which match values in management_info
            # Create {management_info key : case_response_dict value}
            management_info_out[primary_key].update({key: case_response_dict[management_info_spec[key]]
                                                     for key in management_info_spec.keys()})

    return json.dumps(management_info_out)
