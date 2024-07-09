import pytest
from src.resources.authentifications.authentification import Auth
from src.espocrm_api.endpoint import Endpoint
from src.payloads.payloads_team import PayloadTeam
from src.espocrm_api.api_request import EspocrmRequest
from src.assertions.status_code_assertions import AssertionStatusCode
from src.assertions.schema_assertions import AssertionSchemas

import json


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.testEddy
def test_delete_with_empty_id_list(get_headers):  # 83
    headers = Auth().get_valid_user_headers(get_headers)
    payload = PayloadTeam().build_payload_delete_multiple_team(entityType="Team", action="delete", params=None,
                                                               idle=None)
    AssertionSchemas().assert_team_delete_multiple_team_schema_payload_file(payload)
    response = EspocrmRequest().post(Endpoint.massAction(), headers, payload)
    AssertionStatusCode().assert_status_code_500(response)


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.testEddy
def test_delete_nonexistent_team(get_headers):  # 84
    headers = Auth().get_valid_user_headers(get_headers)
    payload = PayloadTeam().build_payload_delete_multiple_team(entityType="Team", action="delete",
                                                               params=["no_existente"], idle=False)
    AssertionSchemas().assert_team_delete_multiple_team_schema_payload_file(payload)
    response = EspocrmRequest().delete(Endpoint.massAction(), headers, payload)
    AssertionStatusCode().assert_status_code_405(response)


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.smoke
@pytest.mark.testEddy
def test_delete_team_correctly(setup_team_delete_multiple_one_team):  # 80
    headers, team, team2 = setup_team_delete_multiple_one_team
    payload = PayloadTeam().build_payload_delete_multiple_team(entityType="Team", action="delete", params=[team['id']],
                                                               idle=False)
    AssertionSchemas().assert_team_delete_multiple_team_schema_payload_file(payload)
    response = EspocrmRequest().post(Endpoint.massAction(), headers, payload)
    AssertionStatusCode().assert_status_code_200(response)


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.testEddy
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_delete_team_with_nonexistent_id(get_headers):  # 85
    headers = Auth().get_valid_user_headers(get_headers)
    payload = PayloadTeam().build_payload_delete_multiple_team(entityType="Team", action="delete", params=["invalid"],
                                                               idle=False)
    AssertionSchemas().assert_team_delete_multiple_team_schema_payload_file(payload)
    response = EspocrmRequest().post(Endpoint.massAction(), headers, payload)
    AssertionStatusCode().assert_status_code_404(response)  # 404 eso deberia ser


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.testEddy
def test_delete_team_with_incorrect_action(setup_team_delete_multiple_one_team):  # 88
    headers, team, team2 = setup_team_delete_multiple_one_team
    payload = PayloadTeam().build_payload_delete_multiple_team(entityType="Team", action="update", params=[team['id']],
                                                               idle=False)
    AssertionSchemas().assert_team_delete_multiple_team_schema_payload_file(payload)
    response = EspocrmRequest().delete(Endpoint.massAction(), headers, payload)
    AssertionStatusCode().assert_status_code_405(response)


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.testEddy
def test_delete_team_with_incorrect_entity_type(setup_team_delete_multiple_one_team):  # 87
    headers, team, team2 = setup_team_delete_multiple_one_team
    payload = PayloadTeam().build_payload_delete_multiple_team(entityType="User", action="delete", params=[team['id']],
                                                               idle=False)
    AssertionSchemas().assert_team_delete_multiple_team_schema_payload_file(payload)
    response = EspocrmRequest().delete(Endpoint.massAction(), headers, payload)
    AssertionStatusCode().assert_status_code_405(response)


# @pytest.mark.regression
# @pytest.mark.functional
# @pytest.mark.smoke
# @pytest.mark.testEddy
# def test_delete_team_response_content(setup_team_delete_multiple_one_team):  #81  Incoherencia
#     headers, team, team2 = setup_team_delete_multiple_one_team
#     payload = PayloadTeam().build_payload_delete_multiple_team(entityType="Team", action="delete",params=[team['id']], idle=False)
#     AssertionSchemas().assert_team_delete_multiple_team_schema_payload_file(payload)
#     response = EspocrmRequest().post(Endpoint.massAction(), headers, payload)
#     AssertionStatusCode().assert_status_code_200(response)
#     assert response.json() == {"count": 1, "ids": [team['id']]}

@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.smoke
@pytest.mark.testEddy
def test_delete_team_check_ids_in_response(setup_team_delete_multiple_team):  # 82   BUG
    headers, team, team2 = setup_team_delete_multiple_team
    payload = PayloadTeam().build_payload_delete_multiple_team(entityType="Team", action="delete",
                                                               params=[team['id'], team2['id']], idle=False)
    AssertionSchemas().assert_team_delete_multiple_team_schema_payload_file(payload)
    response = EspocrmRequest().post(Endpoint.massAction(), headers, payload)
    AssertionStatusCode().assert_status_code_200(response)
    assert all(team_id in response.json().get("ids", []) for team_id in [team['id'], team2['id']])
