from enum import Enum


class Endpoint(Enum):
    LOGIN = "/App/user"
    BASE_EQUIPOS = "/Team"
    BASE_EQUIPO_USUARIOS = "/Team/667594ac5470f5dc3/users"

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

    @staticmethod
    def build_url_equipo_usuarios(base, primaryFilter=None, select=None, maxSize=None, offset=None, orderBy=None,
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
        return f"{base}?{'&'.join(params)}"

    @classmethod
    def EQUIPO_USUARIOS(cls, primaryFilter="",
                        select="teamRole,userName,salutationName,firstName,lastName,middleName,name", maxSize=5,
                        offset=0, orderBy="userName", order="asc"):
        return cls.build_url_equipo_usuarios(cls.BASE_EQUIPO_USUARIOS.value, primaryFilter, select, maxSize, offset,
                                             orderBy, order)


