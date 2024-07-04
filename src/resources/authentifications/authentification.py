from src.utils.load_resources import load_credential_resource


class Auth:
    def __init__(self):
        self.users = self.load_file()

    @staticmethod
    def load_file():
        return load_credential_resource("users.json")

    def get_user(self, user_type):
        return self.users.get(user_type)

    def build_headers(self, get_headers, user_type, additional_headers=None):
        user = self.get_user(user_type)
        headers = get_headers(user["username"], user["password"])
        if additional_headers:
            headers.update(additional_headers)
        return headers

    def get_valid_user_headers(self, get_headers, additional_headers=None):
        return self.build_headers(get_headers, "valid_user", additional_headers)

    def get_invalid_user_headers(self, get_headers, additional_headers=None):
        return self.build_headers(get_headers, "invalid_user", additional_headers)

    def get_unauthorized_teams_user_headers(self, get_headers, additional_headers=None):
        return self.build_headers(get_headers, "unauthorized_teams_user", additional_headers)

    def get_without_teams_user_headers(self, get_headers, additional_headers=None):
        return self.build_headers(get_headers, "without_teams_user", additional_headers)

    def get_disabled_user_headers(self, get_headers, additional_headers=None):
        return self.build_headers(get_headers, "disabled_user", additional_headers)

    def get_empty_user_headers(self, get_headers, additional_headers=None):
        return self.build_headers(get_headers, "empty_user", additional_headers)



###BORRAR
from src.utils.load_resources import load_credential_resource
from config import BASE_URI
from src.espocrm_api.api_request import EspocrmRequest


class Authentication:
    def __init__(self):
        self.users = self.load_file()

    @staticmethod
    def load_file():
        return load_credential_resource("users.json")

    def get_user(self, user_type):
        return self.users.get(user_type)

    def _authenticate_user(self, get_headers, endpoint, user_type, method, payload=None):
        user = self.get_user(user_type)
        url = f'{BASE_URI}{endpoint}'
        headers = get_headers(user["username"], user["password"])
        if method == 'GET':
            return EspocrmRequest().get(url, headers=headers)
        elif method == 'POST':
            return EspocrmRequest().post(url, headers=headers, payload=payload)
        elif method == 'PUT':
            return EspocrmRequest().put(url, headers=headers, payload=payload)
        elif method == 'DELETE':
            return EspocrmRequest().delete(url, headers=headers, payload=payload)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

    def authenticate_sin_equipo(self, get_headers, endpoint, method):
        return self._authenticate_user(get_headers, endpoint, "no_equipo_user", method, payload=None)

    def authenticate_valid_user(self, get_headers, endpoint, method):
        return self._authenticate_user(get_headers, endpoint, "valid_user", method, payload=None)

    def authenticate_invalid_user(self, get_headers, endpoint, method):
        return self._authenticate_user(get_headers, endpoint, "invalid_user", method, payload=None)

    def authenticate_no_authorization_equipos(self, get_headers, endpoint, method):
        return self._authenticate_user(get_headers, endpoint, "no_authorization_equipos_user", method, payload=None)

    def authenticate_user_disabled(self, get_headers, endpoint, method):
        return self._authenticate_user(get_headers, endpoint, "disabled_user", method, payload=None)

    def authenticate_user_empty(self, get_headers, endpoint, method):
        return self._authenticate_user(get_headers, endpoint, "empty_user", method, payload=None)
