import pytest
from src.resources.authentifications.authentification import Auth
from src.espocrm_api.api_request import EspocrmRequest
from src.espocrm_api.endpoint_teams import EndpointTeams
from src.assertions.status_code_assertions import AssertionStatusCode
from src.assertions.schema_assertions import AssertionSchemas
from src.assertions.teams_assertions import AssertionTeams


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.smoke
def test_data_default(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams.team_users(), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_teams_users_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_max_size0(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams().team_users(maxSize=0), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_teams_users_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_max_height_greater_than_200(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams().team_users(maxSize=201), headers)
    AssertionStatusCode().assert_status_code_403(response)
    AssertionTeams().assert_response_empty(response.text)


@pytest.mark.regression
@pytest.mark.functional
def test_max_height_less_than_200(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams().team_users(maxSize=195), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_teams_users_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_max_size_negative(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams().team_users(maxSize=-15), headers)
    AssertionStatusCode().assert_status_code_500(response)
    AssertionTeams().assert_response_empty(response.text)


@pytest.mark.regression
@pytest.mark.functional
def test_max_size_string(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams().team_users(maxSize="hola"), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_teams_users_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.smoke
def test_list_teams_users_invalid_authentication(get_headers):
    headers = Auth().get_invalid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams().team_users(), headers)
    AssertionStatusCode().assert_status_code_401(response)
    AssertionTeams().assert_response_empty(response.text)


@pytest.mark.regression
@pytest.mark.functional
def test_list_teams_users_order_asc(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams().team_users(order='asc'), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_teams_users_schema_file(response.json())
    AssertionTeams().assert_check_order_asc(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_list_teams_users_order_desc(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams().team_users(order='desc'), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_teams_users_schema_file(response.json())
    AssertionTeams().assert_check_order_desc(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_list_teams_users_orderby_empty(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams().team_users(orderBy=''), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_teams_users_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_list_teams_users_orderby_null(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams().team_users(orderBy="null"), headers)
    AssertionStatusCode().assert_status_code_400(response)
    try:
        AssertionTeams().assert_empty_field_list(response.json())
    except ValueError:
        AssertionTeams().assert_response_empty(response.text)


@pytest.mark.regression
@pytest.mark.functional
def test_max_offset0(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams().team_users(offset=0), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_teams_users_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_offset_height_less_than_200(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams().team_users(offset=195), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_teams_users_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_offset_negative(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams().team_users(offset=-15), headers)
    AssertionStatusCode().assert_status_code_500(response)
    AssertionTeams().assert_response_empty(response.text)


@pytest.mark.regression
@pytest.mark.functional
def test_offset_string(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams().team_users(offset="hola"), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_teams_users_schema_file(response.json())
