import json


class PayloadTeam:
    @staticmethod
    def build_payload_add_user_team(user_ids):
        payload = {
            "ids": user_ids
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
