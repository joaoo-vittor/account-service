from faker import Faker

from src.infra.config import DBConnectionHandler
from .user_repository import UserRepository


faker = Faker()
user_repository = UserRepository()
db_connection = DBConnectionHandler()


def test_insert_user():
    """insert one user on database"""

    name = faker.name()
    password = faker.word()

    new_user = user_repository.inserted_user(user_name=name, password=password)

    engine = db_connection.get_engine()
    query_user = engine.execute(
        "SELECT * FROM users WHERE id='{}';".format(new_user.id)
    ).fetchone()

    engine.execute("DELETE FROM users WHERE id='{}'".format(new_user.id))

    assert new_user.id == query_user.id
    assert new_user.user_name == query_user.user_name
    assert new_user.password == query_user.password


def test_select_user_to_user_name():
    """select one user on database"""

    user_name = faker.name()
    password = faker.word()

    new_user = user_repository.inserted_user(user_name=user_name, password=password)

    selected_user = user_repository.selected_user(user_name=new_user.user_name)

    engine = db_connection.get_engine()
    query_user = engine.execute(
        "SELECT * FROM users WHERE user_name='{}';".format(new_user.user_name)
    ).fetchone()

    engine.execute("DELETE FROM users WHERE id='{}'".format(new_user.id))

    assert selected_user.id == query_user.id
    assert selected_user.user_name == query_user.user_name
    assert selected_user.user_name == user_name
    assert query_user.user_name == user_name
    assert new_user.user_name == user_name
    assert new_user.user_name == selected_user.user_name
    assert new_user.user_name == query_user.user_name
    assert new_user.id == query_user.id
    assert new_user.id == selected_user.id


def test_select_user_to_user_id():
    """select one user on database"""

    user_name = faker.name()
    password = faker.word()

    new_user = user_repository.inserted_user(user_name=user_name, password=password)

    selected_user = user_repository.selected_user(user_id=new_user.id)

    engine = db_connection.get_engine()
    query_user = engine.execute(
        "SELECT * FROM users WHERE id='{}';".format(new_user.id)
    ).fetchone()

    engine.execute("DELETE FROM users WHERE id='{}'".format(new_user.id))

    assert selected_user.id == query_user.id
    assert selected_user.id == new_user.id
    assert query_user.id == new_user.id
    assert selected_user.user_name == query_user.user_name


def test_select_user_to_user_id_and_user_name():
    """select one user on database"""

    user_name = faker.name()
    password = faker.word()

    new_user = user_repository.inserted_user(user_name=user_name, password=password)

    selected_user = user_repository.selected_user(
        user_id=new_user.id, user_name=user_name
    )

    engine = db_connection.get_engine()
    query_user = engine.execute(
        "SELECT * FROM users WHERE id='{}' AND user_name='{}';".format(
            new_user.id, user_name
        )
    ).fetchone()

    engine.execute("DELETE FROM users WHERE id='{}'".format(new_user.id))

    assert selected_user.id == query_user.id
    assert selected_user.id == new_user.id
    assert query_user.id == new_user.id
    assert selected_user.user_name == query_user.user_name
    assert selected_user.user_name == user_name
    assert query_user.user_name == user_name


def test_update_user_name():
    """update user name"""

    user_name = faker.name()
    password = faker.word()
    num_aleatorio = faker.random_number(digits=10)
    updated_params = {"user_name": f"joaoo-vittor{num_aleatorio}"}

    new_user = user_repository.inserted_user(user_name=user_name, password=password)

    update_new_user_name = user_repository.updated_user(
        user_id=new_user.id,
        user_name=new_user.user_name,
        old_password=new_user.password,
        new_data=updated_params,
    )

    engine = db_connection.get_engine()
    query_user = engine.execute(
        "SELECT * FROM users WHERE id='{}';".format(new_user.id)
    ).fetchone()

    engine.execute("DELETE FROM users WHERE id='{}'".format(new_user.id))

    assert update_new_user_name == True
    assert query_user.id == new_user.id
    assert query_user.user_name == updated_params["user_name"]


def test_update_user_name_and_password_and_email():
    """update user name and password and email"""

    user_name = faker.name()
    password = faker.word()
    num_aleatorio = faker.random_number(digits=10)
    updated_params = {
        "user_name": f"joaoo-vittor{num_aleatorio}",
        "email": f"joaoo-vittor{num_aleatorio}@gmail.com",
        "password": f"joaovitor_{num_aleatorio}",
    }

    new_user = user_repository.inserted_user(user_name=user_name, password=password)

    update_new_user_name = user_repository.updated_user(
        user_id=new_user.id,
        user_name=new_user.user_name,
        old_password=new_user.password,
        new_data=updated_params,
    )

    engine = db_connection.get_engine()
    query_user = engine.execute(
        "SELECT * FROM users WHERE id='{}';".format(new_user.id)
    ).fetchone()

    engine.execute("DELETE FROM users WHERE id='{}'".format(new_user.id))

    assert update_new_user_name == True
    assert query_user.id == new_user.id
    assert query_user.user_name == updated_params["user_name"]
    assert query_user.email == updated_params["email"]
    assert query_user.password == updated_params["password"]
    assert new_user.password == password


def test_deactivate_user():
    """deactivate user"""

    user_name = faker.name()
    password = faker.word()

    new_user = user_repository.inserted_user(user_name=user_name, password=password)

    deactivate_user = user_repository.deactivate_user(
        user_name=new_user.user_name, user_id=new_user.id, password=new_user.password
    )

    engine = db_connection.get_engine()
    query_user = engine.execute(
        "SELECT * FROM users WHERE id='{}';".format(new_user.id)
    ).fetchone()

    engine.execute("DELETE FROM users WHERE id='{}'".format(new_user.id))

    assert deactivate_user == True
    assert new_user.active == 1
    assert query_user.active == 0
    assert new_user.active != query_user.active


def test_activate_user():
    """activate user"""

    user_name = faker.name()
    password = faker.word()

    new_user = user_repository.inserted_user(user_name=user_name, password=password)

    deactivate_user = user_repository.deactivate_user(
        user_name=new_user.user_name, user_id=new_user.id, password=new_user.password
    )

    activate_user = user_repository.reactivate_user(
        user_name=new_user.user_name, user_id=new_user.id, password=new_user.password
    )

    engine = db_connection.get_engine()
    query_user = engine.execute(
        "SELECT * FROM users WHERE id='{}';".format(new_user.id)
    ).fetchone()

    engine.execute("DELETE FROM users WHERE id='{}'".format(new_user.id))

    assert deactivate_user == True
    assert activate_user == True
    assert new_user.active == query_user.active
