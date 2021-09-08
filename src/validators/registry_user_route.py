from cerberus import Validator


def validate_registry_user_route(query_params: any) -> bool:
    schema = {
        "user_name": {"type": "string", "required": True},
        "password": {"type": "string", "required": True},
    }
    v = Validator(schema)

    return v.validate(query_params)
