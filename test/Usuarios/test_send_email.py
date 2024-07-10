import pytest, random, string
from src.espocrm_api.endpoint import Endpoint
from src.resources.authentifications.authentification import Auth
from src.espocrm_api.api_request import EspocrmRequest
from src.assertions.status_code_assertions import AssertionStatusCode
from src.assertions.users_assertions import AssertionUsers
from src.resources.call_request.user import UserCall
from src.payloads.payloads_user import PayloadUser


@pytest.mark.smoke
@pytest.mark.functional
def test_send_user_email_with_required_fields(setup_teardown_user):
    headers, user = setup_teardown_user
    payload = PayloadUser().build_payload_email(to=user["emailAddress"], subject="Prueba")
    response = EspocrmRequest().post(Endpoint.email(), headers, payload)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionUsers().assert_response_is_not_empty(response)
    response_data = response.json()
    AssertionUsers().assert_valid_email_response(response_data, user["emailAddress"], "Prueba")


@pytest.mark.smoke
@pytest.mark.functional
def test_send_user_email_with_invalid_data(setup_teardown_user):
    headers, user = setup_teardown_user
    invalid_email = "invalid_email_format"
    invalid_subject = ""
    payload = PayloadUser().build_payload_email(to=invalid_email, subject=invalid_subject)
    response = EspocrmRequest().post(Endpoint.email(), headers, payload)
    AssertionStatusCode().assert_status_code_400(response)
