from typing import Type, Dict
from src.domain.models import User
from src.data.interface import UserRepositoryInterface as UserRepository


class FindUserSpy:
    """Find User Spy"""

    def __init__(self, user_repository: Type[UserRepository]) -> None:
        self.user_repository = user_repository
        self.find_user_params = {}

    def by_id_and_name(self, user_id: int, user_name: str) -> Dict[bool, User]:
        """Deactivate User
        :params
                -- user_id: id of the user
                -- user_name: user name of User

        :return - Dictionary with informations of the process
        """

        self.find_user_params["user_id"] = user_id
        self.find_user_params["user_name"] = user_name

        response = None

        validate_entry = isinstance(user_id, int) and isinstance(user_name, str)

        if validate_entry:
            response = User(id=1, user_name="", password="", email=None, active=0)

        return {"Success": validate_entry, "Data": response}
