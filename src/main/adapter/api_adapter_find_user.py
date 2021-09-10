from typing import Type
from sqlalchemy.exc import IntegrityError
from src.main.interface import RouteInterface as Route
from src.presenters.helpes import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors


def flask_adapter_find_user(request: any, api_route: Type[Route]) -> any:
    """Adapter pattern to Flask
    :param - Flask Request
    :api_route - Composite Route
    """

    try:
        # query_string_params = request.get_json()
        query_string_params = request.args.to_dict()
        params = {}

        if "user_name" in query_string_params.keys():
            params["user_name"] = str(query_string_params["user_name"])

        if "user_id" in query_string_params.keys():
            params["user_id"] = int(query_string_params["user_id"])

        if (
            "user_id" in query_string_params.keys()
            and "user_name" in query_string_params.keys()
        ):
            params["user_name"] = str(query_string_params["user_name"])
            params["user_id"] = int(query_string_params["user_id"])

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
