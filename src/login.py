import base64
import requests
from config import BASE_URI, X_Api_Key


def test_login_valido():
    url = f'{BASE_URI}/App/user'
    espo_authorization = encoded("junior", "junior1")
    payload = {}
    headers = {
        'Espo-Authorization': espo_authorization,
        'X-Api-Key': X_Api_Key
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)


def encoded(username, password):
    credentials = f'{username}:{password}'
    encode = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    return encode


test_login_valido()
