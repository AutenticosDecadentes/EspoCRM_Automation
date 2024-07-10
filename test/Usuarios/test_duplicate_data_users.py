# import pytest
# from src.payloads.payloads_user import PayloadUser
# from src.assertions.schema_assertions import AssertionSchemas
# from src.espocrm_api.api_request import EspocrmRequest
# from src.espocrm_api.endpoint_users import EndpointUsers
# from src.assertions.status_code_assertions import AssertionStatusCode
#
#
# @pytest.mark.regression
# @pytest.mark.functional
# @pytest.mark.smoke
# def test_duplicate_data_user_with_valid_id(setup_duplicate_data_team):
#     headers, user = setup_duplicate_data_team
#     payload = PayloadUser().build_payload_duplicate_data_user(user['id'])
#     AssertionSchemas().assert_user_duplicate_data_schema_payload_file(payload)
#     response = EspocrmRequest().post(EndpointUsers.duplicate_data(), headers, payload)
#     AssertionStatusCode().assert_status_code_200(response)
#     print(response.json())
#     AssertionSchemas().assert_user_duplicate_data_schema_file(response.json())
#
#
# @pytest.mark.regression
# @pytest.mark.functional
# @pytest.mark.smoke
# def test_duplicate_data_user_with_invalid_id(setup_teardown_user):
#     headers, user = setup_teardown_user
#     payload = PayloadUser().build_payload_duplicate_data_user("0")
#     AssertionSchemas().assert_user_duplicate_data_schema_payload_file(payload)
#     response = EspocrmRequest().post(EndpointUsers.duplicate_data(), headers, payload)
#     AssertionStatusCode().assert_status_code_400(response)
#
