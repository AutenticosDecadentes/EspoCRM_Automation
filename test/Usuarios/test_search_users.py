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
def test_search_user_by_valid_name(setup_search_user):
    headers, user1, user2, user3, user4 = setup_search_user
    response = EspocrmRequest().get(EndpointUsers.search_usuers(where="DiegoDos"), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_users_search_schema_file(response.json())


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.functional
def test_search_user_by_found_last_name(setup_search_user):
     headers, user1, user2, user3, user4 = setup_search_user
     response = EspocrmRequest().get(EndpointUsers.search_usuers(where="tres"), headers)
     AssertionStatusCode().assert_status_code_200(response)
     AssertionSchemas().assert_users_search_schema_file(response.json())

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.functional
def test_search_user_by_found_username(setup_search_user):
    headers, user1, user2, user3, user4 = setup_search_user
    response = EspocrmRequest().get(EndpointUsers.search_usuers(where="diego_prueba"), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_users_search_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_search_user_by_found_email(setup_search_user):
    headers, user1, user2, user3, user4= setup_search_user
    response = EspocrmRequest().get(EndpointUsers.search_usuers(where="diego.dos@gmail.com"), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_users_search_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_search_user_by_invalid_name(setup_search_user):
    headers, user1, user2, user3, user4 = setup_search_user
    response = EspocrmRequest().get(EndpointUsers.search_usuers(where="mnbmbmbjkhghjjjg"), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_users_search_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_search_user_by_invalid_last_name(setup_search_user):
    headers, user1, user2, user3, user4 = setup_search_user
    response = EspocrmRequest().get(EndpointUsers.search_usuers(where="apellido_no_valido"), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_users_search_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_search_user_by_invalid_username(setup_search_user):
    headers, user1, user2, user3, user4 = setup_search_user
    response = EspocrmRequest().get(EndpointUsers.search_usuers(where="username_no_valido"), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_users_search_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_search_user_by_invalid_email(setup_search_user):
    headers, user1, user2, user3, user4 = setup_search_user
    response = EspocrmRequest().get(EndpointUsers.search_usuers(where="email_no_valido"), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_users_search_schema_file(response.json())


#
@pytest.mark.regression
@pytest.mark.functional
def test_search_user_empty_field(setup_search_user):
    headers, user1, user2, user3, user4 = setup_search_user
    response = EspocrmRequest().get(EndpointUsers.search_usuers(where=""), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_users_search_schema_file(response.json())


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.functional
def test_search_user_invalid_login(get_headers, setup_search_user):
    headers, user1, user2, user3, user4 = setup_search_user
    headers1 = Auth().get_invalid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointUsers.search_usuers(where="diego_prueba4"), headers1)
    AssertionStatusCode().assert_status_code_401(response)
    AssertionUsers().assert_response_empty(response.text)


@pytest.mark.regression
@pytest.mark.functional
def test_search_users_with_maxSize(setup_search_user):
    headers, user1, user2, user3, user4 = setup_search_user
    response = EspocrmRequest().get(EndpointUsers.search_usuers(maxSize=5), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_users_search_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_search_users_with_offset(setup_search_user):
    headers, user1, user2, user3, user4 = setup_search_user
    response = EspocrmRequest().get(EndpointUsers.search_usuers(offset=10), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_users_search_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_search_users_with_orderBy_name(setup_search_user):
    headers, user1, user2, user3, user4 = setup_search_user
    response = EspocrmRequest().get(EndpointUsers.search_usuers(orderBy="name"), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_users_search_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_search_users_with_order_desc(setup_search_user):
    headers, user1, user2, user3, user4 = setup_search_user
    response = EspocrmRequest().get(EndpointUsers.search_usuers(order="desc"), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_users_search_schema_file(response.json())
