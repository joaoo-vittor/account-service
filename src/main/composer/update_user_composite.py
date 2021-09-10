from src.main.interface import RouteInterface
from src.presenters.controllers import UpdateUserController
from src.infra.repo import UserRepository
from src.data.updated_user import UpdatedUser


def update_user_composite() -> RouteInterface:
    """Composing Update User Route
    :param - None
    :return - Object with Update User Route
    """

    update_user_use_case = UpdatedUser(UserRepository())
    update_user_controller = UpdateUserController(update_user_use_case)

    return update_user_controller
