import pytest


class AssertionOrdenamiento:
    @staticmethod
    def assert_comprobar_ordenamiento(response):
        assert all(response.json().get('list')[i]['userName'] <= response.json().get('list')[i+1]['userName'] for i in range(len(response.json())-1))