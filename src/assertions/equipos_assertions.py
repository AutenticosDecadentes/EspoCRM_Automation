import pytest


class AssertionEquipos:
    @staticmethod
    def assert_check_orden(response_json, orden):
        lista = [equipo['name'] for equipo in response_json['list']]
        if orden == "asc":
            assert lista == sorted(lista), "La lista de equipos no esta en orden asc"
        elif orden == "desc":
            assert lista == sorted(lista, reverse=True), "La lista de equipos no esta en orden desc"
        else:
            pytest.fail(f"Orden '{orden}' invalido")

