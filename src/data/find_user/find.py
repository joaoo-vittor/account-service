from typing import Type, Dict
from src.domain.models import User
from src.domain.use_cases import FindUser as FindUserInterface
from src.data.interface import UserRepositoryInterface as UserRepository


class FindUser(FindUserInterface):
    """Class to define use case Find User"""

    def __init__(self, user_repository: Type[UserRepository]) -> None:
        self.user_repository = user_repository

    def by_id_and_name(self, user_id: int, user_name: str) -> Dict[bool, User]:
        """Select User by user id and user name
        :params - user_id: id of the user
                - user_name: user name of User
        :return - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = self.user_repository.selected_user(
                user_id=user_id, user_name=user_name
            )
        if response:
            return {"Success": validate_entry, "Data": response}
        return {"Success": False, "Data": response}
