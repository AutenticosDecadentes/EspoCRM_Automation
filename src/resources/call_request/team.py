from src.espocrm_api.endpoint_teams import EndpointTeams
from src.espocrm_api.api_request import EspocrmRequest


class TeamCall:
    @classmethod
    def view(cls, headers, team_id):
        response = EspocrmRequest().get(EndpointTeams.view(team_id), headers)
        return response.json()

    @classmethod
    def create(cls, headers, payload):
        response = EspocrmRequest().post(EndpointTeams.team(), headers, payload)
        return response.json()

    @classmethod
    def update(cls, headers, payload, team_id):
        response = EspocrmRequest().put(EndpointTeams.view(team_id), headers, payload)
        return response.json()

    @classmethod
    def delete(cls, headers, team_id):
        response = EspocrmRequest().delete(EndpointTeams.view(team_id), headers)
        return response.json()

    @classmethod
    def view_users(cls, headers, team_id):
        response = EspocrmRequest().get(EndpointTeams.team_users(team_id), headers)
        return response.json()

    @classmethod
    def add_user(cls, headers, payload, team_id):
        response = EspocrmRequest().post(EndpointTeams.add_users(team_id), headers, payload)
        return response.json()
