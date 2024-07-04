import pytest
from src.resources.authentifications.authentification import Auth
from src.espocrm_api.endpoint_teams import EndpointTeams
from src.espocrm_api.api_request import EspocrmRequest
from src.assertions.status_code_assertions import AssertionStatusCode
from src.assertions.schema_assertions import AssertionSchemas


@pytest.mark.regression
@pytest.mark.functional
def test_view_team_additional_headers(get_headers):  # 52
    additional_headers = {'header_extra': 'value_extra'}
    headers = Auth().get_valid_user_headers(get_headers, additional_headers)
    response = EspocrmRequest().get(EndpointTeams.view(), headers)
    AssertionStatusCode().assert_status_code_200(response)


@pytest.mark.regression
@pytest.mark.functional
def test_view_team_incorrect_http_method(get_headers):  # 51
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().post(EndpointTeams.view(), headers, payload=None)
    AssertionStatusCode().assert_status_code_405(response)


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.smoke
def test_view_team_correct(get_headers):  # 46
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams.view(), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_team_view_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_view_team_incorrect_authorization(get_headers):  # 48
    headers = Auth().get_invalid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams.view(), headers)
    AssertionStatusCode().assert_status_code_401(response)


@pytest.mark.regression
@pytest.mark.functional
def test_view_team_without_authorization(get_headers):  # 47
    headers = Auth().get_empty_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams.view(), headers)
    AssertionStatusCode().assert_status_code_401(response)


@pytest.mark.regression
@pytest.mark.functional
def test_view_team_id_not_exists(get_headers):  # 49
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams.view(team_id="id_no_existente"), headers)
    AssertionStatusCode().assert_status_code_404(response)


@pytest.mark.regression
@pytest.mark.functional
def test_view_team_id_incorrect_format(get_headers):  #
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams.view(team_id="formatoIncorrecto"), headers)
    AssertionStatusCode().assert_status_code_404(response)
