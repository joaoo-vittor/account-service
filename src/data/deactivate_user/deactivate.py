from typing import Type, Dict
from src.domain.models import User
from src.domain.use_cases import DeactivateUser as DeactivateUserInterface
from src.data.interface import UserRepositoryInterface as UserRepository


class DeactivateUser(DeactivateUserInterface):
    """Class to define Deactivate User use case"""

    def __init__(self, user_repository: Type[UserRepository]) -> None:
        self.user_repository = user_repository

    def deactivate_user(
        self, user_id: int, user_name: str, password: str
    ) -> Dict[bool, User]:
        """Select User by user id and user name
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
            response = self.user_repository.deactivate_user(
                user_name=user_name, user_id=user_id, password=password
            )

        return {"Success": validate_entry, "Data": response}
