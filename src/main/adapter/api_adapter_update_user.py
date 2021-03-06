from typing import Type
from sqlalchemy.exc import IntegrityError
from src.main.interface import RouteInterface as Route
from src.presenters.helpes import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors
from flask_jwt_extended import get_jwt_identity


def flask_adapter_update_user(request: any, api_route: Type[Route]) -> any:
    """Adapter pattern to Flask
    :param - Flask Request
    :api_route - Composite Route
    """

    try:
        query_string_params = request.get_json()
        identity_token = get_jwt_identity()
        params = {}

        if (
            "old_password" in query_string_params.keys()
            and "new_data" in query_string_params.keys()
        ):
            params["user_id"] = int(identity_token["user_id"])
            params["user_name"] = str(identity_token["user_name"])
            params["old_password"] = str(query_string_params["old_password"])
            params["new_data"] = query_string_params["new_data"]

    except:
        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    http_request = HttpRequest(header=request.headers, body=request.json, query=params)

    try:
        response = api_route.route(http_request=http_request)
    except IntegrityError:
        http_error = HttpErrors.error_409()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    except Exception as exc:
        print(exc)
        http_error = HttpErrors.error_500()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    return response
