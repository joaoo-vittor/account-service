from cerberus import Validator


def validate_find_user_route(query_params: any) -> bool:
    schema = {
        "user_id": {"type": "integer", "required": False},
        "user_name": {"type": "string", "required": False},
    }
    v = Validator(schema)

    return v.validate(query_params)
