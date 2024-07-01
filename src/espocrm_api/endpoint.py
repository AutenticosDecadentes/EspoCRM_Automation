from enum import Enum


class Endpoint(Enum):
    LOGIN = "/App/user"
    LISTA_USUARIOS = "/User?userType=internal&select=isActive,emailAddressIsOptedOut,emailAddressIsInvalid,emailAddress,emailAddressData,title,userName,salutationName,firstName,lastName,middleName,name&maxSize=20&offset=0&orderBy=userName&order=asc"
    LISTA_USUARIOS_DESC = "/User?userType=internal&select=isActive,emailAddressIsOptedOut,emailAddressIsInvalid,emailAddress,emailAddressData,title,userName,salutationName,firstName,lastName,middleName,name&maxSize=20&offset=0&orderBy=userName&order=desc"
    LISTA_USUARIOS_ASC = "/User?userType=internal&select=isActive,emailAddressIsOptedOut,emailAddressIsInvalid,emailAddress,emailAddressData,title,userName,salutationName,firstName,lastName,middleName,name&maxSize=20&offset=0&orderBy=userName&order=asc"
    LISTA_USUARIOS_VACIA = "/User?maxSize=0&offset=0&orderBy=userName&order=asc"