from faker import Faker
from src.infra.test import UserRepositorySpy
from src.data.test import DeactivateUserSpy
from src.presenters.helpes import HttpRequest
from .deactivate_user_controllers import DeactivateUserController


faker = Faker()


def test_route():
    """Test route Deactivate User"""

    deactivate_user_use_case = DeactivateUserSpy(UserRepositorySpy())
    deactivate_user_controller = DeactivateUserController(deactivate_user_use_case)

    attribute = {
        "user_id": faker.random_number(digits=2),
        "user_name": faker.name(),
        "password": faker.password(length=12),
    }

    http_request = HttpRequest(query=attribute)

    http_response = deactivate_user_controller.route(http_request=http_request)

    assert http_response.status_code == 200
    assert "error" not in http_response.body


def test_route_invalid_query_error_422():
    """Test route Deactivate User"""

    deactivate_user_use_case = DeactivateUserSpy(UserRepositorySpy())
    deactivate_user_controller = DeactivateUserController(deactivate_user_use_case)

    attribute = {
        "user_id": faker.random_number(digits=2),
        "user_name": faker.name(),
    }

    http_request = HttpRequest(query=attribute)

    http_response = deactivate_user_controller.route(http_request=http_request)

    assert http_response.status_code == 422
    assert "error" in http_response.body


def test_route_invalid_query_error_400():
    """Test route Deactivate User"""

    deactivate_user_use_case = DeactivateUserSpy(UserRepositorySpy())
    deactivate_user_controller = DeactivateUserController(deactivate_user_use_case)

    http_request = HttpRequest()

    http_response = deactivate_user_controller.route(http_request=http_request)

    assert http_response.status_code == 400
    assert "error" in http_response.body
