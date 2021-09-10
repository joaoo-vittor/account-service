from src.main.interface import RouteInterface
from src.presenters.controllers import DeactivateUserController
from src.infra.repo import UserRepository
from src.data.deactivate_user import DeactivateUser


def deactivate_user_composite() -> RouteInterface:
    """Composing Deactivate User Route
    :param - None
    :return - Object with Update User Route
    """

    deactivate_user_use_case = DeactivateUser(UserRepository())
    deactivate_user_controller = DeactivateUserController(deactivate_user_use_case)

    return deactivate_user_controller
