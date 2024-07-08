import pytest
from src.espocrm_api.endpoint_teams import EndpointTeams
from src.payloads.payloads_team import PayloadTeam
from src.espocrm_api.api_request import EspocrmRequest
from src.assertions.status_code_assertions import AssertionStatusCode
from src.assertions.schema_assertions import AssertionSchemas
from src.resources.authentifications.authentification import Auth


@pytest.mark.regression
@pytest.mark.functional
def test_add_team(setup_add_team):
    headers, created_teams = setup_add_team
    payload = PayloadTeam().build_payload_add_team(name="prueba-test1")
    response = EspocrmRequest().post(EndpointTeams.team(), headers, payload)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_add_team_schema_schema_file(response.json())
    created_team = response.json()
    created_teams.append(created_team)


@pytest.mark.regression
@pytest.mark.functional
def test_add_team_duplicate_name(setup_add_team):
    headers, created_teams = setup_add_team
    payload = PayloadTeam().build_payload_add_team(name="prueba-test1")
    response = EspocrmRequest().post(EndpointTeams.team(), headers, payload)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_add_team_schema_schema_file(response.json())
    created_team = response.json()
    created_teams.append(created_team)
    response1 = EspocrmRequest().post(EndpointTeams.team(), headers, payload)
    AssertionStatusCode().assert_status_code_409(response1)
    created_team = response1.json()
    created_teams.append(created_team)


@pytest.mark.regression
@pytest.mark.functional
def test_add_team_all_data(setup_add_team):
    headers, created_teams = setup_add_team
    payload = PayloadTeam().build_payload_add_team(name="prueba1111", rolesIds="66758f0575dbc3464", rolesNames="Prueba", layoutSetName="Layout 1", workingTimeCalendarName="Calendar", layoutSetId="6675949a021ad4859", workingTimeCalendarId="667594aa8582445d8")
    response = EspocrmRequest().post(EndpointTeams.team(), headers, payload)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_add_team_schema_schema_file(response.json())
    created_team = response.json()
    created_teams.append(created_team)


@pytest.mark.smoke
@pytest.mark.functional
def test_add_team_with_valid_user(setup_add_team):
    headers, created_teams = setup_add_team
    payload = PayloadTeam().build_payload_add_team(name="prueba_valid_user", layoutSetName="Layout 1", workingTimeCalendarName="Calendar", layoutSetId="6675949a021ad4859", workingTimeCalendarId="667594aa8582445d8")
    response = EspocrmRequest().post(EndpointTeams.team(), headers, payload)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_add_team_schema_schema_file(response.json())
    created_team = response.json()
    created_teams.append(created_team)


@pytest.mark.smoke
@pytest.mark.functional
def test_add_team_with_invalid_user(setup_add_team, get_headers):
    headers = Auth().get_invalid_user_headers(get_headers)
    created_teams = setup_add_team
    payload = PayloadTeam().build_payload_add_team(name="prueba_invalid_user", layoutSetName="Layout 1", workingTimeCalendarName="Calendar", layoutSetId="6675949a021ad4859", workingTimeCalendarId="667594aa8582445d8")
    response = EspocrmRequest().post(EndpointTeams.team(), headers, payload)
    AssertionStatusCode().assert_status_code_401(response)

