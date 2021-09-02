from typing import Type
from src.main.interface import RouteInterface
from src.domain.use_cases import DeactivateUser
from src.presenters.errors import HttpErrors
from src.presenters.helpes import HttpRequest, HttpResponse
from src.validators import validate_activate_user_route


class DeactivateUserController(RouteInterface):
    """Class define controller to deactivate_user"""

    def __init__(self, deactivate_user_use_case: Type[DeactivateUser]) -> None:
        self.deactivate_user_use_case = deactivate_user_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """method to call use case"""

        response = None

        if http_request.query:

            validate_query = validate_activate_user_route(http_request.query)

            if validate_query:
                user_id = http_request.query["user_id"]
                user_name = http_request.query["user_name"]
                password = http_request.query["user_name"]

                response = self.deactivate_user_use_case.deactivate_user(
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
