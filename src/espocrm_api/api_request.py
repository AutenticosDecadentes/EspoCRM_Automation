import requests


class EspocrmRequest:
    @staticmethod
    def get(url, headers=None):
        response = requests.get(url, headers=headers)
        return response
    @staticmethod
    def post(url, headers, payload):
        response = requests.post(url, headers=headers, data=payload)
        return response

    @staticmethod
    def put(url, headers, payload):
        response = requests.put(url, headers=headers, data=payload)
        return response

    @staticmethod
    def delete(url, headers, payload):
        response = requests.delete(url, headers=headers, data=payload)
        return response
