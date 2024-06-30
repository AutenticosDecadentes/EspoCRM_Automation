import pytest
import requests
import base64
from config import BASE_URI, X_Api_Key


@pytest.fixture
def get_headers():
    def _get_headers(username, password):
        espo_authorization = encoded(username, password)
        return {
            'Espo-Authorization': espo_authorization,
            'X-Api-Key': X_Api_Key
        }
    return _get_headers


def encoded(username, password):
    credentials = f'{username}:{password}'
    encode = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    return encode
