import json

class PayloadAvatar:
    @staticmethod
    def build_payload_add_avatar(payload):
        return json.dumps(payload)
    

