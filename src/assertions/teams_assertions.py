import pytest


class AssertionTeams:
    @staticmethod
    def assert_check_orden(response_json, order):
        list = [team['name'] for team in response_json['list']]
        if order == "asc":
            assert list == sorted(list), "La lista de equipos no esta en orden asc"
        elif order == "desc":
            assert list == sorted(list, reverse=True), "La lista de equipos no esta en orden desc"
        else:
            pytest.fail(f"Orden '{order}' invalido")

    @staticmethod
    def assert_response_empty(response_text):
        assert response_text == ''

    @staticmethod
    def assert_empty_field_list(response_json):
        field = "list"
        list_field = response_json.get(field)
        assert list_field is not None, f"'{field}' not found in the response."
        assert isinstance(list_field, list), f"The field '{field}' is not a list."
        assert len(list_field) == 0, f"The list '{field}' is not empty."

    @staticmethod
    def assert_field_total_equals(response_json, expected_total):
        assert response_json[
                   'total'] == expected_total, f"Expected total to be {expected_total}, but got {response_json['total']}"

    @staticmethod
    def assert_field_list_no_empty(response_json):
        assert response_json['list'] is not None, "List is None"
        assert len(response_json['list']) > 0, "List is empty"

    @staticmethod
    def assert_check_order_asc(response_json):
        lists = [user['userName'] for user in response_json['list']]
        assert lists == sorted(lists), "The user list is not in ascending order"

    @staticmethod
    def assert_check_order_desc(response_json):
        lists = [user['userName'] for user in response_json['list']]
        assert lists == sorted(lists, reverse=True), "The user list is not in descending order"
