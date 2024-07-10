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
def test_search_user_by_valid_name(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointUsers.search_usuers(where="darwin"), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_users_search_schema_file(response.json())


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.functional
def test_search_user_by_found_last_name(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointUsers.search_usuers(where="Montano"), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_users_search_schema_file(response.json())


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.functional
def test_search_user_by_found_username(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointUsers.search_usuers(where="hola"), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_users_search_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_search_user_by_found_email(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointUsers.search_usuers(where="201604461@est.umss"), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_users_search_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_search_user_by_invalid_name(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointUsers.search_usuers(where="mnbmbmbjkhghjjjg"), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_users_search_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_search_user_by_invalid_last_name(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointUsers.search_usuers(where="apellido_no_valido"), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_users_search_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_search_user_by_invalid_username(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointUsers.search_usuers(where="username_no_valido"), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_users_search_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_search_user_by_invalid_email(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointUsers.search_usuers(where="email_no_valido"), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_users_search_schema_file(response.json())


#
@pytest.mark.regression
@pytest.mark.functional
def test_search_user_empty_field(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointUsers.search_usuers(where=""), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_users_search_schema_file(response.json())


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.functional
def test_search_user_invalid_login(get_headers):
    headers = Auth().get_invalid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointUsers.search_usuers(where="diego"), headers)
    AssertionStatusCode().assert_status_code_401(response)
    AssertionUsers().assert_response_empty(response.text)


@pytest.mark.regression
@pytest.mark.functional
def test_search_users_with_maxSize(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointUsers.search_usuers(maxSize=5), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_users_search_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_search_users_with_offset(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointUsers.search_usuers(offset=10), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_users_search_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_search_users_with_orderBy_name(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointUsers.search_usuers(orderBy="name"), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_users_search_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_search_users_with_order_desc(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointUsers.search_usuers(order="desc"), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_users_search_schema_file(response.json())
