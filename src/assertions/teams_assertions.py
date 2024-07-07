import pytest


class AssertionTeams:
    @staticmethod
    def assert_check_orden(response_json, order):
        list = [team['name'] for team in response_json['list']]
        if order == "asc":
            assert list == sorted(list), "The equipment list is not in asc order"
        elif order == "desc":
            assert list == sorted(list, reverse=True), "The equipment list is not in order"
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

    @staticmethod
    def assert_response_true(response):
        assert response.text == "true"

    @staticmethod
    def assert_response_false(response):
        assert response.text == "false"

    @staticmethod
    def assert_users_in_team(users_id, team):
        user_ids_in_team = [user['id'] for user in team['list']]
        for user_id in users_id:
            assert user_id in user_ids_in_team, f"User with ID {user_id} not found in the team."

    @staticmethod
    def assert_user_not_in_team(user_id, team):
        user_ids_in_team = [user['id'] for user in team['list']]
        assert user_id not in user_ids_in_team, f"User with ID {user_id} found in the team."
