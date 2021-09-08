from cerberus import Validator


def validate_find_user_route(query_params: any) -> bool:
    schema = {
        "user_id": {"type": "integer", "required": True},
        "user_name": {"type": "string", "required": True},
    }
    v = Validator(schema)

    return v.validate(query_params)
