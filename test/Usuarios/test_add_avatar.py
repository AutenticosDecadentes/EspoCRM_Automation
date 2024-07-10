# import pytest
# from src.espocrm_api.endpoint_users import EndpointUsers
# from src.payloads.payloads_user import PayloadUser
# from src.espocrm_api.api_request import EspocrmRequest
# from src.assertions.status_code_assertions import AssertionStatusCode
# from src.payloads.payload_avatar import PayloadAvatar
# from src.Imagenes.Importar import Imagen
# from src.assertions.schema_assertions import AssertionSchemas
#
#
# @pytest.mark.smoke
# @pytest.mark.functional
# def test_add_avatar_file_valid_image(setup_add_avatar):
#     headers, user = setup_add_avatar
#     payload = PayloadAvatar().build_payload_add_avatar(Imagen.imagen_avatar.value)
#     response = EspocrmRequest().post(EndpointUsers.avatar(), headers, payload)
#     AssertionStatusCode().assert_status_code_200(response)
#     AssertionSchemas().assert_add_avatar_schema_file(response.json())
#
# @pytest.mark.smoke
# @pytest.mark.functional
# def test_add_avatar_file_invalid_image(setup_add_avatar):
#     headers, user = setup_add_avatar
#     payload = PayloadAvatar().build_payload_add_avatar(Imagen.imagenInvalida.value )
#     response = EspocrmRequest().post(EndpointUsers.avatar(), headers, payload)
#     AssertionStatusCode().assert_status_code_400(response)
#
#
