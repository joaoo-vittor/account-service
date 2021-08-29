from src.domain.models import User
from src.domain.test import mock_users


class UserRepositorySpy:
    """Spy to User Repository"""

    def __init__(self):
        self.insert_user_params = {}
        self.select_user_params = {}
        self.update_user_params = {}
        self.deactive_user_params = {}
        self.reactive_user_params = {}

    def inserted_user(self, user_name: str, password: str):
        """Spy to all the attributes"""

        self.insert_user_params["user_name"] = user_name
        self.insert_user_params["password"] = password

        return mock_users()

    def selected_user(self, user_name: str = None, user_id: int = None) -> User:
        """Spy to all the attributes"""

        self.select_user_params["id"] = user_id
        self.select_user_params["user_name"] = user_name

        return mock_users()

    def updated_user(
        self,
        user_name: str,
        user_id: int,
        old_password: str,
        new_data: dict = None,
    ) -> bool:
        """Spy to all the attributes"""

        self.update_user_params["id"] = user_id
        self.update_user_params["user_name"] = user_name
        self.update_user_params["old_password"] = old_password
        self.update_user_params["new_data"] = new_data

        return mock_users()

    def deactivate_user(self, user_name: str, user_id: int, password: str) -> bool:
        """Spy to all the attributes"""

        self.deactive_user_params["id"] = user_id
        self.deactive_user_params["user_name"] = user_name
        self.deactive_user_params["password"] = password

        return mock_users()

    def reactivate_user(self, user_name: str, user_id: int, password: str) -> bool:
        """Spy to all the attributes"""

        self.reactive_user_params["id"] = user_id
        self.reactive_user_params["user_name"] = user_name
        self.reactive_user_params["password"] = password

        return mock_users()
