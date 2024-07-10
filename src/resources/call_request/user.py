from src.espocrm_api.endpoint_users import EndpointUsers
from src.espocrm_api.api_request import EspocrmRequest


class UserCall:
    @classmethod
    def view(cls, headers, user_id):
        response = EspocrmRequest().get(EndpointUsers.view(user_id), headers)
        return response.json()

    @classmethod
    def create(cls, headers, payload):
        response = EspocrmRequest().post(EndpointUsers.user(), headers, payload)
        return response.json()

    @classmethod
    def update(cls, headers, payload, user_id):
        response = EspocrmRequest().put(EndpointUsers.view(user_id), headers, payload)
        return response.json()

    @classmethod
    def delete(cls, headers, user_id):
        response = EspocrmRequest().delete(EndpointUsers.view(user_id), headers)
        return response.json()
