import pytest
import json


@pytest.mark.usefixtures('client', 'add_response_to_db')
class TestURLs:

    def test_unauthorised_api_key(self, client):
        url_data = client.get('/management_information/OPN/2001?api_key=123')
        assert url_data.status_code == 401

    def test_missing_api_key(self, client):
        url_data = client.get('/management_information/OPN/2001')
        assert url_data.status_code == 401

    def test_nonexistent_tla_survey(self, client):
        url_data = client.get('/management_information/cat/2001?api_key=123456')
        assert url_data.status_code == 404

    def test_nonexistent_time_period(self, client):
        url_data = client.get('/management_information/cat/2001?api_key=123456')
        assert url_data.status_code == 404

    def test_output_from_undefined_mi_spec(self, client):
        url_data = client.get('/management_information/OPN/2001?api_key=123456')
        data = json.loads(url_data.data)
        assert data['1234']['QUOTA'] == '7'
        assert data['1234']['ADDRESS'] is None
        assert data['1234']['HHOLD'] == 2
        assert data['1234']['INTNUM'] == ''

    @pytest.mark.parametrize('add_response_to_db', [['{"serial_number": "QID.Case_ID"}']], indirect=True)
    def test_output_fields_correct(self, client, add_response_to_db):
        url_data = client.get('/management_information/OPN/2001?api_key=123456')
        data = json.loads(url_data.data)
        assert data['1234']['QUOTA'] == '7'
        assert data['1234']['ADDRESS'] is None
        assert data['1234']['HHOLD'] == 2
        assert data['1234']['INTNUM'] == ''
        assert data['1234']['serial_number'] is None


