from src.main.interface import RouteInterface
from src.presenters.controllers import FindUserController
from src.infra.repo import UserRepository
from src.data.find_user import FindUser


def find_user_composite() -> RouteInterface:
    """Composing Find User Route
    :param - None
    :return - Object with Find User Route
    """

    find_user_use_case = FindUser(UserRepository())
    find_user_controller = FindUserController(find_user_use_case)

    return find_user_controller
