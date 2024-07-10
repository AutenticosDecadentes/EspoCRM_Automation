from src.utils.load_resources import load_schema_resource
import jsonschema
import pytest
import json


class AssertionSchemas:
    @staticmethod
    def validate_json_schema(response, schema_file):
        try:
            schema = load_schema_resource(schema_file)
        except FileNotFoundError:
            pytest.fail(f"Schema file '{schema_file}' not found")
        except json.JSONDecodeError as err:
            pytest.fail(f"Failed to decode JSON schema: {err}")

        try:
            jsonschema.validate(instance=response, schema=schema)
            return True
        except jsonschema.exceptions.ValidationError as err:
            pytest.fail(f"JSON schema validation failed: {err}")

    @staticmethod
    def assert_users_search_schema_file(response):
        return AssertionSchemas().validate_json_schema(response, "users_search_list_schema.json")

    @staticmethod
    def assert_teams_list_schema_file(response):
        return AssertionSchemas().validate_json_schema(response, "teams_list_schema.json")

    @staticmethod
    def assert_teams_list_without_select_schema_file(response):
        return AssertionSchemas().validate_json_schema(response, "teams_list_without_select_schema.json")

    @staticmethod
    def assert_teams_users_schema_file(response):
        return AssertionSchemas().validate_json_schema(response, "teams_users_schema.json")

    @staticmethod
    def assert_users_list_schema_file(response):
        return AssertionSchemas().validate_json_schema(response, "users_list_schema.json")

    @staticmethod
    def assert_team_view_schema_file(response):
        return AssertionSchemas().validate_json_schema(response, "team_view_schema.json")

    @staticmethod
    def assert_users_order_asc_schema_file(response):
        return AssertionSchemas().validate_json_schema(response, "users_list_asc_schema.json")

    @staticmethod
    def assert_users_order_desc_schema_file(response):
        return AssertionSchemas().validate_json_schema(response, "users_list_desc_schema.json")

    @staticmethod
    def assert_team_add_user_schema_payload_file(payload):
        if isinstance(payload, str):
            payload = json.loads(payload)
        return AssertionSchemas().validate_json_schema(payload, "team_add_user_schema.json")

    @staticmethod
    def assert_add_team_schema_schema_file(payload):
        return AssertionSchemas().validate_json_schema(payload, "add_team_schema.json")

    @staticmethod
    def assert_team_delete_multiple_team_schema_payload_file(payload):
        if isinstance(payload, str):
            payload = json.loads(payload)
        return AssertionSchemas().validate_json_schema(payload, "team_delete_multiple_team_schema.json")

    @staticmethod
    def assert_team_unlink_user_schema_payload_file(payload):
        if isinstance(payload, str):
            payload = json.loads(payload)
        return AssertionSchemas().validate_json_schema(payload, "team_unlink_user_schema.json")

    @staticmethod
    def assert_user_update_multiple_users_schema_payload_file(payload):
        if isinstance(payload, str):
            payload = json.loads(payload)
        return AssertionSchemas.validate_json_schema(payload, "test_update_multiple_users.json")

    @staticmethod
    def assert_user_duplicate_data_schema_payload_file(payload):
        if isinstance(payload, str):
            payload = json.loads(payload)
        return AssertionSchemas().validate_json_schema(payload, "user_duplicate_data_payload_schema.json")

    @staticmethod
    def assert_user_duplicate_data_schema_file(response):
        return AssertionSchemas().validate_json_schema(response, "user_duplicate_data_response_schema.json")

    @staticmethod
    def assert_add_user_schema_file(payload):
        return AssertionSchemas().validate_json_schema(payload, "add_user_schema.json")
    @staticmethod
    def assert_add_avatar_schema_file(payload):
        return AssertionSchemas().validate_json_schema(payload, "add_avatar_schema.json")

