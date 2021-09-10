from typing import Type
from src.main.interface import RouteInterface
from src.presenters.helpes import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors
from src.domain.use_cases import UpdateUser
from src.validators import validate_update_user_route


class UpdateUserController(RouteInterface):
    """Class define controller to Update User"""

    def __init__(self, update_user_use_case: Type[UpdateUser]) -> None:
        self.update_user_use_case = update_user_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """method to call use case"""

        response = None

        if http_request.query:

            validate_query = validate_update_user_route(http_request.query)

            if validate_query:
                user_id = http_request.query["user_id"]
                user_name = http_request.query["user_name"]
                old_password = http_request.query["old_password"]
                new_data = http_request.query["new_data"]

                response = self.update_user_use_case.updated_user(
                    user_id=user_id,
                    user_name=user_name,
                    old_password=old_password,
                    new_data=new_data,
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
