# endpoints.py
from enum import Enum


class Endpoint(Enum):
    LOGIN = "/App/user"
    EQUIPOS = "/Team"
    TEAM_ID = '667594ac5470f5dc3'


def build_url(base_uri, team_id=Endpoint.TEAM_ID.value, primary_filter='',
              select='teamRole,userName,salutationName,firstName,lastName,middleName,name', max_size=5, offset=0,
              order_by='userName', order='asc'):
    return (
        f'{base_uri}/Team/{team_id}/users?primaryFilter={primary_filter}&select={select}&maxSize={max_size}&offset={offset}&orderBy={order_by}&order={order}')
