import pytest
from src.espocrm_api.endpoint_users import EndpointUsers
from src.resources.authentifications.authentification import Auth
from src.espocrm_api.api_request import EspocrmRequest
from src.assertions.status_code_assertions import AssertionStatusCode
from src.assertions.schema_assertions import AssertionSchemas
from src.assertions.users_assertions import AssertionUsers
from src.payloads.payloads_user import PayloadUser



@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.functional
def test_user_sort_asc(setup_add_user_asc):
    headers = setup_add_user_asc
    response = EspocrmRequest().get(EndpointUsers.order(order='asc'), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_users_order_asc_schema_file(response.json())


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.functional
def test_user_sort_desc(setup_add_user_asc):
    headers = setup_add_user_asc
    response = EspocrmRequest().get(EndpointUsers.order(order='desc'), headers)
    AssertionStatusCode().assert_status_code_200(response)


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.functional
def test_user_asc_invalid_credentials(get_headers):
    headers = Auth().get_invalid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointUsers.order(order='asc'), headers)
    AssertionStatusCode().assert_status_code_401(response)
    AssertionUsers().assert_response_empty(response.text)


@pytest.mark.regression
@pytest.mark.functional
def test_pagination_list_size(setup_add_user_asc):
    maxSize = 10
    headers = setup_add_user_asc
    response = EspocrmRequest().get(EndpointUsers.order(maxSize=maxSize), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_users_order_asc_schema_file(response.json())
    AssertionUsers().assert_list_no_empty(response.json())
    AssertionUsers().assert_list_length_within_range(response.json(), max_len=maxSize)


@pytest.mark.regression
@pytest.mark.functional
def test_invalid_order_by_parameters(setup_add_user_asc):
    headers = setup_add_user_asc
    response = EspocrmRequest().get(EndpointUsers.order(orderBy="campo_inexistente"), headers)
    AssertionStatusCode().assert_status_code_400(response)


@pytest.mark.regression
@pytest.mark.functional
def test_invalid_order_parameters(setup_add_user_asc):
    headers = setup_add_user_asc
    response = EspocrmRequest().get(EndpointUsers.order(order="campo_inexistente"), headers)
    AssertionStatusCode().assert_status_code_400(response)


@pytest.mark.regression
@pytest.mark.functional
def test_optional_fields_sorting(setup_add_user_asc):
    orderBy = 'emailAddress'
    headers = setup_add_user_asc
    response = EspocrmRequest().get(EndpointUsers.order(orderBy=orderBy), headers)
    AssertionStatusCode().assert_status_code_200(response)


