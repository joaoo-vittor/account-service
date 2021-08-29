from faker import Faker
from src.domain.models import User


faker = Faker()


def mock_users(has_email: bool = False, is_active: bool = True) -> User:
    """Mock to user"""
    return User(
        id=faker.random_number(digits=5),
        user_name=faker.name(),
        password=faker.word(),
        email=has_email if faker.email() else None,
        active=is_active if 1 else 0,
    )
