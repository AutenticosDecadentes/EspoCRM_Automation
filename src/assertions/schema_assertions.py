from src.utils.load_resources import load_schema_resource
import jsonschema
import pytest

class AssertionSchemas:
    @staticmethod
    def normalize_response(response):
        if isinstance(response, dict):
            for key, value in response.items():
                if isinstance(value, dict):
                    AssertionSchemas.normalize_response(value)
                elif isinstance(value, list):
                    for item in value:
                        AssertionSchemas.normalize_response(item)
                elif key == "deleted" and isinstance(value, bool):
                    response[key] = str(value).lower() == "true"
        return response

    @staticmethod
    def validate_json_schema(response, schema_file):
        schema = load_schema_resource(schema_file)
        try:
            jsonschema.validate(instance=response, schema=schema)
            return True
        except jsonschema.exceptions.ValidationError as err:
            pytest.fail(f"JSON schema validation failed: {err}")

    @staticmethod
    def assert_ver_equipo_schema_file(response):
        return AssertionSchemas.validate_json_schema(response, "ver_equipo_schema.json")