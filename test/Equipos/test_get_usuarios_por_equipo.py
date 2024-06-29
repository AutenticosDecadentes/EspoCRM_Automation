import requests
import pytest
from jsonschema import validate
from config import BASE_URI
from src.schemas.equipo_usuario_schema import meeting_schema


def test_datos_por_defecto(get_headers):
    url = (f'{BASE_URI}/Team/667594ac5470f5dc3/users?primaryFilter=&select=teamRole%2CuserName%2CsalutationName'
           f'%2CfirstName%2ClastName%2CmiddleName%2Cname&maxSize=5&offset=0&orderBy=userName&order=asc')
    headers = get_headers("admin", "admin")
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    validate(instance=response.json(), schema=meeting_schema)


def test_max_size0(get_headers):
    url = (f'{BASE_URI}/Team/667594ac5470f5dc3/users?maxSize=0')
    headers = get_headers("admin", "admin")
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    validate(instance=response.json(), schema=meeting_schema)


def test_max_size_alto_mas_de_200(get_headers):
    url = (f'{BASE_URI}/Team/667594ac5470f5dc3/users?maxSize=201')
    headers = get_headers("admin", "admin")
    response = requests.get(url, headers=headers)
    assert response.status_code == 403
    if response.headers.get('Content-Type') == 'application/json' and response.text:
        validate(instance=response.json(), schema=meeting_schema)
    else:
        assert response.text == ''  # Verificar que la respuesta no tiene contenido


def test_max_size_alto_menos_de_200(get_headers):
    url = (f'{BASE_URI}/Team/667594ac5470f5dc3/users?maxSize=195')
    headers = get_headers("admin", "admin")
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    validate(instance=response.json(), schema=meeting_schema)