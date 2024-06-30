from enum import Enum


class Endpoint(Enum):
    LOGIN = "/App/user"
    LISTA_EQUIPOS = "/Team?select=name&maxSize=20&offset=0&orderBy=name&order=asc"
    LISTA_EQUIPOS_SIN_SELECT = "/Team?maxSize=2&offset=0&order=asc"
    LISTA_EQUIPOS_SELECT_DESCONOCIDO = "/Team?select=unknown&maxSize=20&offset=0&orderBy=name&order=asc"
    LISTA_EQUIPOS_MAXSIZE_MAYOR_TOTAL = "/Team?select=name&maxSize=200&offset=0&orderBy=name&order=asc"
    LISTA_EQUIPOS_OFFSET_MAYOR_TOTAL = "/Team?select=name&maxSize=20&offset=201&orderBy=name&order=asc"
    LISTA_EQUIPOS_ORDEN_ASC = "/Team?select=name&maxSize=20&offset=0&orderBy=name&order=asc"
    LISTA_EQUIPOS_ORDEN_DESC = "/Team?select=name&maxSize=20&offset=0&orderBy=name&order=desc"
