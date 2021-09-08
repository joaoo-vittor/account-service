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
                "email": {"type": "string", "required": False},
                "user_name": {"type": "string", "required": False},
            },
        },
    }
    v = Validator(schema)

    return v.validate(query_params)
