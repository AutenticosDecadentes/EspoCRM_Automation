import pytest, random, string
from src.espocrm_api.endpoint_teams import EndpointTeams
from src.payloads.payloads_team import PayloadTeam
from src.resources.authentifications.authentification import Auth
from src.espocrm_api.api_request import EspocrmRequest
from src.assertions.schema_assertions import AssertionSchemas
from src.assertions.status_code_assertions import AssertionStatusCode
from src.assertions.teams_assertions import AssertionTeams
from src.resources.call_request.team import TeamCall
from src.resources.call_request.user import UserCall


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.functional
def test_add_team_user_exists(setup_team_add_user):
    headers, team, user1, user2 = setup_team_add_user
    payload = PayloadTeam().build_payload_add_user_team([user1['id']])
    AssertionSchemas().assert_team_add_user_schema_payload_file(payload)
    response = EspocrmRequest().post(EndpointTeams.add_users(team['id']), headers, payload)
    team_users = TeamCall().view_users(headers, team['id'])
    AssertionStatusCode().assert_status_code_200(response)
    AssertionTeams().assert_response_true(response)
    AssertionTeams().assert_field_list_no_empty(team_users)
    AssertionTeams().assert_users_in_team([user1['id']], team_users)


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.smoke
def test_add_team_multi_users(setup_team_add_user):
    headers, team, user1, user2 = setup_team_add_user
    payload = PayloadTeam().build_payload_add_user_team([user1['id'], user2['id']])
    AssertionSchemas().assert_team_add_user_schema_payload_file(payload)
    response = EspocrmRequest().post(EndpointTeams.add_users(team['id']), headers, payload)
    team_users = TeamCall().view_users(headers, team['id'])
    AssertionStatusCode().assert_status_code_200(response)
    AssertionTeams().assert_response_true(response)
    AssertionTeams().assert_field_list_no_empty(team_users)
    AssertionTeams().assert_users_in_team([user1['id'], user2['id']], team_users)


@pytest.mark.regression
@pytest.mark.functional
def test_add_team_user_invalid(setup_team_add_user):
    headers, team, user1, user2 = setup_team_add_user
    user_id_invalid = ''.join(random.choices(string.ascii_letters + string.digits, k=17))
    payload = PayloadTeam().build_payload_add_user_team([user_id_invalid])
    AssertionSchemas().assert_team_add_user_schema_payload_file(payload)
    response = EspocrmRequest().post(EndpointTeams.add_users(team['id']), headers, payload)
    team_users = TeamCall().view_users(headers, team['id'])
    AssertionStatusCode().assert_status_code_404(response)
    AssertionTeams().assert_response_empty(response.text)
    AssertionTeams().assert_user_not_in_team([user_id_invalid], team_users)


@pytest.mark.regression
@pytest.mark.functional
def test_add_team_user_exist(setup_team_add_user):
    headers, team, user1, user2 = setup_team_add_user
    payload = PayloadTeam().build_payload_add_user_team([user1['id']])
    AssertionSchemas().assert_team_add_user_schema_payload_file(payload)
    response = EspocrmRequest().post(EndpointTeams.add_users(team['id']), headers, payload)
    team_users = TeamCall().view_users(headers, team['id'])
    AssertionTeams().assert_users_in_team([user1['id']], team_users)
    response = EspocrmRequest().post(EndpointTeams.add_users(team['id']), headers, payload)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionTeams().assert_response_true(response)
    AssertionTeams().assert_field_list_no_empty(team_users)
    AssertionTeams().assert_users_in_team([user1['id']], team_users)


@pytest.mark.regression
@pytest.mark.functional
def test_add_team_not_exists(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    team_id_invalid = ''.join(random.choices(string.ascii_letters + string.digits, k=17))
    user_id_invalid = ''.join(random.choices(string.ascii_letters + string.digits, k=17))
    payload = PayloadTeam().build_payload_add_user_team([user_id_invalid])
    AssertionSchemas().assert_team_add_user_schema_payload_file(payload)
    response = EspocrmRequest().post(EndpointTeams.add_users(team_id_invalid), headers, payload)
    AssertionStatusCode().assert_status_code_404(response)
    AssertionTeams().assert_response_empty(response.text)


@pytest.mark.regression
@pytest.mark.functional
def test_add_user_empty_payload(setup_team_add_user):
    headers, team, user1, user2 = setup_team_add_user
    payload = PayloadTeam().build_payload_add_user_team("")
    response = EspocrmRequest().post(EndpointTeams.add_users(team['id']), headers, payload)
    team_users = TeamCall().view_users(headers, team['id'])
    AssertionStatusCode().assert_status_code_200(response)
    AssertionTeams().assert_response_false(response)


@pytest.mark.regression
@pytest.mark.functional
def test_add_deleted_user(setup_team_add_user, setup_create_user_team):
    headers, team, user1, user2 = setup_team_add_user
    user3 = setup_create_user_team
    UserCall().delete(headers, user3['id'])
    payload = PayloadTeam().build_payload_add_user_team([user3['id']])
    response = EspocrmRequest().post(EndpointTeams.add_users(team['id']), headers, payload)
    AssertionStatusCode().assert_status_code_404(response)
    AssertionTeams().assert_response_empty(response.text)