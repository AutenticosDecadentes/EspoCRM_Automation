import pytest
from src.resources.authentifications.authentification import Auth
from src.espocrm_api.api_request import EspocrmRequest
from src.espocrm_api.endpoint_teams import EndpointTeams
from src.assertions.status_code_assertions import AssertionStatusCode
from src.assertions.schema_assertions import AssertionSchemas
from src.assertions.teams_assertions import AssertionTeams


@pytest.mark.regression
@pytest.mark.functional
def test_list_teams_with_data(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams.list(), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_teams_list_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_list_teams_order_asc(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams.list(order='asc'), headers)
    AssertionStatusCode().assert_status_code_200(response)


@pytest.mark.regression
@pytest.mark.functional
def test_list_teams_order_invalid(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams.list(order='ASCSA'), headers)
    AssertionStatusCode().assert_status_code_400(response)
    AssertionTeams().assert_response_empty(response.text)


@pytest.mark.regression
@pytest.mark.functional
def test_list_teams_order_desc(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams.list(order='desc'), headers)
    AssertionStatusCode().assert_status_code_200(response)


@pytest.mark.regression
@pytest.mark.functional
def test_list_teams_without_data(get_headers):
    headers = Auth().get_without_teams_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams.list(), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_teams_list_schema_file(response.json())
    AssertionTeams().assert_empty_field_list(response.json())
    AssertionTeams().assert_field_total_equals(response.json(), 0)


@pytest.mark.regression
@pytest.mark.functional
def test_list_teams_without_select(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams.list(select=None), headers)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionSchemas.assert_teams_list_without_select_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_list_teams_select_unknown(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams.list(select="unknown"), headers)
    AssertionSchemas.assert_teams_list_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_list_teams_select_special(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams.list(select="***"), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_teams_list_schema_file(response.json())
    AssertionTeams().assert_field_list_no_empty(response.json())


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.functional
def test_list_teams_invalid_authentication(get_headers):
    headers = Auth().get_invalid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams.list(), headers)
    AssertionStatusCode().assert_status_code_401(response)
    AssertionTeams().assert_response_empty(response.text)


@pytest.mark.regression
@pytest.mark.functional
def test_list_teams_unauthorized(get_headers):
    headers = Auth().get_unauthorized_teams_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams.list(), headers)
    AssertionStatusCode().assert_status_code_403(response)
    AssertionTeams().assert_response_empty(response.text)


@pytest.mark.regression
@pytest.mark.functional
def test_list_teams_maxsize_major_total(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams.list(maxSize=200), headers)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionSchemas().assert_teams_list_schema_file(response.json())
    AssertionTeams().assert_field_list_no_empty(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_list_teams_maxsize_cero(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams.list(maxSize=0), headers)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionSchemas().assert_teams_list_schema_file(response.json())
    AssertionTeams().assert_empty_field_list(response.json())


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_list_teams_maxsize_negative(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams.list(maxSize=-1), headers)
    AssertionStatusCode().assert_status_code_400(response)
    AssertionTeams.assert_response_empty(response.text)


@pytest.mark.regression
@pytest.mark.functional
def test_list_teams_maxsize_string(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams.list(maxSize="as"), headers)
    AssertionStatusCode().assert_status_code_200(response)


@pytest.mark.regression
@pytest.mark.functional
def test_list_teams_offset_major_total(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams.list(offset=200), headers)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionSchemas().assert_teams_list_schema_file(response.json())
    AssertionTeams().assert_empty_field_list(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_list_teams_offset_cero(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams.list(offset=0), headers)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionSchemas().assert_teams_list_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_list_teams_offset_negative(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams.list(offset=-1), headers)
    AssertionStatusCode().assert_status_code_400(response)
    AssertionTeams.assert_response_empty(response.text)


@pytest.mark.regression
@pytest.mark.functional
def test_list_teams_offset_string(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams.list(offset="as"), headers)
    AssertionStatusCode().assert_status_code_200(response)


@pytest.mark.regression
@pytest.mark.functional
def test_list_teams_ordeby_unknown(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointTeams.list(orderBy='unknown'), headers)
    AssertionStatusCode().assert_status_code_400(response)
    AssertionTeams.assert_response_empty(response.text)
