import requests
import pytest
from config import BASE_URI
from src.assertions.schema_assertions import AssertionSchemas
from src.assertions.ordenamiento_assertions import AssertionOrdenamiento


def test_ordenacion_ascendente_alfanumericos (get_headers):
    url = f"{BASE_URI}/User?userType=internal&select=isActive,emailAddressIsOptedOut,emailAddressIsInvalid,emailAddress,emailAddressData,title,userName,salutationName,firstName,lastName,middleName,name&maxSize=20&offset=0&orderBy=name&order=asc"
    headers = get_headers("vianca", "p32qQb9MQo")
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    AssertionOrdenamiento.assert_comprobar_ordenamiento(response)
    AssertionSchemas.assert_ordenamiento_asc_schema_file(response.json())



