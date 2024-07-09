from enum import Enum
from config import BASE_URI


class Endpoint(Enum):
    LOGIN = "/App/user"
    BASE_TEAM = "/Team"
    BASE_TEAM_USERS = "/Team/{team_id}/users"
    BASE_TEAM_VIEW = "/Team/{team_id}"
    BASE_USER = "/User"
    BASE_USER_VIEW = "/User/{user_id}"
    BASE_EMAIL = "/Email"
    BASE_MASS_ACTION = "/MassAction"
    BASE_DUPLICATE = "/action/getDuplicateAttributes"

    @classmethod
    def login(cls):
        return f"{BASE_URI}{cls.LOGIN.value}"

    @classmethod
    def email(cls):
        return f"{BASE_URI}{cls.BASE_EMAIL.value}"

    @classmethod
    def massAction(cls):
        return f"{BASE_URI}{cls.BASE_MASS_ACTION.value}"
