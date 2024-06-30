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
