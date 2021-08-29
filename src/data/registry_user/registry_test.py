from faker import Faker
from src.infra.test import UserRepositorySpy
from .registry import RegistryUser


faker = Faker()


def test_registry_user():
    """Testing registry_user method"""

    user_repository = UserRepositorySpy()
    registry_user = RegistryUser(user_repository)

    attributes = {"password": faker.password(length=12), "user_name": faker.name()}

    response = registry_user.registry_user(
        user_name=attributes["user_name"], password=attributes["password"]
    )

    # testing inputs
    assert user_repository.insert_user_params["password"] == attributes["password"]
    assert user_repository.insert_user_params["user_name"] == attributes["user_name"]

    # testing outputs
    assert response["Success"] is True
    assert response["Data"]
