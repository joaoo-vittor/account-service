from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm.exc import NoResultFound
from src.data.interface import UserRepositoryInterface
from src.domain.models import User
from src.infra.config import DBConnectionHandler
from src.infra.entites import Users as UserModel
from src.settings import HASH
from src.queue import publish


class UserRepository(UserRepositoryInterface):
    """Class to manage User Repository"""

    @classmethod
    def inserted_user(cls, user_name: str, password: str):
        """Insert data in user entity
        :params
                -- name: person name
                -- password: user password

        :return - tuple with new user inserted
        """

        with DBConnectionHandler() as connection:
            try:
                password = generate_password_hash(password=password).split(HASH)[1]

                new_user = UserModel(user_name=user_name, password=password)
                connection.session.add(new_user)
                connection.session.commit()

                user = {
                    "id": new_user.id,
                    "user_name": new_user.user_name,
                    "password": new_user.password,
                    "email": new_user.email,
                    "active": new_user.active,
                    "type": new_user.type,
                }

                publish("created_user", user)

                return User(
                    **user,
                )

            except:
                connection.session.rollback()
                raise
            finally:
                connection.session.close()

        return None

    @classmethod
    def selected_user(cls, user_name: str = None, user_id: int = None) -> User:
        """Select data in user entity by id and/or name
        :params
                -- user_id: Id of the registry
                -- user_name: User name

        :return - Users selected
        """
        try:
            data = None

            if user_id and not user_name:
                with DBConnectionHandler() as connection:
                    data = (
                        connection.session.query(UserModel).filter_by(id=user_id).one()
                    )

            if not user_id and user_name:
                with DBConnectionHandler() as connection:
                    data = (
                        connection.session.query(UserModel)
                        .filter_by(user_name=user_name)
                        .one()
                    )

            if user_id and user_name:
                with DBConnectionHandler() as connection:
                    data = (
                        connection.session.query(UserModel)
                        .filter_by(user_name=user_name, id=user_id)
                        .one()
                    )

            return User(
                id=data.id,
                user_name=data.user_name,
                password=data.password,
                email=data.email,
                active=data.active,
                type=data.type,
            )

        except NoResultFound:
            return None
        except Exception as e:
            connection.session.rollback()
            raise
        finally:
            connection.session.close()

    @classmethod
    def updated_user(
        cls,
        user_name: str,
        user_id: int,
        old_password: str,
        new_data: dict = None,
    ) -> bool:
        """Update data of the user on database
        :params
                -- user_id: Id of the registry
                -- user_name: User name
                -- old_password: Old password to verify
                -- new_data: dict with new params to update

        :return - Boolean to Users updated
        """
        try:
            if new_data and user_id and user_name and old_password:
                with DBConnectionHandler() as connection:

                    user_verify = (
                        connection.session.query(UserModel)
                        .filter_by(id=user_id, user_name=user_name)
                        .one()
                    )

                    if "active" in new_data.keys():
                        new_data.pop("active")

                    pwhash = f"{HASH}{user_verify.password}"
                    if check_password_hash(pwhash, old_password):
                        connection.session.query(UserModel).filter_by(
                            id=user_id, user_name=user_name
                        ).update(new_data, synchronize_session=False)
                        connection.session.commit()

                        return True

                return None

        except NoResultFound:
            return {}
        except:
            connection.session.rollback()
            raise
        finally:
            connection.session.close()

    @classmethod
    def deactivate_user(cls, user_name: str, user_id: int, password: str) -> bool:
        """Deactivate user of database
        :params
                -- user_id: Id of the registry
                -- user_name: User name
                -- password: password to verify

        :return - Boolean to Users deactivate
        """
        try:
            if user_id and user_name and password:
                with DBConnectionHandler() as connection:
                    user_verify = (
                        connection.session.query(UserModel)
                        .filter_by(id=user_id, user_name=user_name)
                        .one()
                    )

                    pwhash = f"{HASH}{user_verify.password}"
                    if check_password_hash(pwhash, password):
                        connection.session.query(UserModel).filter_by(
                            id=user_id, user_name=user_name
                        ).update({"active": 0}, synchronize_session=False)
                        connection.session.commit()
                        return True

            return None

        except NoResultFound:
            return None
        except:
            connection.session.rollback()
            raise
        finally:
            connection.session.close()

    @classmethod
    def reactivate_user(self, user_name: str, password: str) -> bool:
        """Activate user of database
        :params
                -- user_name: User name
                -- password: password to verify

        :return
                -- Boolean to Users activate
        """
        try:
            if user_name and password:
                with DBConnectionHandler() as connection:
                    user_verify = (
                        connection.session.query(UserModel)
                        .filter_by(user_name=user_name)
                        .one()
                    )

                    pwhash = f"{HASH}{user_verify.password}"
                    if check_password_hash(pwhash, password):
                        connection.session.query(UserModel).filter_by(
                            user_name=user_name
                        ).update({"active": 1}, synchronize_session=False)
                        connection.session.commit()
                        return True

            return None

        except NoResultFound:
            return None
        except:
            connection.session.rollback()
            raise
        finally:
            connection.session.close()
