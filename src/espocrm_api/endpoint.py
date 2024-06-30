from enum import Enum


class Endpoint(Enum):
    LOGIN = "/App/user"
    LISTA_USUARIOS = "/User?userType=internal&select=isActive%2CemailAddressIsOptedOut%2CemailAddressIsInvalid%2CemailAddress%2CemailAddressData%2Ctitle%2CuserName%2CsalutationName%2CfirstName%2ClastName%2CmiddleName%2Cname&maxSize=20&offset=0&orderBy=userName&order=asc"
