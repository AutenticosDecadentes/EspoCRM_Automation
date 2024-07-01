import pytest
from src.assertions.schema_assertions import AssertionSchemas
from src.assertions.equipos_assertions import AssertionEquipos
from src.assertions.usuarios_assertions import AssertionUsuarios
from src.espocrm_api.endpoint import Endpoint
from src.resources.authentications.authentication import Authentication


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.smoke
def test_datos_por_defecto(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.EQUIPO_USUARIOS(), 'GET')
    AssertionSchemas().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_usuarios_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_max_size0(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.EQUIPO_USUARIOS(maxSize=0), 'GET')
    AssertionSchemas().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_usuarios_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_max_size_alto_mas_de_200(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.EQUIPO_USUARIOS(maxSize=201), 'GET')
    AssertionSchemas().assert_status_code(response, 403)
    AssertionSchemas().assert_response_vacio(response.text)


@pytest.mark.regression
@pytest.mark.functional
def test_max_size_alto_menos_de_200(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.EQUIPO_USUARIOS(maxSize=195), 'GET')
    AssertionSchemas().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_usuarios_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_max_size_negativo(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.EQUIPO_USUARIOS(maxSize=-15), 'GET')
    AssertionSchemas().assert_status_code(response, 500)
    AssertionSchemas().assert_response_vacio(response.text)


@pytest.mark.regression
@pytest.mark.functional
def test_max_size_negativo(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.EQUIPO_USUARIOS(maxSize="hola"), 'GET')
    AssertionSchemas().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_usuarios_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.smoke
def test_lista_equipos_usuarios_autenficacion_invalida(get_headers):
    response = Authentication().authenticate_invalid_user(get_headers, Endpoint.EQUIPO_USUARIOS(), 'GET')
    AssertionSchemas().assert_status_code(response, 401)
    AssertionSchemas().assert_response_vacio(response.text)


@pytest.mark.regression
@pytest.mark.functional
def test_lista_equipos_usuarios_orden_asc(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.EQUIPO_USUARIOS(order='asc'), 'GET')
    AssertionSchemas().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_usuarios_schema_file(response.json())
    AssertionUsuarios().assert_check_orden_asc(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_lista_equipos_usuarios_orden_desc(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.EQUIPO_USUARIOS(order='desc'), 'GET')
    AssertionSchemas().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_usuarios_schema_file(response.json())
    AssertionUsuarios().assert_check_orden_desc(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_lista_equipos_usuarios_ordenBy_vacio(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.EQUIPO_USUARIOS(orderBy=''), 'GET')
    AssertionSchemas().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_usuarios_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_lista_equipos_usuarios_ordenBy_null(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.EQUIPO_USUARIOS(orderBy="null"), 'GET')
    AssertionSchemas().assert_status_code(response, 400)
    try:
        AssertionUsuarios().assert_empty_list(response.json())
    except ValueError:  # Manejar error de decodificación JSON
        AssertionSchemas().assert_response_vacio(response.text)
