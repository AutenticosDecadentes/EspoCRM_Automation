import pytest
from src.espocrm_api.endpoint_users import EndpointUsers
from src.resources.authentifications.authentification import Auth
from src.espocrm_api.api_request import EspocrmRequest
from src.assertions.status_code_assertions import AssertionStatusCode
from src.assertions.schema_assertions import AssertionSchemas
from src.assertions.users_assertions import AssertionUsers


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.functional
def test_list_users_with_successful_data(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointUsers.list(), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_users_list_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_list_users_required_authentication(get_headers):
    headers = Auth().get_invalid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointUsers.list(), headers)
    AssertionStatusCode().assert_status_code_401(response)


@pytest.mark.regression
@pytest.mark.functional
def test_list_users_descending_order(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointUsers.list(order='desc'), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_users_list_schema_file(response.json())


#
@pytest.mark.regression
@pytest.mark.functional
def test_list_users_ascending_order(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointUsers.list(order='asc'), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_users_list_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_list_users_empty_list(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointUsers.list(maxSize=0), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_users_list_schema_file(response.json())
    AssertionUsers().assert_empty_list(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_list_users_specified_fields(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointUsers.list(maxSize=0), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_users_list_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_list_users_total(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointUsers.list(maxSize=0), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_users_list_schema_file(response.json())


#
@pytest.mark.regression
@pytest.mark.functional
def test_list_users_address_not_found(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointUsers.user_error(), headers)
    AssertionStatusCode().assert_status_code_404(response)
