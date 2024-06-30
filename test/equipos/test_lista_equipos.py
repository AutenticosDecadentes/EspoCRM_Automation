import pytest
from src.assertions.equipos_assertions import AssertionEquipos
from src.assertions.schema_assertions import AssertionSchemas
from src.espocrm_api.endpoint import Endpoint
from src.resources.authentications.authentication import Authentication


def test_lista_equipos_con_datos_exitoso(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTA_EQUIPOS(), 'GET')
    AssertionEquipos().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_lista_schema_file(response.json())


def test_lista_equipos_sin_datos_exitoso(get_headers):
    response = Authentication().authenticate_sin_equipo(get_headers, Endpoint.LISTA_EQUIPOS(), 'GET')
    AssertionEquipos().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_lista_schema_file(response.json())
    AssertionEquipos().assert_empty_list(response.json(), "list")
    AssertionEquipos().assert_total_equals(response.json(), 0)


def test_lista_equipos_sin_select(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTA_EQUIPOS(select=None), 'GET')
    AssertionEquipos().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_sin_select_schema_file(response.json())


def test_lista_equipos_autenficacion_invalida(get_headers):
    response = Authentication().authenticate_invalid_user(get_headers, Endpoint.LISTA_EQUIPOS(), 'GET')
    AssertionEquipos().assert_status_code(response, 401)
    AssertionEquipos().assert_response_vacio(response.text)


def test_lista_equipos_select_desconocido(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTA_EQUIPOS(select="unknown"), 'GET')
    AssertionEquipos().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_lista_schema_file(response.json())


def test_lista_equipos_sin_autorizacion(get_headers):
    response = Authentication().authenticate_no_authorization_equipos(get_headers, Endpoint.LISTA_EQUIPOS(), 'GET')
    AssertionEquipos().assert_status_code(response, 403)
    AssertionEquipos().assert_response_vacio(response.text)


def test_lista_equipos_maxsize_mayor_al_total(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTA_EQUIPOS(maxSize=200), 'GET')
    AssertionEquipos().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_lista_schema_file(response.json())


def test_lista_equipos_offser_mayor_al_total(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTA_EQUIPOS(offset=200), 'GET')
    AssertionEquipos().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_lista_schema_file(response.json())
    AssertionEquipos().assert_empty_list(response.json(), "list")


def test_lista_equipos_orden_asc(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTA_EQUIPOS(order='asc'), 'GET')
    AssertionEquipos().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_lista_schema_file(response.json())
    AssertionEquipos().assert_check_orden(response.json(), 'asc')


def test_lista_equipos_orden_desc(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTA_EQUIPOS(order='desc'), 'GET')
    AssertionEquipos().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_lista_schema_file(response.json())
    AssertionEquipos().assert_check_orden(response.json(), 'desc')


def test_lista_equipos_maxsize_cero(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTA_EQUIPOS(maxSize=0), 'GET')
    AssertionEquipos().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_lista_schema_file(response.json())
    AssertionEquipos().assert_empty_list(response.json(), 'list')


def test_lista_equipos_maxsize_negative(get_headers):
    # Status code esperado 400 bad request
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTA_EQUIPOS(maxSize=-1), 'GET')
    AssertionEquipos().assert_status_code(response, 500)
    AssertionEquipos().assert_response_vacio(response.text)


def test_lista_equipos_maxsize_string(get_headers):
    # Status code esperado 400 bad request
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTA_EQUIPOS(maxSize="string"), 'GET')
    AssertionEquipos().assert_status_code(response, 200)
