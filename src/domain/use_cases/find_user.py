from abc import ABC, abstractclassmethod
from typing import Dict
from src.domain.models import User


class FindUser(ABC):
    """Interface to FindUser use case"""

    @abstractclassmethod
    def by_id_and_name(cls, user_id: int, user_name: str) -> Dict[bool, User]:
        """Specific Case"""

        raise Exception("Should implement method: by_id_and_name")

    @abstractclassmethod
    def by_id(cls, user_id: int) -> Dict[bool, User]:
        """Specific Case"""

        raise Exception("Should implement method: by_id")

    @abstractclassmethod
    def by_name(cls, user_name: str) -> Dict[bool, User]:
        """Specific Case"""

        raise Exception("Should implement method: by_name")
