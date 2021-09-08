from typing import Type, Dict
from src.domain.models import User
from src.data.interface import UserRepositoryInterface as UserRepository


class RegistryUserSpy:
    """Registry User Spy"""

    def __init__(self, user_repository: Type[UserRepository]) -> None:
        self.user_repository = user_repository
        self.registry_user_params = {}

    def registry_user(self, user_name: str, password: str) -> Dict[bool, User]:
        """Registry User
        :params
                -- user_name: user name of User
                -- password: password of the user

        :return - Dictionary with informations of the process
        """

        self.registry_user_params["user_name"] = user_name
        self.registry_user_params["password"] = password

        response = None

        validate_entry = isinstance(password, str) and isinstance(user_name, str)

        if validate_entry:
            response = User(id=1, user_name="", password="", email=None, active=0)

        return {"Success": validate_entry, "Data": response}
