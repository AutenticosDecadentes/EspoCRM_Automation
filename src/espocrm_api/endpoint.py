from enum import Enum


class Endpoint(Enum):
    LOGIN = "/App/user"
    LISTA_EQUIPOS = "/Team?select=asdasd&maxSize=200&offset=0&orderBy=name&order=asc"
    LISTA_EQUIPOS_SIN_SELECT = "/Team?maxSize=2&offset=0&order=asc"
    LISTA_EQUIPOS_DESCONOCIDO = "/Team?select=unknown&maxSize=200&offset=0&orderBy=name&order=asc"
