from conftest import get_headers
from src.assertions.equipos_assertions import AssertionEquipos
from src.assertions.schema_assertions import AssertionSchemas
from src.espocrm_api.endpoint import Endpoint
from src.resources.authentications.authentication import Authentication


def test_datos_por_defecto(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.EQUIPO_USUARIOS(), 'GET')
    AssertionEquipos().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_usuarios_schema_file(response.json())

def test_max_size0(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.EQUIPO_USUARIOS(maxSize=0), 'GET')
    AssertionEquipos().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_usuarios_schema_file(response.json())



def test_max_size_alto_mas_de_200(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.EQUIPO_USUARIOS(maxSize=201), 'GET')
    AssertionEquipos().assert_status_code(response, 403)
    AssertionEquipos().assert_response_vacio(response.text)


def test_max_size_alto_menos_de_200(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.EQUIPO_USUARIOS(maxSize=195), 'GET')
    AssertionEquipos().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_usuarios_schema_file(response.json())

def test_max_size_negativo(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.EQUIPO_USUARIOS(maxSize=-15), 'GET')
    AssertionEquipos().assert_status_code(response, 500)
    AssertionEquipos().assert_response_vacio(response.text)

def test_max_size_negativo(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.EQUIPO_USUARIOS(maxSize="hola"), 'GET')
    AssertionEquipos().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_usuarios_schema_file(response.json())

def test_lista_equipos_usuarios_autenficacion_invalida(get_headers):
    response = Authentication().authenticate_invalid_user(get_headers, Endpoint.EQUIPO_USUARIOS(), 'GET')
    AssertionEquipos().assert_status_code(response, 401)
    AssertionEquipos().assert_response_vacio(response.text)

def test_lista_equipos_usuarios_orden_asc(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.EQUIPO_USUARIOS(order='asc'), 'GET')
    AssertionEquipos().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_usuarios_schema_file(response.json())


def test_lista_equipos_usuarios_orden_desc(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.EQUIPO_USUARIOS(order='desc'), 'GET')
    AssertionEquipos().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_usuarios_schema_file(response.json())

def test_lista_equipos_usuarios_ordenBy_vacio(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.EQUIPO_USUARIOS(orderBy=''), 'GET')
    AssertionEquipos().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_usuarios_schema_file(response.json())

def test_lista_equipos_usuarios_ordenBy_null(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.EQUIPO_USUARIOS(orderBy="null"), 'GET')
    AssertionEquipos().assert_status_code(response, 400)
    AssertionEquipos().assert_response_vacio(response.text)