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

    @staticmethod
    def assert_list_length_within_range(response_json, min_len=1, max_len=20):
        list_length = len(response_json['list'])
        assert min_len <= list_length <= max_len, "The length of the list should be between {min_len} and {max_len}."

    @staticmethod
    def assert_list_no_empty(response_json):
        assert response_json['list'] is not None

    @staticmethod
    def assert_response_true(response):
        assert response.text == "true"

    @staticmethod
    def assert_response_is_not_empty(response_text):
        assert response_text != ''

    @staticmethod
    def assert_valid_email_response(response_data, expected_email, expected_subject):
        assert 'id' in response_data, "The response does not contain an ID"
        assert response_data['to'] == expected_email, f"Expected email {expected_email} but got {response_data['to']}"
        assert response_data[
                   'subject'] == expected_subject, f"Expected subject {expected_subject} but got {response_data['subject']}"



    @staticmethod
    def assert_email_with_cc_and_bcc(response, expected_cc, expected_bcc):
        response_data = response.json()
        assert response_data[
                   "cc"] == expected_cc, f"Expected cc field to be {expected_cc}, but got {response_data['cc']}."
        assert response_data[
                   "bcc"] == expected_bcc, f"Expected bcc field to be {expected_bcc}, but got {response_data['bcc']}."
