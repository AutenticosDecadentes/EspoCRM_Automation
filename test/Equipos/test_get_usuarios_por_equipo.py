import requests
import pytest
from jsonschema import validate
from config import BASE_URI
from src.schemas.equipo_usuario_schema import meeting_schema
from src.schemas.endpoints.endpoints import build_url, Endpoint


def test_datos_por_defecto(get_headers):
    url = build_url(BASE_URI)
    headers = get_headers("admin", "admin")
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    validate(instance=response.json(), schema=meeting_schema)


def test_max_size0(get_headers):
    url = build_url(BASE_URI, max_size=0)
    headers = get_headers("admin", "admin")
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    validate(instance=response.json(), schema=meeting_schema)


def test_max_size_alto_mas_de_200(get_headers):
    url = build_url(BASE_URI, max_size=201)
    headers = get_headers("admin", "admin")
    response = requests.get(url, headers=headers)
    assert response.status_code == 403
    if response.headers.get('Content-Type') == 'application/json' and response.text:
        validate(instance=response.json(), schema=meeting_schema)
    else:
        assert response.text == ''


def test_max_size_alto_menos_de_200(get_headers):
    url = build_url(BASE_URI, max_size=195)
    headers = get_headers("admin", "admin")
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    validate(instance=response.json(), schema=meeting_schema)