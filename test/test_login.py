# from src.assertions.equipos_assertions import AssertionEquipos
# from src.assertions.schema_assertions import AssertionSchemas
# from src.espocrm_api.endpoint import Endpoint
# from src.resources.authentifications.authentication import Authentication
#
#
# def test_login_valido(get_headers):
#     response = Authentication().authenticate_valid_user(get_headers, Endpoint.LOGIN.value, 'GET')
#     AssertionSchemas.assert_status_code(response, 200)
#
#
# def test_login_invalido(get_headers):
#     response = Authentication().authenticate_invalid_user(get_headers, Endpoint.LOGIN.value, 'GET')
#     AssertionSchemas.assert_status_code(response, 401)
#
#
# def test_login_usuario_deshabilitado(get_headers):
#     response = Authentication().authenticate_user_disabled(get_headers, Endpoint.LOGIN.value, 'GET')
#     AssertionSchemas.assert_status_code(response, 401)
