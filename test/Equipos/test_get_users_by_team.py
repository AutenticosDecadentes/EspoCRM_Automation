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
def test_data_default(setup_add_user_team):
    headers, team = setup_add_user_team
    response = EspocrmRequest().get(EndpointTeams.team_users(team_id=team['id']), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_teams_users_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_max_size0(setup_add_user_team):
    headers, team = setup_add_user_team
    response = EspocrmRequest().get(EndpointTeams.team_users(team_id=team['id'], maxSize=0), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_teams_users_schema_file(response.json())



@pytest.mark.regression
@pytest.mark.functional
def test_max_height_greater_than_200(setup_add_user_team):
    headers, team = setup_add_user_team
    response = EspocrmRequest().get(EndpointTeams.team_users(team_id=team['id'], maxSize=201), headers)
    AssertionStatusCode().assert_status_code_403(response)
    AssertionTeams().assert_response_empty(response.text)


@pytest.mark.regression
@pytest.mark.functional
def test_max_height_less_than_200(setup_add_user_team):
    headers, team = setup_add_user_team
    response = EspocrmRequest().get(EndpointTeams.team_users(team_id=team['id'], maxSize=195), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_teams_users_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_max_size_negative(setup_add_user_team):
    headers, team = setup_add_user_team
    response = EspocrmRequest().get(EndpointTeams.team_users(team_id=team['id'], maxSize=-15), headers)
    AssertionStatusCode().assert_status_code_400(response)
    AssertionTeams().assert_response_empty(response.text)


@pytest.mark.regression
@pytest.mark.functional
def test_max_size_string(setup_add_user_team):
    headers, team = setup_add_user_team
    response = EspocrmRequest().get(EndpointTeams.team_users(team_id=team['id'], maxSize="hola"), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_teams_users_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.smoke
def test_list_teams_users_invalid_authentication(get_headers, setup_add_user_team):
    valid_headers, team = setup_add_user_team
    headers = Auth().get_invalid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams.team_users(team_id=team['id']), headers)
    AssertionStatusCode().assert_status_code_401(response)
    AssertionTeams().assert_response_empty(response.text)


@pytest.mark.regression
@pytest.mark.functional
def test_list_teams_users_order_asc(setup_add_user_team):
    headers, team = setup_add_user_team
    response = EspocrmRequest().get(EndpointTeams.team_users(team_id=team['id'], order='asc'), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_teams_users_schema_file(response.json())
    AssertionTeams().assert_check_order_asc(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_list_teams_users_order_desc(setup_add_user_team):
    headers, team = setup_add_user_team
    response = EspocrmRequest().get(EndpointTeams.team_users(team_id=team['id'], order='desc'), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_teams_users_schema_file(response.json())
    AssertionTeams().assert_check_order_desc(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_list_teams_users_orderby_empty(setup_add_user_team):
    headers, team = setup_add_user_team
    response = EspocrmRequest().get(EndpointTeams.team_users(team_id=team['id'], orderBy=''), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_teams_users_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_list_teams_users_orderby_null(setup_add_user_team):
    headers, team = setup_add_user_team
    response = EspocrmRequest().get(EndpointTeams.team_users(team_id=team['id'], orderBy="null"), headers)
    AssertionStatusCode().assert_status_code_400(response)
    try:
        AssertionTeams().assert_empty_field_list(response.json())
    except ValueError:
        AssertionTeams().assert_response_empty(response.text)


@pytest.mark.regression
@pytest.mark.functional
def test_max_offset0(setup_add_user_team):
    headers, team = setup_add_user_team
    response = EspocrmRequest().get(EndpointTeams.team_users(team_id=team['id'], offset=0), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_teams_users_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_offset_height_less_than_200(setup_add_user_team):
    headers, team = setup_add_user_team
    response = EspocrmRequest().get(EndpointTeams.team_users(team_id=team['id'], offset=195), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_teams_users_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_offset_negative(setup_add_user_team):
    headers, team = setup_add_user_team
    response = EspocrmRequest().get(EndpointTeams.team_users(team_id=team['id'], offset=-15), headers)
    AssertionStatusCode().assert_status_code_400(response)
    AssertionTeams().assert_response_empty(response.text)


@pytest.mark.regression
@pytest.mark.functional
def test_offset_string(setup_add_user_team):
    headers, team = setup_add_user_team
    response = EspocrmRequest().get(EndpointTeams.team_users(team_id=team['id'], offset="hola"), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_teams_users_schema_file(response.json())
