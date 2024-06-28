# schema de respuesta de lista de equipos
equipo_lista_schema = {
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
                    }
                },
                "required": ["id", "name"]
            }
        }
    },
    "required": ["total", "list"]
}

# schema de respuesta de lista de equipos sin select
schema_sin_select = {
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
                    "deleted": {
                        "type": "boolean"
                    },
                    "positionList": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "createdAt": {
                        "type": "string"
                    },
                    "modifiedAt": {
                        "type": "string"
                    },
                    "layoutSetId": {
                        "oneOf": [
                            {
                                "type": "string"
                            },
                            {
                                "type": "null"
                            }
                        ]
                    },
                    "layoutSetName": {
                        "oneOf": [
                            {
                                "type": "string"
                            },
                            {
                                "type": "null"
                            }
                        ]
                    },
                    "workingTimeCalendarId": {
                        "oneOf": [
                            {
                                "type": "string"
                            },
                            {
                                "type": "null"
                            }
                        ]
                    },
                    "workingTimeCalendarName": {
                        "oneOf": [
                            {
                                "type": "string"
                            },
                            {
                                "type": "null"
                            }
                        ]
                    }
                },
                "required": [
                    "id",
                    "name",
                    "deleted",
                    "positionList",
                    "createdAt",
                    "modifiedAt",
                    "layoutSetId",
                    "layoutSetName",
                    "workingTimeCalendarId",
                    "workingTimeCalendarName"
                ]
            }
        }
    },
    "required": [
        "total",
        "list"
    ]
}
