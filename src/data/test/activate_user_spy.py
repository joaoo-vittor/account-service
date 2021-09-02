from typing import Type, Dict
from src.domain.models import User
from src.data.interface import UserRepositoryInterface as UserRepository


class ActivateUserSpy:
    """Activate User Spy"""

    def __init__(self, activate_user_repository: Type[UserRepository]) -> None:
        self.activate_user_repository = activate_user_repository
        self.activate_user_params = {}

    def activate_user(
        self, user_id: int, user_name: str, password: str
    ) -> Dict[bool, User]:
        """Activate User
        :params - user_id: id of the user
                - user_name: user name of User
                - password: password to verify deactivate
        :return - Dictionary with informations of the process
        """

        self.activate_user_params["user_id"] = user_id
        self.activate_user_params["user_name"] = user_name
        self.activate_user_params["password"] = password

        response = None

        validate_entry = (
            isinstance(user_id, int)
            and isinstance(user_name, str)
            and isinstance(password, str)
        )

        if validate_entry:
            response = User(id=1, user_name="", password="", email=None, active=1)

        return {"Success": validate_entry, "Data": response}
