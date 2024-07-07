import pytest
from src.resources.authentifications.authentification import Auth
from src.resources.call_request.user import UserCall
@pytest.fixture(scope="function")
def setup_add_user(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    created_users = []
    yield headers, created_users
    for user in created_users:
        UserCall().delete(headers, user['id'])

#@pytest.fixture(scope="function")
#def setup_add_invalid_user(get_headers):
 #   headers = Auth().get_valid_user_headers(get_headers)

    #yield headers
