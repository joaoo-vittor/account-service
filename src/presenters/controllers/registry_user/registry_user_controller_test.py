from faker import Faker
from src.infra.test import UserRepositorySpy
from src.data.test import RegistryUserSpy
from src.presenters.helpes import HttpRequest
from .registry_user_controller import RegistryUserController


faker = Faker()


def test_route():
    """Test route Registry User"""

    registry_user_use_case = RegistryUserSpy(UserRepositorySpy())
    registry_user_controller = RegistryUserController(registry_user_use_case)

    attribute = {
        "user_name": faker.name(),
        "password": faker.password(),
    }

    http_request = HttpRequest(query=attribute)

    http_response = registry_user_controller.route(http_request)

    assert http_response.status_code == 200
    assert "error" not in http_response.body


def test_route_invalid_query_error_422():
    """Test route Registry User"""

    registry_user_use_case = RegistryUserSpy(UserRepositorySpy())
    registry_user_controller = RegistryUserController(registry_user_use_case)

    attribute = {
        "user_name": faker.name(),
    }

    http_request = HttpRequest(query=attribute)

    http_response = registry_user_controller.route(http_request)

    assert http_response.status_code == 422
    assert "error" in http_response.body


def test_route_invalid_query_error_400():
    """Test route Registry User"""

    registry_user_use_case = RegistryUserSpy(UserRepositorySpy())
    registry_user_controller = RegistryUserController(registry_user_use_case)

    http_request = HttpRequest()
    http_response = registry_user_controller.route(http_request)

    assert http_response.status_code == 400
    assert "error" in http_response.body
