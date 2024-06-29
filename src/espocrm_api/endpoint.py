from enum import Enum


class Endpoint(Enum):
    LOGIN = "/App/user"
    LISTA_EQUIPOS = "/Team?select=name&maxSize=2&offset=0&order=asc"
    LISTA_EQUIPOS_SIN_SELECT = "/Team?maxSize=2&offset=0&order=asc"
