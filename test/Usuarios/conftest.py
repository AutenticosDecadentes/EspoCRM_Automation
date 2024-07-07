import pytest
from src.resources.authentifications.authentification import Auth
from src.payloads.payloads_user import PayloadUser
from src.resources.call_request.user import UserCall


@pytest.fixture(scope="function")
def setup_create_user(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    payload_user_1 = PayloadUser().build_payload_add_user(userName="miki", salutationName="Mrs.",
                                                          firstName="alejandro",
                                                          lastName="aliendre")
    user = UserCall().create(headers, payload_user_1)
    yield headers, user