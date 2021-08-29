from faker import Faker
from src.infra.test import UserRepositorySpy
from .deactivate import DeactivateUser


faker = Faker()


def test_deactivate_user():
    """Testing deactivate_user method"""

    user_repository = UserRepositorySpy()
    deactivate_user_use_case = DeactivateUser(user_repository)

    attributes = {
        "id": faker.random_number(digits=2),
        "user_name": faker.name(),
        "password": faker.password(length=12),
    }

    response = deactivate_user_use_case.deactivate_user(
        user_id=attributes["id"],
        user_name=attributes["user_name"],
        password=attributes["password"],
    )

    # testing inputs
    assert user_repository.deactive_user_params["id"] == attributes["id"]
    assert user_repository.deactive_user_params["user_name"] == attributes["user_name"]
    assert user_repository.deactive_user_params["password"] == attributes["password"]

    # testing outputs
    assert response["Success"] is True
    assert response["Data"]
