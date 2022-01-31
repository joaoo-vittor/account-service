from typing import Type
from src.main.interface import RouteInterface
from src.presenters.helpes import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors
from src.domain.use_cases import FindUser
from src.validators import validate_find_user_route


class FindUserController(RouteInterface):
    """Class define controller to find use"""

    def __init__(self, find_user_use_case: Type[FindUser]) -> None:
        self.find_user_use_case = find_user_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """method to call use case"""

        response = None

        if http_request.query:

            validate_query = validate_find_user_route(http_request.query)

            if validate_query:

                if (
                    "user_name" not in http_request.query.keys()
                    and "user_id" in http_request.query.keys()
                ):
                    user_id = http_request.query["user_id"]
                    response = self.find_user_use_case.by_id(user_id=user_id)

                if (
                    "user_name" in http_request.query.keys()
                    and "user_id" not in http_request.query.keys()
                ):
                    user_name = http_request.query["user_name"]
                    response = self.find_user_use_case.by_name(user_name=user_name)

                if (
                    "user_name" in http_request.query.keys()
                    and "user_id" in http_request.query.keys()
                ):
                    user_name = http_request.query["user_name"]
                    user_id = http_request.query["user_id"]
                    response = self.find_user_use_case.by_id_and_name(
                        user_name=user_name, user_id=user_id
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
