from enum import Enum


class Endpoint(Enum):
    LOGIN = "/App/user"
    BASE_EQUIPOS = "/Team"
    BASE_BUSCAR_EQUIPOS = "/User"
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
      
    @staticmethod
    def build_url_buscar_usuarios(base, select=None, maxSize=None, offset=None, orderBy=None, order=None, where=None):

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
        if where is not None:
            params.append(f"where[0][type]=textFilter&where[0][value]={where}")

        return f"{base}?{'&'.join(params)}"

    @classmethod
    def BUSCAR_USUARIOS(cls, maxSize=20, offset=0, orderBy="name", order="asc", where=None):
        select = "isActive%2CemailAddressIsOptedOut%2CemailAddressIsInvalid%2CemailAddress%2CemailAddressData%2Ctitle%2CuserName%2CsalutationName%2CfirstName%2ClastName%2CmiddleName%2Cname"
        return cls.build_url_buscar_usuarios(cls.BASE_BUSCAR_EQUIPOS.value, select, maxSize, offset, orderBy, order, where)

    
      
 