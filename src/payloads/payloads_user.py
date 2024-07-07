import json


class PayloadUser:
    @staticmethod
    def build_payload_add_user(userName, salutationName, firstName, lastName, type="regular", isActive=True,
                               teamsIds=None, avatarId=None, deleteId="0", emailAddressData=None, emailAddress=None,
                               emailAddressIsOptedOut=None, emailAddressIsInvalid=None, phoneNumberData=None,
                               phoneNumber=None, phoneNumberIsOptedOut=None, phoneNumberIsInvalid=None,
                               gender=None, teamsNames=None, teamsColumns=None, defaultTeamName=None,
                               defaultTeamId=None, rolesIds=None, rolesNames=None, workingTimeCalendarName=None,
                               workingTimeCalendarId=None, layoutSetName=None, layoutSetId=None, password="",
                               passwordConfirm=""):
        payload = {
            "type": type,
            "isActive": isActive,
            "teams": {
                "teamsIds": teamsIds if teamsIds is not None else []
            },
            "avatarId": avatarId if avatarId is not None else [],
            "deleteId": deleteId if deleteId is not None else [],
            "userName": userName if userName is not None else [],
            "salutationName": salutationName if salutationName is not None else [],
            "firstName": firstName if firstName is not None else [],
            "lastName": lastName if lastName is not None else [],
            "name": f"{firstName} {lastName}",
            "title": None,
            "emailAddressData": emailAddressData if emailAddressData is not None else [],
            "emailAddress": emailAddress if emailAddress is not None else [],
            "emailAddressIsOptedOut": emailAddressIsOptedOut if emailAddressIsOptedOut is not None else [],
            "emailAddressIsInvalid": emailAddressIsInvalid if emailAddressIsInvalid is not None else [],
            "phoneNumberData": phoneNumberData if phoneNumberData is not None else [],
            "phoneNumber": phoneNumber if phoneNumber is not None else [],
            "phoneNumberIsOptedOut": phoneNumberIsOptedOut if phoneNumberIsOptedOut is not None else [],
            "phoneNumberIsInvalid": phoneNumberIsInvalid if phoneNumberIsInvalid is not None else [],
            "gender": gender if gender is not None else [],
            "teamsIds": teamsIds if teamsIds is not None else [],
            "teamsNames": teamsNames if teamsNames is not None else {},
            "teamsColumns": teamsColumns if teamsColumns is not None else {},
            "defaultTeamName": defaultTeamName if defaultTeamName is not None else [],
            "defaultTeamId": defaultTeamId if defaultTeamId is not None else [],
            "rolesIds": rolesIds if rolesIds is not None else [],
            "rolesNames": rolesNames if rolesNames is not None else {},
            "workingTimeCalendarName": workingTimeCalendarName if workingTimeCalendarName is not None else [],
            "workingTimeCalendarId": workingTimeCalendarId if workingTimeCalendarId is not None else [],
            "layoutSetName": layoutSetName if layoutSetName is not None else [],
            "layoutSetId": layoutSetId if layoutSetId is not None else [],
            "password": password if password is not None else [],
            "passwordConfirm": passwordConfirm if passwordConfirm is not None else []
        }
        return json.dumps(payload)
