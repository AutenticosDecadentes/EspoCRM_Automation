import pytest
from src.espocrm_api.endpoint_users import EndpointUsers
from src.payloads.payloads_user import PayloadUser
from src.espocrm_api.api_request import EspocrmRequest
from src.assertions.status_code_assertions import AssertionStatusCode
from src.assertions.schema_assertions import AssertionSchemas
from src.resources.authentifications.authentification import Auth


# def test_add_invalid_userName(setup_add_invalid_user):
#     headers = setup_add_invalid_user
#     payload = PayloadUser().build_payload_add_user(userName="", salutationName="", firstName="",lastName="")
#     response = EspocrmRequest().post(EndpointUsers.user(), headers, payload)
#     AssertionStatusCode().assert_status_code_400(response)

def test_add_user_without_password(setup_add_user):
    headers, created_users = setup_add_user
    payload = PayloadUser().build_payload_add_user(userName="Aleeeeeeqqqq", salutationName="Mr", firstName="Juaaaan", lastName="Veizagaaaa")
    response = EspocrmRequest().post(EndpointUsers.user(), headers, payload)
    print(payload)
    # created_user = response.json()
    # created_users.append(created_user)
    #AssertionStatusCode().assert_status_code_200(response)


