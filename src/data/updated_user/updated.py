from typing import Type, Dict
from src.domain.use_cases import UpdateUser as UpdateUserInterface
from src.data.interface import UserRepositoryInterface as UserRepository
from src.domain.models import User


class UpdatedUser(UpdateUserInterface):
    """Class define use case to Updates User"""

    def __init__(self, user_repository: Type[UserRepository]) -> None:
        self.user_repository = user_repository

    def updated_user(
        self, user_id: int, user_name: str, old_password: str, new_data: dict = None
    ) -> Dict[bool, User]:
        """Update User by user id and user name
        :params - user_id: id to User
                - user_name: user name of User
                - old_password: password to User
                - new_data: dict with new data to updated
        :return - Dictionary with informations of the process
        """

        response = None
        validate_entry = (
            isinstance(user_id, int)
            and isinstance(user_name, str)
            and isinstance(old_password, str)
            and isinstance(new_data, dict)
        )

        if validate_entry:
            response = self.user_repository.updated_user(
                user_name=user_name,
                user_id=user_id,
                old_password=old_password,
                new_data=new_data,
            )

        if response:
            return {"Success": validate_entry, "Data": response}
        return {"Success": False, "Data": None}
