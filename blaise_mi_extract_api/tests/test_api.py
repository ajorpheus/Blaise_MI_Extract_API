import pytest


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


