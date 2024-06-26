import requests
import pytest
from config import BASE_URI
def test_login_valido(get_headers):
    url = f'{BASE_URI}/App/user'
    headers = get_headers("junior", "junior1")
    response = requests.get(url, headers=headers)
    assert response.status_code == 200

def test_login_invalido(get_headers):
    url = f'{BASE_URI}/App/user'
    headers = get_headers("incorrecto", "incorrecto")
    response = requests.get(url, headers=headers)
    assert response.status_code == 401

def test_login_usuario_deshabilitado(get_headers):
    url = f'{BASE_URI}/App/user'
    headers = get_headers("hola", "hola")
    response = requests.get(url, headers=headers)
    assert response.status_code == 401

def test_login_usuario_incorrecta(get_headers):
    url = f'{BASE_URI}/App/user'
    headers = get_headers("incorrecto", "junior1")
    response = requests.get(url, headers=headers)
    assert response.status_code == 401
def test_login_contraseña_incorrecta(get_headers):
    url = f'{BASE_URI}/App/user'
    headers = get_headers("junior", "incorrecto")
    response = requests.get(url, headers=headers)
    assert response.status_code == 401

def test_login_campos_vacios(get_headers):
    url = f'{BASE_URI}/App/user'
    headers = get_headers("", "")
    response = requests.get(url, headers=headers)
    assert response.status_code == 401

def test_login_usuario_vacio(get_headers):
    url = f'{BASE_URI}/App/user'
    headers = get_headers("", "junior")
    response = requests.get(url, headers=headers)
    assert response.status_code == 401

def test_login_contraseña_vacia(get_headers):
    url = f'{BASE_URI}/App/user'
    headers = get_headers("junior", "")
    response = requests.get(url, headers=headers)
    assert response.status_code == 401
