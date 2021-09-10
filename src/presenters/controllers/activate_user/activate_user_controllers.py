from typing import Type
from src.main.interface import RouteInterface
from src.domain.use_cases import ActivateUser
from src.presenters.helpes import HttpResponse, HttpRequest
from src.presenters.errors import HttpErrors
from src.validators import validate_activate_user_route


class ActivateController(RouteInterface):
    """Class to define controller to activate_user use case"""

    def __init__(self, activate_user_use_case: Type[ActivateUser]) -> None:
        self.activate_user_use_case = activate_user_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """method to call use case"""

        response = None

        if http_request.query:

            validate_query = validate_activate_user_route(http_request.query)

            if validate_query:
                user_id = http_request.query["user_id"]
                user_name = http_request.query["user_name"]
                password = http_request.query["password"]

                response = self.activate_user_use_case.activate_user(
                    user_id=user_id, user_name=user_name, password=password
                )

            else:
                response = {"Success": False, "Data": None}

            if response["Success"] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )

            return HttpResponse(status_code=200, body=response["Data"])

        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
