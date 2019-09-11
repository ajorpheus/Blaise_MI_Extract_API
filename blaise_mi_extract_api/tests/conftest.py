import pytest
from blaise_mi_extract_api import create_app
from blaise_mi_extract_api.models import db
from blaise_mi_extract_api.models import CaseResponse, Survey, Case, FieldPeriod, Instrument, Sample, ApiKey


@pytest.fixture()
def client(request):
    app = create_app('settings.TestConfig')
    client = app.test_client()

    db.app = app
    try:
        db.create_all()
    except Exception as e:
        print(e)

    def teardown():
        db.session.remove()
        db.drop_all()

    request.addfinalizer(teardown)

    return client


@pytest.fixture()
def add_response_to_db(request):
    api_key = ApiKey()
    api_key.api_key = '123456'
    db.session.add(api_key)

    survey = Survey()
    survey.id = 1
    survey.tla = 'OPN'
    db.session.add(survey)

    instrument = Instrument()
    instrument.id = 1
    if hasattr(request, 'param'):
        instrument.MI_spec = request.param[0]
    else:
        instrument.MI_spec = ''
    instrument.survey_id = survey.id
    instrument.field_period_id = 1
    db.session.add(instrument)

    case = Case()
    case.id = 1
    case.survey_id = survey.id
    case.instrument_id = instrument.id
    case.primary_key = 1234
    case.field_period_id = 1
    case.sample_id = 5
    case.household = '2'
    case.interviewer_id = ''
    case.outcome_code = 10
    case.phase = 'Live'
    case.quota = '7'
    case.address = ''
    db.session.add(case)

    case_response = CaseResponse()
    case_response.case_id = case.id
    case_response.response_data = '{"qid.serial_number": "98765"}'
    db.session.add(case_response)

    field_period = FieldPeriod()
    field_period.id = case.field_period_id
    field_period.stage = '2001'
    db.session.add(field_period)

    sample = Sample()
    sample.id = case.sample_id
    db.session.add(sample)

    db.session.commit()

    return
