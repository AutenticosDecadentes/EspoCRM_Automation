import pytest
from src.payloads.payloads_user import PayloadUser
from src.assertions.schema_assertions import AssertionSchemas
from src.assertions.status_code_assertions import AssertionStatusCode
from src.espocrm_api.api_request import EspocrmRequest
from src.espocrm_api.endpoint import Endpoint
from src.resources.authentifications.authentification import Auth


@pytest.mark.smoke
@pytest.mark.functional
def test_successful_role_update(setup_multiple_user):
    headers, user1, user2, user3, user4 = setup_multiple_user
    user_ids = [user1['id'], user2['id'], user3['id'], user4['id']]
    payload = PayloadUser().build_payload_update_users_roles(user_ids, "66758f2c021e4e23f")
    AssertionSchemas().assert_user_update_multiple_users_schema_payload_file(payload)
    response = EspocrmRequest().post(Endpoint.massAction(), headers, payload)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionSchemas.validate_json_schema(response.json(), "test_update_multiple_users.json")


@pytest.mark.smoke
@pytest.mark.functional
def test_invalid_user_role_update(setup_multiple_user, get_headers):
    headers, user1, user2, user3, user4 = setup_multiple_user
    headers1 = Auth().get_unauthorized_users_user_headers(get_headers)
    user_ids = [user1['id'], user2['id'], user3['id'], user4['id']]
    payload = PayloadUser().build_payload_update_users_roles(user_ids, "66758f2c021e4e23f")
    AssertionSchemas().assert_user_update_multiple_users_schema_payload_file(payload)
    response = EspocrmRequest().post(Endpoint.massAction(), headers1, payload)
    AssertionStatusCode.assert_status_code_403(response)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_nonexistent_users_update(setup_multiple_user):
    headers, user1, user2, user3, user4 = setup_multiple_user
    nonexistent_user_ids = ["nonexistent_id_1", "nonexistent_id_2", "nonexistent_id_3"]
    payload = PayloadUser().build_payload_update_users_roles(nonexistent_user_ids, "66758f2c021e4e23f")
    response = EspocrmRequest().post(Endpoint.massAction(), headers, payload)
    AssertionStatusCode.assert_status_code_404(response)
