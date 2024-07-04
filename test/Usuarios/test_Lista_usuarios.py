# import pytest
# from src.assertions.usuarios_assertions import AssertionUsuarios
# from src.assertions.schema_assertions import AssertionSchemas
# from src.espocrm_api.endpoint import Endpoint
# from src.resources.authentifications.authentication import Authentication
#
#
# @pytest.mark.smoke
# @pytest.mark.regression
# @pytest.mark.functional
# def test_lista_usuarios_con_datos_exitoso(get_headers):
#     response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTAR_USUARIOS(), 'GET')
#     AssertionSchemas().assert_status_code(response, 200)
#     AssertionSchemas().assert_usuario_lista_schema_file(response.json())
#
#
# @pytest.mark.regression
# @pytest.mark.functional
# def test_lista_usuarios_requiere_autenticacion(get_headers):
#     response = Authentication().authenticate_invalid_user(get_headers, Endpoint.LISTAR_USUARIOS(), 'GET')
#     AssertionSchemas().assert_status_code(response, 401)
#
#
# @pytest.mark.regression
# @pytest.mark.functional
# def test_lista_usuarios_orden_descendente(get_headers):
#     response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTAR_USUARIOS(order='desc'), 'GET')
#     AssertionSchemas().assert_status_code(response, 200)
#     AssertionUsuarios().assert_check_orden_desc(response.json())
#     AssertionSchemas().assert_usuario_lista_schema_file(response.json())
#
#
# @pytest.mark.regression
# @pytest.mark.functional
# def test_lista_usuarios_orden_ascendente(get_headers):
#     response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTAR_USUARIOS(order='asc'), 'GET')
#     AssertionSchemas().assert_status_code(response, 200)
#     AssertionUsuarios().assert_check_orden_asc(response.json())
#     AssertionSchemas().assert_usuario_lista_schema_file(response.json())
#
#
# @pytest.mark.regression
# @pytest.mark.functional
# def test_lista_usuarios_lista_vacia(get_headers):
#     response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTAR_USUARIOS(maxSize=0), 'GET')
#     AssertionSchemas().assert_status_code(response, 200)
#     AssertionUsuarios().assert_empty_list(response.json())
#     AssertionSchemas().assert_usuario_lista_schema_file(response.json())
#
#
# @pytest.mark.regression
# @pytest.mark.functional
# def test_lista_usuarios_campos_especificados(get_headers):
#     response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTAR_USUARIOS(), 'GET')
#     AssertionSchemas().assert_status_code(response, 200)
#     AssertionUsuarios().assert_campos_especificados(response.json())
#     AssertionSchemas().assert_usuario_lista_schema_file(response.json())
#
#
# @pytest.mark.regression
# @pytest.mark.functional
# def test_lista_usuarios_total(get_headers):
#     response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTAR_USUARIOS(), 'GET')
#     AssertionSchemas().assert_status_code(response, 200)
#     AssertionUsuarios().assert_total(response.json())
#     AssertionSchemas().assert_usuario_lista_schema_file(response.json())
#
#
# @pytest.mark.regression
# @pytest.mark.functional
# def test_lista_usuarios_direccion_no_encontrada(get_headers):
#     response = Authentication().authenticate_valid_user(get_headers, Endpoint.USUARIO_ERROR, 'GET')
#     AssertionSchemas().assert_status_code(response, 404)
