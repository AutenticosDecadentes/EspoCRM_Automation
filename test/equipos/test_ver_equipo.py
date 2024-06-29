import requests
import pytest
from config import BASE_URI
from src.assertions.equipos_assertions import AssertionEquipos
from src.espocrm_api.api_request import EspocrmRequest
from src.espocrm_api.endpoint import Endpoint

def test_ver_equipo_correcto(get_headers): #
    url = f'{BASE_URI}{Endpoint.VER_EQUIPOS.value}'
    headers = get_headers("admin", "admin")
    response = requests.get(url, headers=headers)
    AssertionEquipos().asser_status_code(response,200)
    # assert response.status_code == 200

def test_ver_equipo_headers_adicionales(get_headers): #52
    url = f'{BASE_URI}{Endpoint.VER_EQUIPOS.value}'
    headers = get_headers("admin", "admin")
    headers["header_extra"] = "valor_extra"
    response = EspocrmRequest().get(url, headers=headers)
    AssertionEquipos().asser_status_code(response, 200)


def test_ver_equipo_metodo_http_incorrecto(get_headers): #51
    url = f'{BASE_URI}{Endpoint.VER_EQUIPOS.value}'
    headers = get_headers("admin", "admin")
    response = requests.post(url, headers=headers)
    AssertionEquipos().asser_status_code(response, 405)


def test_ver_equipo_correcto(get_headers): #46 revisar
    url = f'{BASE_URI}{Endpoint.VER_EQUIPOS.value}'
    headers = get_headers("admin", "admin")
    response = requests.get(url, headers=headers)
    AssertionEquipos().asser_status_code(response, 200)


def test_ver_equipo_autorizacion_incorrecta(get_headers): #48
    url = f'{BASE_URI}{Endpoint.VER_EQUIPOS.value}'
    headers = get_headers("incorrecto", "incorrecto")
    response = requests.get(url, headers=headers)
    AssertionEquipos().asser_status_code(response, 401)


def test_ver_equipo_sin_autorizacion(get_headers): #47
    url = f'{BASE_URI}{Endpoint.VER_EQUIPOS.value}'
    headers = get_headers("", "")
    response = requests.get(url, headers=headers)
    AssertionEquipos().asser_status_code(response, 401)


def test_ver_equipo_id_no_existe(get_headers): #49
    url = f'{BASE_URI}/Team/id_no_existente'
    headers = get_headers("admin", "admin")
    response = requests.get(url, headers=headers)
    AssertionEquipos().asser_status_code(response, 404)


def test_ver_equipo_id_formato_incorrecto(get_headers): #
    url = f'{BASE_URI}/Team/formatoIncorrecto'
    headers = get_headers("admin", "admin")
    response = requests.get(url, headers=headers)
    AssertionEquipos().asser_status_code(response, 404)


