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
