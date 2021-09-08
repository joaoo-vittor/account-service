from typing import Type
from src.main.interface import RouteInterface
from src.presenters.helpes import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors
from src.domain.use_cases import RegistryUser
from src.validators import validate_registry_user_route


class RegistryUserController(RouteInterface):
    """Class define controller to registry user"""

    def __init__(self, registry_user_use_case: Type[RegistryUser]) -> None:
        self.registry_user_use_case = registry_user_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """method to call use case"""

        response = None

        if http_request.query:

            validate_query = validate_registry_user_route(http_request.query)

            if validate_query:
                user_name = http_request.query["user_name"]
                password = http_request.query["password"]

                response = self.registry_user_use_case.registry_user(
                    user_name=user_name, password=password
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
