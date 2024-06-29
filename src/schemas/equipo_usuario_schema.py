meeting_schema = {
    "type": "object",
    "properties": {
        "total": {
            "type": "integer"
        },
        "list": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "string"
                    },
                    "name": {
                        "type": "string"
                    },
                    "userName": {
                        "type": "string"
                    },
                    "type": {
                        "type": "string"
                    },
                    "salutationName": {
                        "type": ["string", "null"]
                    },
                    "firstName": {
                        "type": ["string", "null"]
                    },
                    "lastName": {
                        "type": "string"
                    },
                    "isActive": {
                        "type": "boolean"
                    },
                    "teamRole": {
                        "type": ["null"]
                    },
                    "middleName": {
                        "type": ["null"]
                    },
                    "createdById": {
                        "type": "string"
                    }
                },
                "required": [
                    "id",
                    "name",
                    "userName",
                    "type",
                    "salutationName",
                    "firstName",
                    "lastName",
                    "isActive",
                    "teamRole",
                    "middleName",
                    "createdById"
                ]
            }
        }
    },
    "required": [
        "total",
        "list"
    ]
}