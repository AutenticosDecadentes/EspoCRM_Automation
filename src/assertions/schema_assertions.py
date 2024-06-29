from src.utils.load_resources import load_schema_resource
import jsonschema
import pytest

class AssertionSchemas:
    @staticmethod
    def validate_json_schema(response, schema_file):
        schema = load_schema_resource(schema_file)
        try:
            jsonschema.validate(instance=response, schema=schema)
            return True
        except jsonschema.exceptions.ValidationError as err:
            pytest.fail(f"JSON schema validation failed: {err}")

