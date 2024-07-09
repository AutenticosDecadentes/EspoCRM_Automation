import pytest
from src.espocrm_api.endpoint_users import EndpointUsers
from src.payloads.payloads_user import PayloadUser
from src.espocrm_api.api_request import EspocrmRequest
from src.assertions.status_code_assertions import AssertionStatusCode
from src.assertions.schema_assertions import AssertionSchemas


@pytest.mark.functional
def test_add_invalid_userName(setup_add_user):
    headers, created_users = setup_add_user
    payload = PayloadUser().build_payload_add_user(userName="", salutationName="Mrs.", firstName="nombre", lastName="nombre")
    response = EspocrmRequest().post(EndpointUsers.user(), headers, payload)
    AssertionStatusCode().assert_status_code_400(response)

@pytest.mark.smoke
def test_add_user_without_password(setup_add_user):
     headers, created_users = setup_add_user
     payload = PayloadUser().build_payload_add_user(userName="noname", salutationName="Mrs.", firstName="apellido", lastName="apellidio")
     response = EspocrmRequest().post(EndpointUsers.user(), headers, payload)
     AssertionStatusCode().assert_status_code_200(response)
     created_user = response.json()
     created_users.append(created_user)

@pytest.mark.smoke
def test_add_user_duplicate_userName(setup_add_user):
    headers, created_users = setup_add_user
    payload = PayloadUser().build_payload_add_user(userName = "estrellita11",
    type = "admin",
    salutationName = "Mr.",
    firstName = "vadria",
    lastName = "sacfvs",
    isActive = True,
    emailAddress = "vianvfver00@gmail.com",
    phoneNumber = "+59172256555",
    gender = "Male",
    rolesIds = "66758ef1d775a381e",
    rolesNames = {"66758ef1d775a381e": "Administrador"},
    workingTimeCalendarId = "667594aa8582445d8",
    workingTimeCalendarName = "Calendar",
    layoutSetId = "6675949a021ad4859",
    layoutSetName = "Layout 1",
    deleteId = "0",
    password = "",
    passwordConfirm = "")
    response = EspocrmRequest().post(EndpointUsers.user(), headers, payload)
    print( payload)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_add_user_schema_file(response.json())
    created_user = response.json()
    created_users.append(created_user)
    response1 = EspocrmRequest().post(EndpointUsers.user(), headers, payload)
    AssertionStatusCode().assert_status_code_409(response1)


@pytest.mark.functional
def test_add_user_with_valid_complete_data(setup_add_user):
    headers, created_users = setup_add_user
    payload = PayloadUser().build_payload_add_user(userName = "vianquis",
    type = "admin",
    salutationName = "Mr.",
    firstName = "vianquisuwu",
    lastName = "Marrrrrrrr",
    isActive = True,
    emailAddress = "vianquis00@gmail.com",
    phoneNumber = "+59172255555",
    gender = "Male",
    rolesIds = "66758ef1d775a381e",
    rolesNames = {"66758ef1d775a381e": "Administrador"},
    workingTimeCalendarId = "667594aa8582445d8",
    workingTimeCalendarName = "Calendar",
    layoutSetId = "6675949a021ad4859",
    layoutSetName = "Layout 1",
    deleteId = "0",
    password = "",
    passwordConfirm = "")
    response = EspocrmRequest().post(EndpointUsers.user(), headers, payload)
    AssertionStatusCode().assert_status_code_200(response)
    created_user = response.json()
    created_users.append(created_user)

