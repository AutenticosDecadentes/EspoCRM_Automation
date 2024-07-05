from src.espocrm_api.endpoint import Endpoint
from config import BASE_URI


class EndpointTeams:
    @staticmethod
    def build_url_list(base, select=None, maxSize=None, offset=None, orderBy=None, order=None):
        params = []
        if select is not None:
            params.append(f"select={select}")
        if maxSize is not None:
            params.append(f"maxSize={maxSize}")
        if offset is not None:
            params.append(f"offset={offset}")
        if orderBy is not None:
            params.append(f"orderBy={orderBy}")
        if order is not None:
            params.append(f"order={order}")
        return f"{BASE_URI}{base}?{'&'.join(params)}"

    @classmethod
    def list(cls, select="name", maxSize=20, offset=0, orderBy="name", order="asc"):
        return cls.build_url_list(Endpoint.BASE_EQUIPOS.value, select, maxSize, offset, orderBy, order)

    @staticmethod
    def build_url_team_users(base, team_id, primaryFilter=None, select=None, maxSize=None, offset=None, orderBy=None,
                             order=None):
        params = []
        if primaryFilter is not None:
            params.append(f"primaryFilter={primaryFilter}")
        if select is not None:
            params.append(f"select={select}")
        if maxSize is not None:
            params.append(f"maxSize={maxSize}")
        if offset is not None:
            params.append(f"offset={offset}")
        if orderBy is not None:
            params.append(f"orderBy={orderBy}")
        if order is not None:
            params.append(f"order={order}")
        return f"{BASE_URI}{base.format(team_id=team_id)}?{'&'.join(params)}"

    @classmethod
    def team_users(cls, team_id="667594ce0383bbd32", primaryFilter="",
                   select="teamRole,userName,salutationName,firstName,lastName,middleName,name", maxSize=5, offset=0,
                   orderBy="userName", order="asc"):
        return cls.build_url_team_users(Endpoint.BASE_EQUIPO_USUARIOS.value, team_id, primaryFilter, select, maxSize,
                                        offset,
                                        orderBy, order)

    @staticmethod
    def build_url_team_view(base, team_id):
        return f"{BASE_URI}{base.format(team_id=team_id)}"

    @classmethod
    def view(cls, team_id="667db6747f894544e"):
        return cls.build_url_team_view(Endpoint.VER_EQUIPOS.value, team_id)
