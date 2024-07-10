# import pytest, random, string
# from src.espocrm_api.endpoint_teams import EndpointTeams
# from src.payloads.payloads_team import PayloadTeam
# from src.resources.authentifications.authentification import Auth
# from src.espocrm_api.api_request import EspocrmRequest
# from src.assertions.schema_assertions import AssertionSchemas
# from src.assertions.status_code_assertions import AssertionStatusCode
# from src.assertions.teams_assertions import AssertionTeams
# from src.resources.call_request.team import TeamCall
# from src.resources.call_request.user import UserCall
#
#
# @pytest.mark.smoke
# @pytest.mark.regression
# @pytest.mark.functional
# def test_unlink_team_user_exists(setup_team_unlink_user):
#     headers, team, user1, user2 = setup_team_unlink_user
#     payload = PayloadTeam().build_payload_unlink_user_team(user1['id'])
#     AssertionSchemas().assert_team_unlink_user_schema_payload_file(payload)
#     response = EspocrmRequest().delete(EndpointTeams.delete_users(team['id']), headers, payload)
#     team_users = TeamCall().view_users(headers, team['id'])
#     AssertionStatusCode().assert_status_code_200(response)
#     AssertionTeams().assert_response_true(response)
#     AssertionTeams().assert_user_not_in_team([user1['id']], team_users)
#
#
# @pytest.mark.smoke
# @pytest.mark.regression
# @pytest.mark.functional
# def test_unlink_team_user_invalid_authentication(setup_team_unlink_user, get_headers):
#     headers, team, user1, user2 = setup_team_unlink_user
#     headers = Auth().get_invalid_user_headers(get_headers)
#     payload = PayloadTeam().build_payload_unlink_user_team(user1['id'])
#     AssertionSchemas().assert_team_unlink_user_schema_payload_file(payload)
#     response = EspocrmRequest().delete(EndpointTeams.delete_users(team['id']), headers, payload)
#     AssertionStatusCode().assert_status_code_401(response)
#     AssertionTeams().assert_response_empty(response.text)
#
#
# @pytest.mark.regression
# @pytest.mark.functional
# def test_unlink_team_not_exits(setup_team_unlink_user):
#     headers, team, user1, user2 = setup_team_unlink_user
#     team_id_invalid = ''.join(random.choices(string.ascii_letters + string.digits, k=17))
#     payload = PayloadTeam().build_payload_unlink_user_team(user1['id'])
#     AssertionSchemas().assert_team_unlink_user_schema_payload_file(payload)
#     response = EspocrmRequest().delete(EndpointTeams.delete_users(team_id_invalid), headers, payload)
#     AssertionStatusCode().assert_status_code_404(response)
#     AssertionTeams().assert_response_empty(response.text)
#
#
# @pytest.mark.regression
# @pytest.mark.functional
# def test_unlink_user_not_exits(setup_team_unlink_user):
#     headers, team, user1, user2 = setup_team_unlink_user
#     user_id_invalid = ''.join(random.choices(string.ascii_letters + string.digits, k=17))
#     payload = PayloadTeam().build_payload_unlink_user_team(user_id_invalid)
#     AssertionSchemas().assert_team_unlink_user_schema_payload_file(payload)
#     response = EspocrmRequest().delete(EndpointTeams.delete_users(team['id']), headers, payload)
#     AssertionStatusCode().assert_status_code_404(response)
#     AssertionTeams().assert_response_empty(response.text)
#
#
# @pytest.mark.regression
# @pytest.mark.functional
# @pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
# def test_unlink_user_exist_in_team(setup_team_unlink_user):
#     headers, team, user1, user2 = setup_team_unlink_user
#     payload = PayloadTeam().build_payload_unlink_user_team(user2['id'])
#     AssertionSchemas().assert_team_unlink_user_schema_payload_file(payload)
#     response = EspocrmRequest().delete(EndpointTeams.delete_users(team['id']), headers, payload)
#     team_users = TeamCall().view_users(headers, team['id'])
#     AssertionStatusCode().assert_status_code_404(response)
#     AssertionTeams().assert_response_false(response)
#     AssertionTeams().assert_user_not_in_team([user1['id']], team_users)
#
#
# @pytest.mark.regression
# @pytest.mark.functional
# def test_unlink_team_user_unauthorized(setup_team_unlink_user, get_headers):
#     headers, team, user1, user2 = setup_team_unlink_user
#     headers = Auth().get_unauthorized_teams_user_headers(get_headers)
#     payload = PayloadTeam().build_payload_unlink_user_team(user1['id'])
#     AssertionSchemas().assert_team_unlink_user_schema_payload_file(payload)
#     response = EspocrmRequest().delete(EndpointTeams.delete_users(team['id']), headers, payload)
#     AssertionStatusCode().assert_status_code_403(response)
#     AssertionTeams().assert_response_empty(response.text)
#
#
# @pytest.mark.regression
# @pytest.mark.functional
# def test_unlink_team_user_id_empty(setup_team_unlink_user):
#     headers, team, user1, user2 = setup_team_unlink_user
#     payload = PayloadTeam().build_payload_unlink_user_team("")
#     AssertionSchemas().assert_team_unlink_user_schema_payload_file(payload)
#     response = EspocrmRequest().delete(EndpointTeams.delete_users(team['id']), headers, payload)
#     AssertionStatusCode().assert_status_code_400(response)
#     AssertionTeams().assert_response_empty(response.text)
