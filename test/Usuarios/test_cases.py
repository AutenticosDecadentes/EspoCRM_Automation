import requests
import pytest
from config import BASE_URI
from conftest import get_headers
from src.assertions.usuarios_assertions import AssertionUsuarios
from src.assertions.schema_assertions import AssertionSchemas
from src.espocrm_api.api_request import EspocrmRequest



def test_buscar_usuario_por_nombre_valido(get_headers):
    url = f'{BASE_URI}/User?where%5B0%5D%5Btype%5D=textFilter&where%5B0%5D%5Bvalue%5D=diego'
    headers = get_headers("diego", "zlM23bQzWm")
    response = EspocrmRequest().get(url, headers=headers)
    AssertionUsuarios.assert_status_code(response, 200)
    AssertionSchemas.assert_usuarios_buscar_schema_file(response.json())



def test_buscar_usuario_por_apellido_encontrado(get_headers):
    headers = get_headers("diego", "zlM23bQzWm")
    url = f'{BASE_URI}/User?where%5B0%5D%5Btype%5D=textFilter&where%5B0%5D%5Bvalue%5D=Montano'
    response = EspocrmRequest().get(url, headers=headers)
    AssertionUsuarios.assert_status_code(response, 200)
    AssertionSchemas.assert_usuarios_buscar_schema_file(response.json())


def test_buscar_usuario_por_username_encontrado(get_headers):
    headers = get_headers("diego", "zlM23bQzWm")
    url = f'{BASE_URI}/User?where%5B0%5D%5Btype%5D=textFilter&where%5B0%5D%5Bvalue%5D=hola'
    response = EspocrmRequest().get(url, headers=headers)
    AssertionUsuarios.assert_status_code(response, 200)
    AssertionSchemas.assert_usuarios_buscar_schema_file(response.json())


def test_buscar_usuario_por_email_encontrado(get_headers):
    headers = get_headers("diego", "zlM23bQzWm")
    url = f'{BASE_URI}/User?where%5B0%5D%5Btype%5D=textFilter&where%5B0%5D%5Bvalue%5D=201604461@est.umss'
    response = EspocrmRequest().get(url, headers=headers)
    AssertionUsuarios.assert_status_code(response, 200)
    AssertionSchemas.assert_usuarios_buscar_schema_file(response.json())


def test_buscar_usuario_por_nombre_no_valido(get_headers):
    headers = get_headers("diego", "zlM23bQzWm")
    url = f'{BASE_URI}/User?where%5B0%5D%5Btype%5D=textFilter&where%5B0%5D%5Bvalue%5D=mnbmbmbjkhghjjjg'
    response = EspocrmRequest().get(url, headers=headers)
    AssertionUsuarios.assert_status_code(response, 200)
    AssertionSchemas.assert_usuarios_buscar_schema_file(response.json())


def test_buscar_usuario_por_apellido_no_valido(get_headers):
    headers = get_headers("diego", "zlM23bQzWm")
    url = f'{BASE_URI}/User?where%5B0%5D%5Btype%5D=textFilter&where%5B0%5D%5Bvalue%5D=apellido_no_valido'
    response = EspocrmRequest().get(url, headers=headers)
    AssertionUsuarios.assert_status_code(response, 200)
    AssertionSchemas.assert_usuarios_buscar_schema_file(response.json())


def test_buscar_usuario_por_username_no_valido(get_headers):
    headers = get_headers("diego", "zlM23bQzWm")
    url = f'{BASE_URI}/User?where%5B0%5D%5Btype%5D=textFilter&where%5B0%5D%5Bvalue%5D=username_no_valido'
    response = EspocrmRequest().get(url, headers=headers)
    AssertionUsuarios.assert_status_code(response, 200)
    AssertionSchemas.assert_usuarios_buscar_schema_file(response.json())


def test_buscar_usuario_por_email_no_valido(get_headers):
    headers = get_headers("diego", "zlM23bQzWm")
    url = f'{BASE_URI}/User?where%5B0%5D%5Btype%5D=textFilter&where%5B0%5D%5Bvalue%5D=email_no_valido'
    response = EspocrmRequest().get(url, headers=headers)
    AssertionUsuarios.assert_status_code(response, 200)
    AssertionSchemas.assert_usuarios_buscar_schema_file(response.json())


def test_buscar_usuario_campo_vacio(get_headers):
    headers = get_headers("diego", "zlM23bQzWm")
    url = f'{BASE_URI}/User?where%5B0%5D%5Btype%5D=textFilter&where%5B0%5D%5Bvalue%5D='
    response = EspocrmRequest().get(url, headers=headers)
    AssertionUsuarios.assert_status_code(response, 200)
    AssertionSchemas.assert_usuarios_buscar_schema_file(response.json())

# Functionaltest

def test_buscar_usuario_por_username_encontrado(get_headers):
    headers = get_headers("diego", "zlM23bQzWm")
    url = f'{BASE_URI}/User?where%5B0%5D%5Btype%5D=textFilter&where%5B0%5D%5Bvalue%5D=username_encontrado'
    response = EspocrmRequest().get(url, headers=headers)
    AssertionUsuarios.assert_status_code(response, 200)
    AssertionSchemas.assert_usuarios_buscar_schema_file(response.json())


def test_buscar_usuario_por_username_no_valido(get_headers):
    headers = get_headers("diego", "zlM23bQzWm")
    url = f'{BASE_URI}/User?where%5B0%5D%5Btype%5D=textFilter&where%5B0%5D%5Bvalue%5D=username_no_valido'
    response = EspocrmRequest().get(url, headers=headers)
    AssertionUsuarios.assert_status_code(response, 200)
    AssertionSchemas.assert_usuarios_buscar_schema_file(response.json())


def test_buscar_usuario_campo_vacio(get_headers):
    headers = get_headers("diego", "zlM23bQzWm")
    url = f'{BASE_URI}/User?where%5B0%5D%5Btype%5D=textFilter&where%5B0%5D%5Bvalue%5D=""'
    response = EspocrmRequest().get(url, headers=headers)
    AssertionUsuarios.assert_status_code(response, 200)
    AssertionSchemas.assert_usuarios_buscar_schema_file(response.json())

def test_buscar_usuario_con_login_invalido(get_headers):
    url = f'{BASE_URI}/User?where%5B0%5D%5Btype%5D=textFilter&where%5B0%5D%5Bvalue%5D=diego'
    headers = get_headers("incorrecto", "incorrecto")
    response = EspocrmRequest().get(url, headers=headers)
    AssertionUsuarios.assert_status_code(response, 401)