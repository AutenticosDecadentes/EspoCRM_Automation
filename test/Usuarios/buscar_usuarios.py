import requests
import pytest
from config import BASE_URI
def test_buscar_usaurios(get_headers):
    url = f'{BASE_URI}/User?userType=internal&select=isActive%2CemailAddressIsOptedOut%2CemailAddressIsInvalid%2CemailAddress%2CemailAddressData%2Ctitle%2CuserName%2CsalutationName%2CfirstName%2ClastName%2CmiddleName%2Cname&maxSize=20&offset=0&orderBy=name&order=asc&where%5B0%5D%5Btype%5D=textFilter&where%5B0%5D%5Bvalue%5D=diego'
    headers = get_headers("diego", "zlM23bQzWm")
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
