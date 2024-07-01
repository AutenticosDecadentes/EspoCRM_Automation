from src.utils.load_resources import load_schema_resource
import jsonschema
import pytest


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
    def assert_usuarios_buscar_schema_file(response):
        return AssertionSchemas().validate_json_schema(response, "usuarios_schema.json")
    
    @staticmethod
    def assert_equipo_lista_schema_file(response):
        return AssertionSchemas().validate_json_schema(response, "equipo_lista_schema.json")

    @staticmethod
    def assert_equipo_sin_select_schema_file(response):
        return AssertionSchemas().validate_json_schema(response, "equipo_sin_select_schema.json")

    @staticmethod
    def assert_equipo_usuarios_schema_file(response):
        return AssertionSchemas().validate_json_schema(response, "equipo_usuario_schema.json")

    @staticmethod
    def assert_usuario_lista_schema_file(response):
        return AssertionSchemas().validate_json_schema(response, "usuario_lista_schema.json")

    @staticmethod
    def assert_ver_equipo_schema_file(response):
        return AssertionSchemas().validate_json_schema(response, "equipo_ver_schema.json")

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
    def assert_response_vacio(response_text):
        assert response_text == ''

    @staticmethod
    def assert_list_no_empty(response_json):
        assert response_json['list'] is not None
