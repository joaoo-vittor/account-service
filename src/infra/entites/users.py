from sqlalchemy import Column, String, Integer, DateTime, Boolean
from sqlalchemy.sql import func
from src.infra.config import Base


class Users(Base):
    """Users Entity"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=True, unique=True)
    password = Column(String(200), nullable=False)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self) -> str:
        return f"User [user_name={self.user_name}]"

    def __eq__(self, o: object) -> bool:
        if (
            self.id == o.id
            and self.user_name == o.user_name
            and self.password == o.password
        ):
            return True
        return False
