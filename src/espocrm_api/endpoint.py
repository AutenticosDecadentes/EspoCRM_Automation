from enum import Enum
from config import BASE_URI


class Endpoint(Enum):
    LOGIN = "/App/user"
    BASE_EQUIPOS = "/Team"
    BASE_EQUIPO_USUARIOS = "/Team/{team_id}/users"
    VER_EQUIPOS = "/Team/{team_id}"
    BASE_USER = "/User"
    BASE_BUSCAR_EQUIPOS = "/User"
    BASE_USUARIO = "/User"
    USUARIO_ERROR = "/ NonExistentEndpoint"
    BASE_BUSCAR_USUARIOS = "/User"

    @classmethod
    def login(cls):
        return f"{BASE_URI}{cls.LOGIN.value}"
