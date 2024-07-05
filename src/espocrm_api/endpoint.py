from enum import Enum
from config import BASE_URI


class Endpoint(Enum):
    LOGIN = "/App/user"
    BASE_TEAM = "/Team"
    BASE_TEAM_USERS = "/Team/{team_id}/users"
    BASE_TEAM_VIEW = "/Team/{team_id}"
    BASE_USER = "/User"

    @classmethod
    def login(cls):
        return f"{BASE_URI}{cls.LOGIN.value}"
