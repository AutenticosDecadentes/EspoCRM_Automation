import json


class PayloadTeam:
    @staticmethod
    def build_payload_add_user_team(user_ids):
        payload = {
            "ids": user_ids
        }
        return json.dumps(payload)

    @staticmethod
    def build_payload_unlink_user_team(user_id):
        payload = {
            "id": user_id
        }
        return json.dumps(payload)

    @staticmethod
    def build_payload_add_team(name, rolesIds=None, rolesNames=None, positionList=None, layoutSetName=None,
                               layoutSetId=None, workingTimeCalendarName=None, workingTimeCalendarId=None):
        payload = {
            "name": name,
            "rolesIds": rolesIds if rolesIds is not None else [],
            "rolesNames": rolesNames if rolesNames is not None else {},
            "positionList": positionList if positionList is not None else [],
            "layoutSetName": layoutSetName,
            "layoutSetId": layoutSetId,
            "workingTimeCalendarName": workingTimeCalendarName,
            "workingTimeCalendarId": workingTimeCalendarId
        }
        return json.dumps(payload)

    @staticmethod
    def build_payload_delete_multiple_team(entityType=None, action=None, params=None, idle=None):
        payload = {
            "entityType": entityType if entityType is not None else "",
            "action": action if action is not None else "",
            "params": {"ids": params} if params is not None else {"ids": []},
            "idle": idle if idle is not None else False,
        }
        return json.dumps(payload)
