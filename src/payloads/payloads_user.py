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
            "avatarId": avatarId,
            "deleteId": deleteId,
            "userName": userName,
            "salutationName": salutationName,
            "firstName": firstName,
            "lastName": lastName,
            "name": f"{firstName} {lastName}",
            "title": None,
            "emailAddressData": emailAddressData if emailAddressData is not None else [],
            "emailAddress": emailAddress,
            "emailAddressIsOptedOut": emailAddressIsOptedOut,
            "emailAddressIsInvalid": emailAddressIsInvalid,
            "phoneNumberData": phoneNumberData if phoneNumberData is not None else [],
            "phoneNumber": phoneNumber,
            "phoneNumberIsOptedOut": phoneNumberIsOptedOut,
            "phoneNumberIsInvalid": phoneNumberIsInvalid,
            "gender": gender,
            "teamsIds": teamsIds if teamsIds is not None else [],
            "teamsNames": teamsNames if teamsNames is not None else {},
            "teamsColumns": teamsColumns if teamsColumns is not None else {},
            "defaultTeamName": defaultTeamName,
            "defaultTeamId": defaultTeamId,
            "rolesIds": rolesIds if rolesIds is not None else [],
            "rolesNames": rolesNames if rolesNames is not None else {},
            "workingTimeCalendarName": workingTimeCalendarName,
            "workingTimeCalendarId": workingTimeCalendarId,
            "layoutSetName": layoutSetName,
            "layoutSetId": layoutSetId,
            "password": password,
            "passwordConfirm": passwordConfirm
        }
        return json.dumps(payload)

    @staticmethod
    def build_payload_email(status="Sending", to=None, isRead=True, isImportant=False, inTrash=False, folderId=None,
                            isUsers=False, isHtml=True, isSystem=False, isJustSent=False,
                            fromAddress="hhellooworld01@gmail.com", cc="", bcc="", parentType=None, parentName=None,
                            parentId=None, selectTemplateName=None,
                            selectTemplateId=None,
                            subject=None, attachmentsIds=None, body=None, bodyPlain=None):
        payload = {
            "status": status,
            "to": to,
            "isRead": isRead,
            "isImportant": isImportant,
            "inTrash": inTrash,
            "folderId": folderId,
            "isUsers": isUsers,
            "isHtml": isHtml,
            "isSystem": isSystem,
            "isJustSent": isJustSent,
            "from": fromAddress,
            "cc": cc,
            "bcc": bcc,
            "parentType": parentType,
            "parentName": parentName,
            "parentId": parentId,
            "selectTemplateName": selectTemplateName,
            "selectTemplateId": selectTemplateId,
            "subject": subject,
            "name": subject,
            "attachmentsIds": attachmentsIds if attachmentsIds is not None else [],
            "body": body,
            "bodyPlain": bodyPlain
        }
        return json.dumps(payload)

    @staticmethod
    def build_payload_update_users_roles(user_ids, role_id):
        payload = {
            "action": "update",
            "entityType": "User",
            "params": {
                "ids": user_ids,
                "where": None,
                "searchParams": None
            },
            "data": {
                "values": {
                    "rolesIds": [role_id]
                },
                "actions": {
                    "rolesIds": "update"
                }
            },
            "idle": False
        }
        return json.dumps(payload)

    @staticmethod
    def build_payload_duplicate_data_user(user_id):
        payload = {
            "id": user_id
        }
        return json.dumps(payload)
