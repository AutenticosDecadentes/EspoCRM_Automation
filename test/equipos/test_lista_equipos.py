import pytest
from config import BASE_URI
from src.assertions.equipos_assertions import assert_status_code,assert_empty_list,assert_total_equals
from src.assertions.schema_assertions import assert_equipo_sin_select_schema_file, assert_equipo_lista_schema_file
from src.espocrm_api.api_request import EspocrmRequest
from src.espocrm_api.endpoint import Endpoint


def test_lista_equipos_con_datos_exitoso(get_headers):
    url = f'{BASE_URI}{Endpoint.LISTA_EQUIPOS.value}'
    headers = get_headers("admin", "admin")
    response = EspocrmRequest().get(url, headers=headers)
    assert_status_code(response, 200)
    assert_equipo_lista_schema_file(response.json())

def test_lista_equipos_sin_datos_exitoso(get_headers):
    url = f'{BASE_URI}{Endpoint.LISTA_EQUIPOS.value}'
    headers = get_headers("sinequipos", "password")
    response = EspocrmRequest().get(url, headers=headers)
    assert_status_code(response, 200)
    assert_equipo_lista_schema_file(response.json())
    assert_empty_list(response.json(), "list")
    assert_total_equals(response.json(), 0)

def test_lista_equipos_sin_select(get_headers):
    url = f'{BASE_URI}{Endpoint.LISTA_EQUIPOS_SIN_SELECT.value}'
    headers = get_headers("chars_dar", "password")
    response = EspocrmRequest().get(url, headers=headers)
    assert_status_code(response, 200)
    assert_equipo_sin_select_schema_file(response.json())

def test_lista_equipos_autenficacion_invalida(get_headers):
    url = f'{BASE_URI}{Endpoint.LISTA_EQUIPOS.value}'
    headers = get_headers("chars_dar", "incorrecto")
    response = EspocrmRequest().get(url, headers=headers)
    assert_status_code(response, 401)
