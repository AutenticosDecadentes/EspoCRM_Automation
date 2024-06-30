import jsonschema
import pytest
from src.schemas.equipo_usuario_schema import meeting_schema


def assert_login_schema_file(response):
    schema = meeting_schema
    try:
        jsonschema.validate(instance=response, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema dont match {err}")