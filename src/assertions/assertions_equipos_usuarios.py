import jsonschema
import pytest
from src.utils.load_resources import load_schema_resource


def assert_login_schema_file(response):
    schema = load_schema_resource("login_schema.json")
    try:
        jsonschema.validate(instance=response, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema dont match {err}")
