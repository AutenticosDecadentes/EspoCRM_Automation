import requests
import pytest
from config import BASE_URI
from src.assertions.usuarios_assertions import AssertionUsuarios
from src.assertions.schema_assertions import AssertionSchemas
from src.espocrm_api.api_request import EspocrmRequest
from src.espocrm_api.endpoint import Endpoint

def test_lista_usuarios_con_datos_exitoso(get_headers):
    url = f'{BASE_URI}{Endpoint.LISTA_USUARIOS.value}'
    headers = get_headers("nicol", "r17yKfBBLL")
    response = EspocrmRequest().get(url, headers=headers)
    AssertionUsuarios().assert_status_code(response, 200)


def test_lista_usuarios_requiere_autenticacion():
    url = f'{BASE_URI}{Endpoint.LISTA_USUARIOS.value}'
    response = EspocrmRequest().get(url)
    AssertionUsuarios().assert_status_code(response, 401)


def test_lista_usuarios_orden_descendente(get_headers):
    url = f'{BASE_URI}{Endpoint.LISTA_USUARIOS_DESC.value}'
    headers = get_headers("nicol", "r17yKfBBLL")
    response = EspocrmRequest().get(url, headers=headers)

    # Assertions
    AssertionUsuarios().assert_status_code(response, 200)
    AssertionUsuarios().assert_check_orden_desc(response.json())


def test_lista_usuarios_orden_ascendente(get_headers):
    url = f'{BASE_URI}{Endpoint.LISTA_USUARIOS_ASC.value}'
    headers = get_headers("nicol", "r17yKfBBLL")
    response = EspocrmRequest().get(url, headers=headers)

    # Assertions
    AssertionUsuarios().assert_status_code(response, 200)
    AssertionUsuarios().assert_check_orden_asc(response.json())


def test_lista_usuarios_lista_vacia(get_headers):
    url = f'{BASE_URI}{Endpoint.LISTA_USUARIOS_VACIA.value}'
    headers = get_headers("nicol", "r17yKfBBLL")
    response = EspocrmRequest().get(url, headers=headers)

    # Assertions
    AssertionUsuarios().assert_status_code(response, 200)
    AssertionUsuarios().assert_empty_list(response.json())

def test_lista_usuarios_campos_especificados(get_headers):
    url = f'{BASE_URI}{Endpoint.LISTA_USUARIOS.value}'
    headers = get_headers("nicol", "r17yKfBBLL")
    response = EspocrmRequest().get(url, headers=headers)
    # Assertions
    AssertionUsuarios().assert_status_code(response, 200)
    AssertionUsuarios().assert_campos_especificados(response.json())


def test_lista_usuarios_total(get_headers):
    url = f'{BASE_URI}{Endpoint.LISTA_USUARIOS.value}'
    headers = get_headers("nicol", "r17yKfBBLL")

    response = EspocrmRequest().get(url, headers=headers)

    # Assertions
    AssertionUsuarios().assert_status_code(response, 200)
    AssertionUsuarios().assert_total(response.json())