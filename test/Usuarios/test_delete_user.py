import pytest, random, string
from src.espocrm_api.api_request import EspocrmRequest
from src.assertions.status_code_assertions import AssertionStatusCode
from src.assertions.users_assertions import AssertionUsers
from src.resources.call_request.user import UserCall
from src.resources.authentifications.authentification import Auth
from src.espocrm_api.endpoint_users import EndpointUsers
@pytest.mark.smoke
def test_delete_user_valid_user(setup_create_user):
    headers, user = setup_create_user
    response = EspocrmRequest().delete(EndpointUsers.view(user['id']), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionUsers().assert_response_true(response)

@pytest.mark.smoke
def test_delete_user_invalid_user(setup_create_user, get_headers):
    headers, user = setup_create_user
    headersAux = headers
    headers = Auth().get_unauthorized_users_user_headers(get_headers)
    response = EspocrmRequest().delete(EndpointUsers.view(user['id']), headers)
    AssertionStatusCode().assert_status_code_403(response)
    UserCall().delete(headersAux, user['id'])

@pytest.mark.smoke
def test_delete_user_nonexistent_user(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    user_id_invalid = ''.join(random.choices(string.ascii_letters + string.digits, k=17))
    response = EspocrmRequest().delete(EndpointUsers.view(user_id_invalid), headers)
    AssertionStatusCode().assert_status_code_404(response)


