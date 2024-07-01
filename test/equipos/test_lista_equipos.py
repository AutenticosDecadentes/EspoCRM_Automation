import pytest
from src.assertions.equipos_assertions import AssertionEquipos
from src.assertions.schema_assertions import AssertionSchemas
from src.espocrm_api.endpoint import Endpoint
from src.resources.authentications.authentication import Authentication

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.functional
def test_lista_equipos_con_datos_exitoso(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTA_EQUIPOS(), 'GET')
    AssertionSchemas().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_lista_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_lista_equipos_order_asc(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTA_EQUIPOS(order='asc'), 'GET')
    AssertionSchemas().assert_status_code(response, 200)
    AssertionEquipos().assert_check_orden(response.json(), 'asc')

@pytest.mark.regression
@pytest.mark.functional
def test_lista_equipos_orden_asc(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTA_EQUIPOS(order='asc'), 'GET')
    AssertionSchemas().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_lista_schema_file(response.json())
    AssertionEquipos().assert_check_orden(response.json(), 'asc')

@pytest.mark.regression
@pytest.mark.functional
def test_lista_equipos_orden_desc(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTA_EQUIPOS(order='desc'), 'GET')
    AssertionSchemas().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_lista_schema_file(response.json())
    AssertionEquipos().assert_check_orden(response.json(), 'desc')

@pytest.mark.regression
@pytest.mark.functional
def test_lista_equipos_sin_datos_exitoso(get_headers):
    response = Authentication().authenticate_sin_equipo(get_headers, Endpoint.LISTA_EQUIPOS(), 'GET')
    AssertionSchemas().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_lista_schema_file(response.json())
    AssertionSchemas().assert_empty_list(response.json(), "list")
    AssertionSchemas().assert_total_equals(response.json(), 0)

@pytest.mark.regression
@pytest.mark.functional
def test_lista_equipos_sin_select(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTA_EQUIPOS(select=None), 'GET')
    AssertionSchemas().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_sin_select_schema_file(response.json())

@pytest.mark.regression
@pytest.mark.functional
def test_lista_equipos_select_desconocido(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTA_EQUIPOS(select="unknown"), 'GET')
    AssertionSchemas().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_lista_schema_file(response.json())

@pytest.mark.regression
@pytest.mark.functional
def test_lista_equipos_select_especiales(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTA_EQUIPOS(select="***"), 'GET')
    AssertionSchemas().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_lista_schema_file(response.json())
    AssertionSchemas().assert_list_no_empty(response.json())

@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.smoke
def test_lista_equipos_autenficacion_invalida(get_headers):
    response = Authentication().authenticate_invalid_user(get_headers, Endpoint.LISTA_EQUIPOS(), 'GET')
    AssertionSchemas().assert_status_code(response, 401)
    AssertionSchemas().assert_response_vacio(response.text)

@pytest.mark.regression
@pytest.mark.functional
def test_lista_equipos_sin_autorizacion(get_headers):
    response = Authentication().authenticate_no_authorization_equipos(get_headers, Endpoint.LISTA_EQUIPOS(), 'GET')
    AssertionSchemas().assert_status_code(response, 403)
    AssertionSchemas().assert_response_vacio(response.text)

@pytest.mark.regression
@pytest.mark.functional
def test_lista_equipos_maxsize_mayor_al_total(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTA_EQUIPOS(maxSize=200), 'GET')
    AssertionSchemas().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_lista_schema_file(response.json())

@pytest.mark.regression
@pytest.mark.functional
def test_lista_equipos_maxsize_cero(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTA_EQUIPOS(maxSize=0), 'GET')
    AssertionSchemas().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_lista_schema_file(response.json())
    AssertionSchemas().assert_empty_list(response.json(), 'list')

@pytest.mark.regression
@pytest.mark.functional
def test_lista_equipos_maxsize_negative(get_headers):
    # Status code esperado 400 bad request
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTA_EQUIPOS(maxSize=-1), 'GET')
    AssertionSchemas().assert_status_code(response, 500)
    AssertionSchemas().assert_response_vacio(response.text)

@pytest.mark.regression
@pytest.mark.functional
def test_lista_equipos_maxsize_string(get_headers):
    # Status code esperado 400 bad request
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTA_EQUIPOS(maxSize="string"), 'GET')
    AssertionSchemas().assert_status_code(response, 200)

@pytest.mark.regression
@pytest.mark.functional
def test_lista_equipos_offser_mayor_al_total(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTA_EQUIPOS(offset=200), 'GET')
    AssertionSchemas().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_lista_schema_file(response.json())
    AssertionSchemas().assert_empty_list(response.json(), "list")

@pytest.mark.regression
@pytest.mark.functional
def test_lista_equipos_offset_cero(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTA_EQUIPOS(offset=0), 'GET')
    AssertionSchemas().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_lista_schema_file(response.json())

@pytest.mark.regression
@pytest.mark.functional
def test_lista_equipos_offset_negative(get_headers):
    # Status code esperado 400 bad request
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTA_EQUIPOS(offset=-1), 'GET')
    AssertionSchemas().assert_status_code(response, 500)
    AssertionSchemas().assert_response_vacio(response.text)

@pytest.mark.regression
@pytest.mark.functional
def test_lista_equipos_offset_string(get_headers):
    # Status code esperado 400 bad request
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTA_EQUIPOS(offset="string"), 'GET')
    AssertionSchemas().assert_status_code(response, 200)

@pytest.mark.regression
@pytest.mark.functional
def test_lista_equipos_ordeby_desconocido(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.LISTA_EQUIPOS(orderBy='unknown'), 'GET')
    AssertionSchemas().assert_status_code(response, 400)
    AssertionSchemas().assert_response_vacio(response.text)
