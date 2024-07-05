import pytest


class AssertionUsers:

    @staticmethod
    def assert_response_empty(response_text):
        assert response_text == ''

    @staticmethod
    def assert_check_order_asc(response_json):
        lists = [user['userName'] for user in response_json['list']]
        assert lists == sorted(lists), "The user list is not in ascending order"

    @staticmethod
    def assert_check_order_desc(response_json):
        lists = [user['userName'] for user in response_json['list']]
        assert lists == sorted(lists, reverse=True), "The user list is not in descending order"

    @staticmethod
    def assert_empty_list(response_json):
        assert isinstance(response_json['list'], list)
        assert len(response_json['list']) == 0

    @staticmethod
    def assert_campos_especificados(response_json):
        expected_campos = [
            'createdById', 'emailAddress', 'emailAddressIsInvalid', 'emailAddressIsOptedOut',
            'firstName', 'id', 'isActive', 'lastName', 'middleName', 'name', 'salutationName',
            'title', 'type', 'userName'

        ]

        for usuario in response_json['list']:
            for campo in expected_campos:
                assert campo in usuario, f"El campo '{campo}' no está presente en la lista de usuarios"

    @staticmethod
    def assert_total(response_json):
        assert 'total' in response_json, "El campo 'total' no está presente en la respuesta JSON"
        assert isinstance(response_json['total'], int), "El campo 'total' no es de tipo entero"
        assert response_json['total'] >= 0, "El campo 'total' debe ser un número positivo"
