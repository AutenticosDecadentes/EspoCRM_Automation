import requests
import pytest
from config import BASE_URI
from src.assertions.equipos_assertions import assert_json_schema, assert_status_code, assert_empty_list, \
    assert_total_equals
from src.schemas.equipo_schema import equipo_lista_schema, schema_sin_select


def test_lista_equipos_con_datos_exitoso(get_headers):
    """
    Prueba para verificar que se obtiene correctamente la lista de equipos con datos.
    """
    url = f'{BASE_URI}/Team?select=name&maxSize=2&offset=0&order=asc'
    headers = get_headers("admin", "admin")
    response = requests.get(url, headers=headers)
    response_json = response.json()
    assert_json_schema(response_json, equipo_lista_schema)
    assert_status_code(response, 200)


def test_lista_equipos_sin_datos_exitoso(get_headers):
    """
    Prueba para verificar que la lista de equipos está vacía cuando no hay equipos.
    """
    url = f'{BASE_URI}/Team?select=name&maxSize=2&offset=0&order=asc'
    headers = get_headers("sinequipos", "password")
    response = requests.get(url, headers=headers)
    response_json = response.json()
    assert_status_code(response, 200)
    assert_json_schema(response_json, equipo_lista_schema)
    assert_empty_list(response_json, "list")
    assert_total_equals(response_json, 0)


def test_lista_equipos_sin_select(get_headers):
    """
    Prueba para verificar que la respuesta sin parámetros de selección
    cumple con el esquema y que el endpoint devuelve una lista de equipos válida.
    """
    url = f'{BASE_URI}/Team?maxSize=2&offset=0&order=asc'
    headers = get_headers("chars_dar", "password")
    response = requests.get(url, headers=headers)
    response_json = response.json()
    assert_status_code(response, 200)
    assert_json_schema(response_json, schema_sin_select)
