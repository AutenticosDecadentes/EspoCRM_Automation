import pytest
from src.assertions.equipos_assertions import AssertionEquipos
from src.assertions.schema_assertions import AssertionSchemas
from src.espocrm_api.endpoint import Endpoint
from src.resources.authentications.authentication import Authentication
from src.espocrm_api.api_request import EspocrmRequest
import requests


@pytest.mark.regression
@pytest.mark.functional
def test_ver_equipo_headers_adicionales(get_headers):  # 52
    url = f'https://espo.spartan-soft.com/api/v1{Endpoint.VER_EQUIPOS.value}'
    headers = get_headers("admin", "admin")
    headers["header_extra"] = "valor_extra"
    response = EspocrmRequest().get(url, headers=headers)
    # response = Authentication().authenticate_valid_user(get_headers, Endpoint.VER_EQUIPOS.value, 'GET')
    AssertionSchemas().assert_status_code(response, 200)
    AssertionSchemas().assert_ver_equipo_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_ver_equipo_metodo_http_incorrecto(get_headers):  # 51
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.VER_EQUIPOS.value, 'POST')
    AssertionSchemas().assert_status_code(response, 405)


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.smoke
def test_ver_equipo_correcto(get_headers):  # 46 revisar
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.VER_EQUIPOS.value, 'GET')
    AssertionSchemas().assert_status_code(response, 200)
    AssertionSchemas().assert_ver_equipo_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_ver_equipo_autorizacion_incorrecta(get_headers):  # 48
    response = Authentication().authenticate_invalid_user(get_headers, Endpoint.VER_EQUIPOS.value, 'GET')
    AssertionSchemas().assert_status_code(response, 401)


@pytest.mark.regression
@pytest.mark.functional
def test_ver_equipo_sin_autorizacion(get_headers):  # 47
    response = Authentication().authenticate_user_empty(get_headers, Endpoint.VER_EQUIPOS.value, 'GET')
    AssertionSchemas().assert_status_code(response, 401)


@pytest.mark.regression
@pytest.mark.functional
def test_ver_equipo_id_no_existe(get_headers):  # 49
    response = Authentication().authenticate_valid_user(get_headers,
                                                        'https://espo.spartan-soft.com/api/v1/Team/id_no_existente',
                                                        'GET')
    AssertionSchemas().assert_status_code(response, 404)


@pytest.mark.regression
@pytest.mark.functional
def test_ver_equipo_id_formato_incorrecto(get_headers):  #
    response = Authentication().authenticate_valid_user(get_headers,
                                                        'https://espo.spartan-soft.com/api/v1/Team/formatoIncorrecto',
                                                        'GET')
    AssertionSchemas().assert_status_code(response, 404)
