from typing import Dict, Type
from src.data.interface import UserRepositoryInterface as UserRepository
from src.domain.models import User
from src.domain.use_cases import ActivateUser as ActivateUserInterface


class ActivateUser(ActivateUserInterface):
    """Class to define Activate User use case"""

    def __init__(self, user_repository: Type[UserRepository]) -> None:
        self.user_repository = user_repository

    def activate_user(
        self, user_id: int, user_name: str, password: str
    ) -> Dict[bool, User]:
        """Activate User
        :params - user_id: id of the user
                - user_name: user name of User
                - password: password to verify deactivate
        :return - Dictionary with informations of the process
        """

        response = None
        validate_entry = (
            isinstance(user_id, int)
            and isinstance(user_name, str)
            and isinstance(password, str)
        )

        if validate_entry:
            response = self.user_repository.reactivate_user(
                user_name=user_name, user_id=user_id, password=password
            )

        return {"Success": validate_entry, "Data": response}
