from abc import ABC, abstractclassmethod
from typing import Dict
from src.domain.models import User


class UpdateUser(ABC):
    """Interface to UpdateUser use case"""

    @abstractclassmethod
    def updated_user(
        cls, user_id: int, user_name: str, old_password: str, new_data: dict = None
    ) -> Dict[bool, User]:
        """Specific Case"""

        raise Exception("Should implement method: updated_user")
