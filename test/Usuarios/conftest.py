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


@pytest.fixture(scope="function")
def setup_teardown_user(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)

    email_address_data = [
        {
            "emailAddress": "n.rita.veizaga.aguilar@gmail.com",
            "primary": True,
            "optOut": False,
            "invalid": False,
            "lower": "n.rita.veizaga.aguilar@gmail.com"
        }
    ]

    payload_user_1 = PayloadUser().build_payload_add_user(
        userName="rita_nicol",
        salutationName="Mrs.",
        firstName="Nicol",
        lastName="Rita",
        emailAddress="n.rita.veizaga.aguilar@gmail.com",
        emailAddressData=email_address_data
    )
    user = UserCall().create(headers, payload_user_1)
    yield headers, user

    UserCall().delete(headers, user["id"])


@pytest.fixture(scope="function")
def setup_add_user(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    created_users = []
    yield headers, created_users

    for user in created_users:
        UserCall().delete(headers, user['id'])



@pytest.fixture(scope="function")
def setup_multiple_user(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    payload_user_1 = PayloadUser().build_payload_add_user(userName="masivo1", salutationName="Mrs.",
                                                          firstName="alendro",
                                                          lastName="alire")
    payload_user_2 = PayloadUser().build_payload_add_user(userName="masivo2", salutationName="Mrs.",
                                                          firstName="alendro",
                                                          lastName="aliere")
    payload_user_3 = PayloadUser().build_payload_add_user(userName="masivo3", salutationName="Mrs.",
                                                          firstName="alejano",
                                                          lastName="aliere")
    payload_user_4 = PayloadUser().build_payload_add_user(userName="masivo4", salutationName="Mrs.",
                                                          firstName="alejndro",
                                                          lastName="aliere")
    user1 = UserCall().create(headers, payload_user_1)
    user2 = UserCall().create(headers, payload_user_2)
    user3 = UserCall().create(headers, payload_user_3)
    user4 = UserCall().create(headers, payload_user_4)

    yield headers, user1, user2, user3, user4

    UserCall().delete(headers, user1['id'])
    UserCall().delete(headers, user2['id'])
    UserCall().delete(headers, user3['id'])
    UserCall().delete(headers, user4['id'])

