import pytest


class AssertionUsuarios:
    @staticmethod
    def assert_status_code(response, expected_status_code):
        assert response.status_code == expected_status_code

    @staticmethod
    def assert_empty_list(response_json, campo):
        assert isinstance(response_json[campo], list)
        assert campo in response_json
        assert len(response_json[campo]) == 0

    @staticmethod
    def assert_total_equals(response_json, expected_total):
        assert response_json['total'] == expected_total

    @staticmethod
    def assert_response_empty(response_json):
        assert response_json == {} or response_json == [] or response_json == ""