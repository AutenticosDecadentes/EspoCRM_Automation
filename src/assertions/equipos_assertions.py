import jsonschema
import pytest

def assert_json_schema(response_json, schema):
    """
    Valida el JSON de respuesta contra el esquema proporcionado.
    """
    try:
        jsonschema.validate(instance=response_json, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema validation error: {err}")


def assert_status_code(response, expected_status_code):
    """
    Verifica que el código de estado de la respuesta sea el esperado.
    """
    assert response.status_code == expected_status_code


def assert_empty_list(response_json, campo):
    """
    Verifica que la lista bajo el 'campo' proporcionado esté vacía.
    """
    assert campo in response_json
    assert isinstance(response_json[campo], list)
    assert len(response_json[campo]) == 0


def assert_total_equals(response_json, expected_total):
    """
    Verifica que el valor de 'total' en el JSON de respuesta sea igual al valor esperado.
    """
    assert 'total' in response_json
    assert response_json['total'] == expected_total
