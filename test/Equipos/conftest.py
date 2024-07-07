import pytest
from src.resources.authentifications.authentification import Auth
from src.payloads.payloads_team import PayloadTeam
from src.payloads.payloads_user import PayloadUser
from src.resources.call_request.team import TeamCall
from src.resources.call_request.user import UserCall


@pytest.fixture(scope="module")
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


@pytest.fixture(scope="module")
def setup_create_user(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    payload_user_1 = PayloadUser().build_payload_add_user(userName="charles", salutationName="Mrs.",
                                                          firstName="Charles",
                                                          lastName="James")
    user = UserCall().create(headers, payload_user_1)
    yield user
