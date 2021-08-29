from abc import ABC, abstractclassmethod
from typing import Dict
from src.domain.models import User


class RegistryUser(ABC):
    """Interface to RegistryUser use case"""

    @abstractclassmethod
    def registry_user(cls, user_name: str, password: str) -> Dict[bool, User]:
        """Specific Case"""

        raise Exception("Should implement method: registry_user")
