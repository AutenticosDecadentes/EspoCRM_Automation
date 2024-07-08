import pytest
from src.espocrm_api.endpoint_teams import EndpointTeams
from src.payloads.payloads_team import PayloadTeam
from src.espocrm_api.api_request import EspocrmRequest
from src.assertions.status_code_assertions import AssertionStatusCode
from src.assertions.schema_assertions import AssertionSchemas
from src.resources.authentifications.authentification import Auth


@pytest.mark.regression
@pytest.mark.functional
def test_edit_team_all_data(setup_edit_team):
    headers, team = setup_edit_team
    payload = PayloadTeam().build_payload_add_team(name="prueba2222", layoutSetName="Layout 1",
                                                   workingTimeCalendarName="Calendar", layoutSetId="6675949a021ad4859",
                                                   workingTimeCalendarId="667594aa8582445d8")
    response = EspocrmRequest().put(EndpointTeams.view(team['id']), headers, payload)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_add_team_schema_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_edit_team_name_empty(setup_edit_team):
    headers, team = setup_edit_team
    payload = PayloadTeam().build_payload_add_team(name="", layoutSetName="Layout 1", rolesIds="66758f0575dbc3464",
                                                   rolesNames="Prueba",
                                                   workingTimeCalendarName="Calendar", layoutSetId="6675949a021ad4859",
                                                   workingTimeCalendarId="667594aa8582445d8")
    response = EspocrmRequest().put(EndpointTeams.view(team['id']), headers, payload)
    AssertionStatusCode().assert_status_code_400(response)
    AssertionSchemas().assert_add_team_schema_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_edit_team_edit_name(setup_edit_team):
    headers, team = setup_edit_team
    payload = PayloadTeam().build_payload_add_team(name="prueba2222")
    response = EspocrmRequest().put(EndpointTeams.view(team['id']), headers, payload)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_add_team_schema_schema_file(response.json())


@pytest.mark.smoke
@pytest.mark.functional
def test_edit_team_with_valid_user(setup_edit_team):
    headers, team = setup_edit_team
    payload = PayloadTeam().build_payload_add_team(name="prueba_valid_user", layoutSetName="Layout 1",
                                                   workingTimeCalendarName="Calendar", layoutSetId="6675949a021ad4859",
                                                   workingTimeCalendarId="667594aa8582445d8")
    response = EspocrmRequest().put(EndpointTeams.view(team['id']), headers, payload)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_add_team_schema_schema_file(response.json())


@pytest.mark.smoke
@pytest.mark.functional
def test_add_team_with_invalid_user(setup_edit_team, get_headers):
    headers = Auth().get_invalid_user_headers(get_headers)
    valid_headers, team = setup_edit_team
    payload = PayloadTeam().build_payload_add_team(
        name="prueba_invalid_user",
        layoutSetName="Layout 1",
        workingTimeCalendarName="Calendar",
        layoutSetId="6675949a021ad4859",
        workingTimeCalendarId="667594aa8582445d8"
    )
    response = EspocrmRequest().put(EndpointTeams.view(team['id']), headers, payload)
    AssertionStatusCode().assert_status_code_401(response)
