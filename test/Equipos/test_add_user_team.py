import pytest
from src.espocrm_api.endpoint_teams import EndpointTeams
from src.payloads.payloads_team import PayloadTeam
from src.resources.authentifications.authentification import Auth
from src.espocrm_api.api_request import EspocrmRequest
from src.assertions.schema_assertions import AssertionSchemas
from src.assertions.status_code_assertions import AssertionStatusCode
from src.assertions.teams_assertions import AssertionTeams
from src.resources.call_request.team import TeamCall


@pytest.mark.smoke
def test_add_team_user_exists(setup_team_add_user):
    headers, team, user1, user2 = setup_team_add_user
    payload = PayloadTeam().build_payload_add_user_team([user1['id'],user2['id']])
    response = EspocrmRequest().post(EndpointTeams.add_users(team['id']), headers, payload)
    team_users = TeamCall().view_users(headers, team['id'])
    AssertionStatusCode().assert_status_code_200(response)
    AssertionTeams().assert_response_true(response)
    AssertionTeams().assert_field_list_no_empty(team_users)
    AssertionTeams().assert_response_true(response)
    AssertionTeams().assert_users_in_team([user1['id']], team_users)
