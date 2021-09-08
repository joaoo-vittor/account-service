from typing import Type, Dict
from src.domain.models import User
from src.data.interface import UserRepositoryInterface as UserRepository
from src.validators import validate_update_user_route


class UpdateUserSpy:
    """Update User Spy"""

    def __init__(self, user_repository: Type[UserRepository]) -> None:
        self.user_repository = user_repository
        self.update_user_params = {}

    def update_user(
        self, user_id: int, user_name: str, old_password: str, new_data: dict = None
    ) -> Dict[bool, User]:
        """Deactivate User
        :params
                -- user_id: id of the user
                -- user_name: user name of User

        :return - Dictionary with informations of the process
        """

        self.update_user_params["user_id"] = user_id
        self.update_user_params["user_name"] = user_name
        self.update_user_params["old_password"] = old_password
        self.update_user_params["new_data"] = new_data

        response = None

        validate_entry = validate_update_user_route(self.update_user_params)

        if validate_entry:
            response = User(id=1, user_name="", password="", email=None, active=0)

        return {"Success": validate_entry, "Data": response}
