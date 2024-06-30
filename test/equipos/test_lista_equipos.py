import pytest
from src.assertions.equipos_assertions import AssertionEquipos
from src.assertions.schema_assertions import AssertionSchemas
from src.espocrm_api.endpoint import Endpoint
from src.resources.authentications.authentication import Authentication


def test_lista_equipos_con_datos_exitoso(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTA_EQUIPOS.value, 'GET')
    AssertionEquipos().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_lista_schema_file(response.json())


def test_lista_equipos_sin_datos_exitoso(get_headers):
    response = Authentication().authenticate_sin_equipo(get_headers, Endpoint.LISTA_EQUIPOS.value, 'GET')
    AssertionEquipos().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_lista_schema_file(response.json())
    AssertionEquipos().assert_empty_list(response.json(), "list")
    AssertionEquipos().assert_total_equals(response.json(), 0)


def test_lista_equipos_sin_select(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTA_EQUIPOS_SIN_SELECT.value, 'GET')
    AssertionEquipos().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_sin_select_schema_file(response.json())


def test_lista_equipos_autenficacion_invalida(get_headers):
    response = Authentication().authenticate_invalid_user(get_headers, Endpoint.LISTA_EQUIPOS.value, 'GET')
    AssertionEquipos().assert_status_code(response, 401)


def test_lista_equipos_select_desconocido(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTA_EQUIPOS_SELECT_DESCONOCIDO.value,
                                                        'GET')
    AssertionEquipos().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_lista_schema_file(response.json())


def test_lista_equipos_sin_autorizacion(get_headers):
    response = Authentication().authenticate_no_authorization_equipos(get_headers, Endpoint.LISTA_EQUIPOS.value, 'GET')
    AssertionEquipos().assert_status_code(response, 403)


def test_lista_equipos_maxsize_mayor_al_total(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTA_EQUIPOS_MAXSIZE_MAYOR_TOTAL.value,
                                                        'GET')
    AssertionEquipos().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_lista_schema_file(response.json())


def test_lista_equipos_offser_mayor_al_total(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTA_EQUIPOS_OFFSET_MAYOR_TOTAL.value,
                                                        'GET')
    AssertionEquipos().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_lista_schema_file(response.json())
    AssertionEquipos().assert_empty_list(response.json(), "list")


def test_lista_equipos_orden_asc(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTA_EQUIPOS_ORDEN_ASC.value, 'GET')
    AssertionEquipos().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_lista_schema_file(response.json())
    AssertionEquipos().assert_check_orden(response.json(), 'asc')


def test_lista_equipos_orden_desc(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTA_EQUIPOS_ORDEN_DESC.value, 'GET')
    AssertionEquipos().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_lista_schema_file(response.json())
    AssertionEquipos().assert_check_orden(response.json(), 'desc')
