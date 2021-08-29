from typing import Dict, Type
from src.domain.models import User
from src.domain.use_cases import RegistryUser as RegistryUserInterface
from src.data.interface import UserRepositoryInterface as UserRepository


class RegistryUser(RegistryUserInterface):
    """class define use case to Regsitry User"""

    def __init__(self, user_repository: Type[UserRepository]) -> None:
        self.user_repository = user_repository

    def registry_user(self, user_name: str, password: str) -> Dict[bool, User]:
        """Select User by user id and user name
        :params - user_name: user name of User
                - password: password to User
        :return - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(user_name, str) and isinstance(password, str)

        if validate_entry:
            response = self.user_repository.inserted_user(
                user_name=user_name, password=password
            )

        return {"Success": validate_entry, "Data": response}
