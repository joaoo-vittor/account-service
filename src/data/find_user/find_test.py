from faker import Faker
from src.infra.test import UserRepositorySpy
from .find import FindUser


faker = Faker()


def test_by_id_and_name():
    """Testing by_id_and_name method"""

    user_repository = UserRepositorySpy()
    find_user = FindUser(user_repository)

    attributes = {"id": faker.random_number(digits=2), "user_name": faker.name()}

    response = find_user.by_id_and_name(
        user_id=attributes["id"], user_name=attributes["user_name"]
    )

    # testing inputs
    assert user_repository.select_user_params["id"] == attributes["id"]
    assert user_repository.select_user_params["user_name"] == attributes["user_name"]

    # testing outputs
    assert response["Success"] is True
    assert response["Data"]
