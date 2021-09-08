from src.domain.use_cases.updated_user import UpdateUser
from faker import Faker
from src.infra.test import UserRepositorySpy
from src.data.test import UpdateUserSpy
from src.presenters.helpes import HttpRequest
from .updated_user_controller import UpdateUserController
from src.validators import validate_update_user_route


faker = Faker()


def test_route():
    """Test route Registry User"""

    update_user_use_case = UpdateUserSpy(UserRepositorySpy())
    update_user_controller = UpdateUserController(update_user_use_case)

    attribute = {
        "user_id": faker.random_number(digits=5),
        "user_name": faker.name(),
        "old_password": faker.password(),
        "new_data": {
            "user_name": faker.name(),
            "password": faker.password(),
            "email": faker.email(),
        },
    }

    http_request = HttpRequest(query=attribute)
    http_response = update_user_controller.route(http_request)

    assert http_response.status_code == 200
    assert "error" not in http_response.body


def test_route_invalid_query_error_422():
    """Test route Registry User"""

    update_user_use_case = UpdateUserSpy(UserRepositorySpy())
    update_user_controller = UpdateUserController(update_user_use_case)

    attribute = {
        "user_id": faker.random_number(digits=5),
        # "user_name": faker.name(),
        "old_password": faker.password(),
        "new_data": {
            "user_name": faker.name(),
            "password": faker.password(),
            "email": faker.email(),
        },
    }

    http_request = HttpRequest(query=attribute)
    http_response = update_user_controller.route(http_request)

    assert http_response.status_code == 422
    assert "error" in http_response.body


def test_route_invalid_query_error_400():
    """Test route Registry User"""

    update_user_use_case = UpdateUserSpy(UserRepositorySpy())
    update_user_controller = UpdateUserController(update_user_use_case)

    http_request = HttpRequest()
    http_response = update_user_controller.route(http_request)

    assert http_response.status_code == 400
    assert "error" in http_response.body
