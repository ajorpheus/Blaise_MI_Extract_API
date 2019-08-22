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
def add_response_to_db():
    # app = create_app('settings.TestConfig')

    api_key = ApiKey()
    api_key.api_key = '123456'
    db.session.add(api_key)

    survey = Survey()
    survey.id = 1
    survey.tla = 'OPN'
    db.session.add(survey)

    instrument = Instrument()
    instrument.id = 1
    instrument.MI_spec = '{"Name": "Person.FirstName"}'
    instrument.survey_id = survey.id
    instrument.field_period_id = 1
    db.session.add(instrument)

    case = Case()
    case.id = 1
    case.survey_id = survey.id
    case.instrument_id = instrument.id
    case.serial_number = '1234'
    case.field_period_id = 1
    case.sample_id = 5
    case.household = ''
    case.interviewer_id = ''
    case.outcome_code = 10
    case.phase = 'Live'
    db.session.add(case)

    case_response = CaseResponse()
    case_response.case_id = case.id
    db.session.add(case_response)

    field_period = FieldPeriod()
    field_period.id = case.field_period_id
    field_period.stage = '2001'
    db.session.add(field_period)

    sample = Sample()
    sample.id = case.sample_id
    sample.quota = '7'
    sample.addresno = ''
    db.session.add(sample)

    db.session.commit()

    return
