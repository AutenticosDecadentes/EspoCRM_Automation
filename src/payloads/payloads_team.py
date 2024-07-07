import json


class PayloadTeam:
    @staticmethod
    def build_payload_add_user_team(user_ids):
        payload = {
            "ids": user_ids
        }
        return json.dumps(payload)

    @staticmethod
    def build_payload_add_team(name=None, rolesIds=None, rolesNames=None, positionList=None, layoutSetName=None,
                               layoutSetId=None, workingTimeCalendarName=None, workingTimeCalendarId=None):
        payload = {
            "name": name if name is not None else [],
            "rolesIds": rolesIds if rolesIds is not None else [],
            "rolesNames": rolesNames if rolesNames is not None else {},
            "positionList": positionList if positionList is not None else [],
            "layoutSetName": layoutSetName if layoutSetName is not None else [],
            "layoutSetId": layoutSetId if layoutSetId is not None else [],
            "workingTimeCalendarName": workingTimeCalendarName if workingTimeCalendarName is not None else [],
            "workingTimeCalendarId": workingTimeCalendarId if workingTimeCalendarId is not None else []
        }
        return json.dumps(payload)
