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
        return AssertionSchemas().validate_json_schema(payload, "team_add_user_schema.json")

    @staticmethod
    def assert_add_team_schema_schema_file(payload):
        return AssertionSchemas().validate_json_schema(payload, "add_team_schema.json")
