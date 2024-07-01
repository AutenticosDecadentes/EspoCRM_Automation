import requests
import pytest

from src.assertions.schema_assertions import AssertionSchemas
from src.espocrm_api.endpoint import Endpoint
from src.resources.authentications.authentication import Authentication

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.functional
def test_ordenacion_usuario_asc(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.ORDENAR_USUARIOS_ASC(), 'GET')
    AssertionSchemas().assert_status_code(response, 200)
    AssertionSchemas().assert_usuarios_orden_asc_schema_file(response.json())

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.functional
def test_ordenacion_usuario_desc(get_headers):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.ORDENAR_USUARIOS_DESC(), 'GET')
    AssertionSchemas().assert_status_code(response, 200)
    AssertionSchemas().assert_usuarios_orden_desc_schema_file(response.json())
    
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.functional
def test_usario_asc_credenciales_invalidas(get_headers):
    response = Authentication().authenticate_invalid_user(get_headers, Endpoint.ORDENAR_USUARIOS_ASC(), 'GET')
    AssertionSchemas().assert_status_code(response, 401)
    AssertionSchemas().assert_response_vacio(response.text)

@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.parametrize("maxSize", [5, 10, 15, 20, 25, 30])  # Aquí puedes ajustar los valores que desees probar
def test_tamano_lista_paginacion(get_headers, maxSize):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.ORDENAR_USUARIOS_ASC(maxSize=maxSize), 'GET')
    AssertionSchemas().assert_status_code(response, 200)  # Uso del método de aserción ya definido para el código de estado
    AssertionSchemas().assert_list_no_empty(response.json())  # Asegura que la lista no está vacía
    AssertionSchemas().assert_list_length_within_range(response.json(), max_len=maxSize)  # Verifica que el tamaño de la lista esté dentro del rango esperado

@pytest.mark.regression
@pytest.mark.functional
def test_parametros_order_by_invalido(get_headers):
    response = Authentication().authenticate_valid_user(get_headers,Endpoint.ORDENAR_USUARIOS_ASC(orderBy="campo_inexistente"),   'GET')
    AssertionSchemas().assert_status_code(response, 400)
    
@pytest.mark.regression
@pytest.mark.functional
def test_parametros_order_invalido(get_headers):
    response = Authentication().authenticate_valid_user(get_headers,Endpoint.ORDENAR_USUARIOS_ASC(order="campo_inexistente"),   'GET')
    AssertionSchemas().assert_status_code(response, 400)

@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.parametrize("orderBy", ['salutationName', 'middleName', 'emailAddress'])
def test_ordenacion_campos_opcionales(get_headers, orderBy):
    response = Authentication().authenticate_valid_user(get_headers, Endpoint.ORDENAR_USUARIOS_ASC(orderBy=orderBy), 'GET')
    AssertionSchemas().assert_status_code(response, 200)










