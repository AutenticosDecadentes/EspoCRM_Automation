# import requests
# import pytest
#
# from src.assertions.usuarios_assertions import AssertionUsuarios
# from src.assertions.schema_assertions import AssertionSchemas
# from src.espocrm_api.endpoint import Endpoint
# from src.resources.authentifications.authentication import Authentication
#
#
# @pytest.mark.smoke
# @pytest.mark.regression
# @pytest.mark.functional
# def test_buscar_usuario_por_nombre_valido(get_headers):
#     response = Authentication().authenticate_valid_user(get_headers, Endpoint.BUSCAR_USUARIOS(where="darwin"), 'GET')
#     AssertionSchemas().assert_status_code(response, 200)
#     AssertionSchemas().assert_usuarios_buscar_schema_file(response.json())
#
# @pytest.mark.smoke
# @pytest.mark.regression
# @pytest.mark.functional
# def test_buscar_usuario_por_apellido_encontrado(get_headers):
#     response = Authentication().authenticate_valid_user(get_headers, Endpoint.BUSCAR_USUARIOS(where="Montano"), 'GET')
#     AssertionSchemas().assert_status_code(response, 200)
#     AssertionSchemas().assert_usuarios_buscar_schema_file(response.json())
#
# @pytest.mark.smoke
# @pytest.mark.regression
# @pytest.mark.functional
# def test_buscar_usuario_por_username_encontrado(get_headers):
#     response = Authentication().authenticate_valid_user(get_headers, Endpoint.BUSCAR_USUARIOS(where="hola"), 'GET')
#     AssertionSchemas().assert_status_code(response, 200)
#     AssertionSchemas().assert_usuarios_buscar_schema_file(response.json())
#
# @pytest.mark.regression
# @pytest.mark.functional
# def test_buscar_usuario_por_email_encontrado(get_headers):
#     response = Authentication().authenticate_valid_user(get_headers, Endpoint.BUSCAR_USUARIOS(where="201604461@est.umss"), 'GET')
#     AssertionSchemas().assert_status_code(response, 200)
#     AssertionSchemas().assert_usuarios_buscar_schema_file(response.json())
#
# @pytest.mark.regression
# @pytest.mark.functional
# def test_buscar_usuario_por_email_invalido(get_headers): # Corregido: email inválido, no encontrado
#     response = Authentication().authenticate_valid_user(get_headers, Endpoint.BUSCAR_USUARIOS(where="mnbmbmbjkhghjjjg"), 'GET')
#     AssertionSchemas().assert_status_code(response, 200)
#     AssertionSchemas().assert_usuarios_buscar_schema_file(response.json())
#
# @pytest.mark.regression
# @pytest.mark.functional
# def test_buscar_usuario_por_apellido_no_valido(get_headers):
#     response = Authentication().authenticate_valid_user(get_headers, Endpoint.BUSCAR_USUARIOS(where="apellido_no_valido"), 'GET')
#     AssertionSchemas().assert_status_code(response, 200)
#     AssertionSchemas().assert_usuarios_buscar_schema_file(response.json())
#
# @pytest.mark.regression
# @pytest.mark.functional
# def test_buscar_usuario_por_username_no_valido(get_headers):
#     response = Authentication().authenticate_valid_user(get_headers, Endpoint.BUSCAR_USUARIOS(where="username_no_valido"), 'GET')
#     AssertionSchemas().assert_status_code(response, 200)
#     AssertionSchemas().assert_usuarios_buscar_schema_file(response.json())
#
# @pytest.mark.regression
# @pytest.mark.functional
# def test_buscar_usuario_por_email_no_valido(get_headers):
#     response = Authentication().authenticate_valid_user(get_headers, Endpoint.BUSCAR_USUARIOS(where="email_no_valido"), 'GET')
#     AssertionSchemas().assert_status_code(response, 200)
#     AssertionSchemas().assert_usuarios_buscar_schema_file(response.json())
#
# @pytest.mark.regression
# @pytest.mark.functional
# def test_buscar_usuario_campo_vacio(get_headers):
#     response = Authentication().authenticate_valid_user(get_headers, Endpoint.BUSCAR_USUARIOS(where=""), 'GET')
#     AssertionSchemas().assert_status_code(response, 200)
#     AssertionSchemas().assert_usuarios_buscar_schema_file(response.json())
#
# @pytest.mark.smoke
# @pytest.mark.regression
# @pytest.mark.functional
# def test_buscar_usuario_con_login_invalido(get_headers):
#     response = Authentication().authenticate_invalid_user(get_headers, Endpoint.BUSCAR_USUARIOS(where="diego"), 'GET')
#     AssertionSchemas().assert_status_code(response, 401)
#     AssertionSchemas().assert_response_vacio(response.text)
#
# @pytest.mark.regression
# @pytest.mark.functional
# def test_buscar_usuarios_con_maxSize(get_headers):
#     response = Authentication().authenticate_valid_user(
#         get_headers, Endpoint.BUSCAR_USUARIOS(maxSize=5), 'GET'
#     )
#     AssertionSchemas().assert_status_code(response, 200)
#     AssertionSchemas().assert_usuarios_buscar_schema_file(response.json())
#
# @pytest.mark.regression
# @pytest.mark.functional
# def test_buscar_usuarios_con_offset(get_headers):
#     response = Authentication().authenticate_valid_user(
#         get_headers, Endpoint.BUSCAR_USUARIOS(offset=10), 'GET'
#     )
#     AssertionSchemas().assert_status_code(response, 200)
#     AssertionSchemas().assert_usuarios_buscar_schema_file(response.json())
#
# @pytest.mark.regression
# @pytest.mark.functional
# def test_buscar_usuarios_con_orderBy_nombre(get_headers):
#     response = Authentication().authenticate_valid_user(
#         get_headers, Endpoint.BUSCAR_USUARIOS(orderBy="name"), 'GET'
#     )
#     AssertionSchemas().assert_status_code(response, 200)
#     AssertionSchemas().assert_usuarios_buscar_schema_file(response.json())
#
# @pytest.mark.regression
# @pytest.mark.functional
# def test_buscar_usuarios_con_order_desc(get_headers):
#     response = Authentication().authenticate_valid_user(
#         get_headers, Endpoint.BUSCAR_USUARIOS(order="desc"), 'GET'
#     )
#     AssertionSchemas().assert_status_code(response, 200)
#     AssertionSchemas().assert_usuarios_buscar_schema_file(response.json())