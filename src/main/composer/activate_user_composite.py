from src.main.interface import RouteInterface
from src.presenters.controllers import ActivateController
from src.infra.repo import UserRepository
from src.data.activate_user import ActivateUser


def activate_user_composite() -> RouteInterface:
    """Composing Activate User Route
    :param - None
    :return - Object with Update User Route
    """

    activate_user_use_case = ActivateUser(UserRepository())
    activate_user_controller = ActivateController(activate_user_use_case)

    return activate_user_controller
