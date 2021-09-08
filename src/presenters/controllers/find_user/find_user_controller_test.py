from faker import Faker
from src.infra.test import UserRepositorySpy
from src.data.test import FindUserSpy
from src.presenters.helpes import HttpRequest
from .find_user_controller import FindUserController


faker = Faker()


def test_route():
    """Test route Find User"""

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)

    attribute = {
        "user_id": faker.random_number(digits=2),
        "user_name": faker.name(),
    }

    http_request = HttpRequest(query=attribute)

    http_response = find_user_controller.route(http_request)

    assert http_response.status_code == 200
    assert "error" not in http_response.body


def test_route_invalid_query_error_422():
    """Test route Find User"""

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)

    attribute = {
        "user_id": faker.random_number(digits=2),
    }

    http_request = HttpRequest(query=attribute)

    http_response = find_user_controller.route(http_request)

    assert http_response.status_code == 422
    assert "error" in http_response.body


def test_route_invalid_query_error_400():
    """Test route Find User"""

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)

    http_request = HttpRequest()
    http_response = find_user_controller.route(http_request)

    assert http_response.status_code == 400
    assert "error" in http_response.body
