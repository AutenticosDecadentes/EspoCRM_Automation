from src.espocrm_api.endpoint import Endpoint
from config import BASE_URI


class EndpointUsers:
    @staticmethod
    def build_url_search_users(base, select=None, maxSize=None, offset=None, orderBy=None, order=None, where=None):

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

        return f"{BASE_URI}{base}?{'&'.join(params)}"

    @classmethod
    def search_usuers(cls, maxSize=20, offset=0, orderBy="name", order="asc", where=None):
        select = "isActive%2CemailAddressIsOptedOut%2CemailAddressIsInvalid%2CemailAddress%2CemailAddressData%2Ctitle%2CuserName%2CsalutationName%2CfirstName%2ClastName%2CmiddleName%2Cname"
        return cls.build_url_search_users(Endpoint.BASE_USER.value, select, maxSize, offset, orderBy, order,
                                          where)
