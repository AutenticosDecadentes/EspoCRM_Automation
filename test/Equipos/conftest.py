import pytest

from src.espocrm_api.api_request import EspocrmRequest
from src.espocrm_api.endpoint_teams import EndpointTeams
from src.resources.authentifications.authentification import Auth
from src.payloads.payloads_team import PayloadTeam
from src.payloads.payloads_user import PayloadUser
from src.resources.call_request.team import TeamCall
from src.resources.call_request.user import UserCall


@pytest.fixture(scope="function")
def setup_team_add_user(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    payload_team = PayloadTeam().build_payload_add_team("Team Golden")
    payload_user_1 = PayloadUser().build_payload_add_user(userName="darwin", salutationName="Mrs.", firstName="Darwin",
                                                          lastName="Garcia")
    payload_user_2 = PayloadUser().build_payload_add_user(userName="victorino", salutationName="Mrs.",
                                                          firstName="Victorino",
                                                          lastName="Perez")
    team = TeamCall().create(headers, payload_team)
    user1 = UserCall().create(headers, payload_user_1)
    user2 = UserCall().create(headers, payload_user_2)
    yield headers, team, user1, user2

    TeamCall().delete(headers, team['id'])
    UserCall().delete(headers, user1['id'])
    UserCall().delete(headers, user2['id'])


@pytest.fixture(scope="function")
def setup_team_unlink_user(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    payload_team = PayloadTeam().build_payload_add_team("Team Red")
    payload_user_1 = PayloadUser().build_payload_add_user(userName="javier", salutationName="Mrs.", firstName="Javi",
                                                          lastName="Garcia")

    payload_user_2 = PayloadUser().build_payload_add_user(userName="ronald", salutationName="Mrs.",
                                                          firstName="Ronald",
                                                          lastName="Perez")
    team = TeamCall().create(headers, payload_team)
    user1 = UserCall().create(headers, payload_user_1)
    user2 = UserCall().create(headers, payload_user_2)
    payload = PayloadTeam().build_payload_add_user_team([user1['id'], user2['id']])
    TeamCall().add_user(headers, payload, team['id'])
    yield headers, team, user1, user2

    TeamCall().delete(headers, team['id'])
    UserCall().delete(headers, user1['id'])
    UserCall().delete(headers, user2['id'])


@pytest.fixture(scope="function")
def setup_create_user_team(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    payload_user_1 = PayloadUser().build_payload_add_user(userName="charles", salutationName="Mrs.",
                                                          firstName="Charles",
                                                          lastName="James")
    user = UserCall().create(headers, payload_user_1)
    yield user


@pytest.fixture(scope="function")
def setup_add_team(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    created_teams = []
    yield headers, created_teams

    for team in created_teams:
        TeamCall().delete(headers, team['id'])


@pytest.fixture(scope="function")
def setup_team_delete_multiple_team(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    payload_team = PayloadTeam().build_payload_add_team("Team Golden")
    payload_team2 = PayloadTeam().build_payload_add_team("Team Golden")
    team = TeamCall().create(headers, payload_team)
    team2 = TeamCall().create(headers, payload_team2)
    yield headers, team, team2


@pytest.fixture(scope="function")
def setup_team_delete_multiple_one_team(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    payload_team = PayloadTeam().build_payload_add_team("Team Golden")
    payload_team2 = PayloadTeam().build_payload_add_team("Team Golden")
    team = TeamCall().create(headers, payload_team)
    team2 = TeamCall().create(headers, payload_team2)
    yield headers, team, team2
    TeamCall().delete(headers, team2['id'])


@pytest.fixture(scope="function")
def setup_team_delete_team(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    payload_team = PayloadTeam().build_payload_add_team("Team Golden")
    team = TeamCall().create(headers, payload_team)
    yield headers, team

@pytest.fixture(scope="function")
def setup_team_view_team(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    payload_team = PayloadTeam().build_payload_add_team("Team Golden")
    team = TeamCall().create(headers, payload_team)
    yield headers, team
    TeamCall().delete(headers, team['id'])

@pytest.fixture(scope="function")
def setup_team_delete_team_invalid(get_headers):
    headers = Auth().get_invalid_user_headers(get_headers)
    payload_team = PayloadTeam().build_payload_add_team("Team Golden")
    team = TeamCall().create(headers, payload_team)
    yield headers, team

@pytest.fixture(scope="function")
def setup_edit_team(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    payload_team = PayloadTeam().build_payload_add_team("probando_ando")
    team = TeamCall().create(headers, payload_team)
    yield headers, team
    TeamCall().delete(headers, team['id'])


@pytest.fixture(scope="function")
def setup_add_user_team(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    payload_team = PayloadTeam().build_payload_add_team("Team prueba")
    payload_user_1 = PayloadUser().build_payload_add_user(userName="orlando001", salutationName="Mrs.", firstName="mike",
                                                          lastName="wazouski")
    payload_user_2 = PayloadUser().build_payload_add_user(userName="orlando002", salutationName="Mrs.",
                                                          firstName="andres",
                                                          lastName="torrez")
    payload_user_3 = PayloadUser().build_payload_add_user(userName="orlando003", salutationName="Mrs.",
                                                          firstName="andres",
                                                          lastName="torrez")
    payload_user_4 = PayloadUser().build_payload_add_user(userName="orlando004", salutationName="Mrs.",
                                                          firstName="andres",
                                                          lastName="torrez")
    team = TeamCall().create(headers, payload_team)
    user_1 = UserCall().create(headers, payload_user_1)
    user_2 = UserCall().create(headers, payload_user_2)
    user_3 = UserCall().create(headers, payload_user_3)
    user_4 = UserCall().create(headers, payload_user_4)
    payload_add_user1 = PayloadTeam().build_payload_add_user_team([user_1['id']])
    payload_add_user2 = PayloadTeam().build_payload_add_user_team([user_2['id']])
    payload_add_user3 = PayloadTeam().build_payload_add_user_team([user_3['id']])
    payload_add_user4 = PayloadTeam().build_payload_add_user_team([user_4['id']])
    EspocrmRequest().post(EndpointTeams.add_users(team['id']), headers, payload_add_user1)
    EspocrmRequest().post(EndpointTeams.add_users(team['id']), headers, payload_add_user2)
    EspocrmRequest().post(EndpointTeams.add_users(team['id']), headers, payload_add_user3)
    EspocrmRequest().post(EndpointTeams.add_users(team['id']), headers, payload_add_user4)
    yield headers, team

    TeamCall().delete(headers, team['id'])
    UserCall().delete(headers, user_1['id'])
    UserCall().delete(headers, user_2['id'])
    UserCall().delete(headers, user_3['id'])
    UserCall().delete(headers, user_4['id'])