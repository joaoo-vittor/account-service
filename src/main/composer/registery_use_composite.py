from src.main.interface import RouteInterface
from src.presenters.controllers import RegistryUserController
from src.infra.repo import UserRepository
from src.data.registry_user import RegistryUser


def registry_user_composite() -> RouteInterface:
    """Composing Registery User Route
    :param - None
    :return - Object with Register User Route
    """

    registry_user_use_case = RegistryUser(UserRepository())
    registry_user_controller = RegistryUserController(registry_user_use_case)

    return registry_user_controller
