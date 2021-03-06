from cerberus import Validator


def validate_update_user_route(query_params: any) -> bool:
    schema = {
        "user_id": {"type": "integer", "required": True},
        "user_name": {"type": "string", "required": True},
        "old_password": {"type": "string", "required": True},
        "new_data": {
            "type": "dict",
            "required": False,
            "schema": {
                "password": {"type": "string", "required": False},
                "email": {
                    "type": "string",
                    "regex": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
                    "required": False,
                },
                "user_name": {"type": "string", "required": False},
                "type": {
                    "type": "string",
                    "required": False,
                    "allowed": ["common", "seller"],
                },
            },
        },
    }
    v = Validator(schema)

    return v.validate(query_params)
