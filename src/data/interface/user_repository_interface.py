from abc import ABC, abstractmethod
from src.infra.entites import Users


class UserRepositoryInterface(ABC):
    """class define interface to UserRepository"""

    @abstractmethod
    def inserted_user(self, user_name: str, password: str):
        """method to insert user on database"""
        raise Exception("method not implemented")

    @abstractmethod
    def selected_user(self, user_name: str, user_id: int) -> Users:
        """method to select one user on database"""
        raise Exception("method not implemented")

    @abstractmethod
    def updated_user(
        self,
        user_name: str,
        user_id: int,
        old_password: str,
        new_data: dict = {},
    ) -> bool:
        """method to update one user on database"""
        raise Exception("method not implemented")

    @abstractmethod
    def deactivate_user(self, user_name: str, user_id: int, password: str) -> bool:
        """method to deactivate one user on database"""
        raise Exception("method not implemented")

    @abstractmethod
    def reactivate_user(self, user_name: str, user_id: int, password: str) -> bool:
        """method to reactivate on user on database"""
        raise Exception("method not implemented")
