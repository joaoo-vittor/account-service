from faker import Faker
from src.infra.test import UserRepositorySpy
from .updated import UpdatedUser


faker = Faker()


def test_updated_user():
    """Testing updated_user method"""

    user_repository = UserRepositorySpy()
    updated_user = UpdatedUser(user_repository)

    attributes = {
        "id": faker.random_number(digits=4),
        "password": faker.password(length=12),
        "user_name": faker.name(),
        "new_data": {"user_name": faker.name()},
    }

    response = updated_user.update_user(
        user_name=attributes["user_name"],
        old_password=attributes["password"],
        user_id=attributes["id"],
        new_data=attributes["new_data"],
    )

    # testing inputs
    assert user_repository.update_user_params["id"] == attributes["id"]
    assert user_repository.update_user_params["user_name"] == attributes["user_name"]
    assert user_repository.update_user_params["old_password"] == attributes["password"]
    assert user_repository.update_user_params["new_data"] == attributes["new_data"]

    # testing outputs
    assert response["Success"] is True
    assert response["Data"]
