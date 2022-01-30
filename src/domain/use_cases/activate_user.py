from abc import ABC, abstractclassmethod
from typing import Dict
from src.domain.models import User


class ActivateUser(ABC):
    """Interface to ActivateUser use case"""

    @abstractclassmethod
    def activate_user(cls, user_name: str, password: str) -> Dict[bool, User]:
        """Specific Case"""

        raise Exception("Should implement method: deactivate_user")
