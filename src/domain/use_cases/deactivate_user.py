from abc import ABC, abstractclassmethod
from typing import Dict
from src.domain.models import User


class DeactivateUser(ABC):
    """Interface to DeactivateUser use case"""

    @abstractclassmethod
    def deactivate_user(
        cls, user_id: int, user_name: str, password: str
    ) -> Dict[bool, User]:
        """Specific Case"""

        raise Exception("Should implement method: deactivate_user")
