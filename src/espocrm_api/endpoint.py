from enum import Enum


class Endpoint(Enum):
    LOGIN = "/App/user"
    BASE_EQUIPOS = "/Team"

    @staticmethod
    def build_url_equipos_list(base, select=None, maxSize=None, offset=None, orderBy=None, order=None):
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
        return f"{base}?{'&'.join(params)}"

    @classmethod
    def LISTA_EQUIPOS(cls, select="name", maxSize=20, offset=0, orderBy="name", order="asc"):
        return cls.build_url_equipos_list(cls.BASE_EQUIPOS.value, select, maxSize, offset, orderBy, order)
