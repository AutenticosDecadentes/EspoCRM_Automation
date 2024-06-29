import pytest


class AssertionEquipos:
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
    def assert_check_orden(response_json, orden):
        lista = [equipo['name'] for equipo in response_json['list']]
        if orden == "asc":
            assert lista == sorted(lista), "La lista de equipos no esta en orden asc"
        elif orden == "desc":
            assert lista == sorted(lista, reverse=True), "La lista de equipos no esta en orden desc"
        else:
            pytest.fail(f"Orden '{orden}' inalido")