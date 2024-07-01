import requests
import pytest

from src.assertions.usuarios_assertions import AssertionUsuarios
from src.assertions.schema_assertions import AssertionSchemas
from src.espocrm_api.endpoint import Endpoint
from src.resources.authentications.authentication import Authentication

def test_buscar_usuario_por_nombre_valido(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.BUSCAR_USUARIOS(where="darwin"), 'GET')
    AssertionUsuarios().assert_status_code(response, 200)
    AssertionSchemas().assert_usuarios_buscar_schema_file(response.json())

def test_buscar_usuario_por_apellido_encontrado(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.BUSCAR_USUARIOS(where="Montano"), 'GET')
    AssertionUsuarios().assert_status_code(response, 200)
    AssertionSchemas().assert_usuarios_buscar_schema_file(response.json())

def test_buscar_usuario_por_username_encontrado(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.BUSCAR_USUARIOS(where="hola"), 'GET')
    AssertionUsuarios().assert_status_code(response, 200)
    AssertionSchemas().assert_usuarios_buscar_schema_file(response.json())

def test_buscar_usuario_por_email_encontrado(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.BUSCAR_USUARIOS(where="201604461@est.umss"), 'GET')
    AssertionUsuarios().assert_status_code(response, 200)
    AssertionSchemas().assert_usuarios_buscar_schema_file(response.json())

def test_buscar_usuario_por_email_encontrado(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.BUSCAR_USUARIOS(where="mnbmbmbjkhghjjjg"), 'GET')
    AssertionUsuarios().assert_status_code(response, 200)
    AssertionSchemas().assert_usuarios_buscar_schema_file(response.json())

def test_buscar_usuario_por_email_encontrado(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.BUSCAR_USUARIOS(where="apellido_no_valido"), 'GET')
    AssertionUsuarios().assert_status_code(response, 200)
    AssertionSchemas().assert_usuarios_buscar_schema_file(response.json())

def test_buscar_usuario_por_email_encontrado(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.BUSCAR_USUARIOS(where="username_no_valido"), 'GET')
    AssertionUsuarios().assert_status_code(response, 200)
    AssertionSchemas().assert_usuarios_buscar_schema_file(response.json())

def test_buscar_usuario_por_username_no_valido(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.BUSCAR_USUARIOS(where="username_no_valido"), 'GET')
    AssertionUsuarios().assert_status_code(response, 200)
    AssertionSchemas().assert_usuarios_buscar_schema_file(response.json())

def test_buscar_usuario_por_email_no_valido(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.BUSCAR_USUARIOS(where="email_no_valido"), 'GET')
    AssertionUsuarios().assert_status_code(response, 200)
    AssertionSchemas().assert_usuarios_buscar_schema_file(response.json())

def test_buscar_usuario_campo_vacio(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.BUSCAR_USUARIOS(where=""), 'GET')
    AssertionUsuarios().assert_status_code(response, 200)
    AssertionSchemas().assert_usuarios_buscar_schema_file(response.json())


def test_buscar_usuario_con_login_invalido(get_headers):
    response = Authentication().authenticate_invalid_user(get_headers,  Endpoint.BUSCAR_USUARIOS(where="diego"), 'GET')
    AssertionUsuarios().assert_status_code(response, 401)
    AssertionUsuarios().assert_response_vacio(response.text)