import pytest
from src.resources.authentifications.authentification import Auth
from src.espocrm_api.endpoint_teams import EndpointTeams
from src.espocrm_api.api_request import EspocrmRequest
from src.assertions.status_code_assertions import AssertionStatusCode
from src.assertions.schema_assertions import AssertionSchemas

import json


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.smoke
@pytest.mark.testEddy2
def test_delete_non_existent_team(get_headers):  #168
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().delete(EndpointTeams.delete('NoExist'), headers)
    AssertionStatusCode().assert_status_code_404(response)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.testEddy2
def test_delete_valid_team(setup_team_delete_team):  #167
    headers, team = setup_team_delete_team
    response = EspocrmRequest().delete(EndpointTeams.delete(team['id']), headers)
    AssertionStatusCode().assert_status_code_200(response)


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.testEddy2
def test_delete_invalid_authorization(get_headers):  #176
    headers = Auth().get_invalid_user_headers(get_headers)
    response = EspocrmRequest().delete(EndpointTeams.delete('crack'), headers)
    AssertionStatusCode().assert_status_code_401(response)


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.testEddy2
def test_delete_missing_headers():  #178
    headers = {"accept": "/"}
    response = EspocrmRequest().delete(EndpointTeams.delete('crack'), headers)
    AssertionStatusCode().assert_status_code_401(response)


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.testEddy2
def test_delete_invalid_team_id(get_headers):  #173
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().delete(EndpointTeams.delete('invalidTeam'), headers)
    AssertionStatusCode().assert_status_code_404(response)


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.testEddy2
def test_delete_valid_team_no_auth_header(setup_team_delete_team):  #171
    headers, team = setup_team_delete_team
    headersInvalid = {"accept": "/"}
    response = EspocrmRequest().delete(EndpointTeams.delete(team['id']), headersInvalid)
    AssertionStatusCode().assert_status_code_401(response)  #Eliminar usuario creado


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.testEddy2
def test_delete_wrong_http_method(setup_team_delete_team):  #172
    headers, team = setup_team_delete_team
    response = EspocrmRequest().post(EndpointTeams.delete(team['id']), headers)
    AssertionStatusCode().assert_status_code_405(response)


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.testEddy2
def test_delete_no_team_id(get_headers):  #175
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().delete(EndpointTeams.delete(''), headers)
    AssertionStatusCode().assert_status_code_404(response)
