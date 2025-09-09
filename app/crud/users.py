from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import select
from app.schemas import UserCreate, UserUpdate, UserOut, UserLogin
from app.utils import hash_password, verify_password, prepare_to_send
from app.models import Users
from app.utils import get_all_columns


def validate_user_password(
        session: Session,
        data: UserLogin,
) -> bool | None:
    """
    Проверить корректность пароля пользователя.

    Args:
        session (Session): Активная SQLAlchemy-сессия.
        data (UserLogin): Данные для входа (username и password).

    Returns:
        bool | None:
            - True, если пароль верный.
            - False, если пароль неверный.
            - None, если пользователь с таким username не найден.
    """
    stmt = select(Users).where(Users.username == data.username)
    result = session.execute(stmt).fetchone()

    if not result:
        return None
    elif verify_password(data.password, result.password):
        return True
    else:
        return False


def get_all_users(
        session: Session,
) -> list[UserOut]:
    """
    Получить всех пользователей из таблицы Users.

    Args:
        session (Session): Активная SQLAlchemy-сессия.

    Returns:
        list[UserOut]: Список пользователей в формате UserOut.
    """
    stmt = select(Users)
    result = session.scalars(stmt)
    return prepare_to_send(result, UserOut)


def add_user(
        session: Session,
        data: UserCreate,
) -> UserOut | None:
    """
    Добавить нового пользователя в таблицу Users.

    Args:
        session (Session): Активная SQLAlchemy-сессия.
        data (UserCreate): Данные нового пользователя.

    Returns:
        UserOut | None: Созданная запись пользователя или None,
        если пользователь с таким username уже существует.
    """
    columns = get_all_columns(Users)

    stmt = insert(Users).values(
        username=data.username,
        password_hash=hash_password(data.password)
    ).on_conflict_do_nothing(
        index_elements=[Users.username],
    ).returning(*columns)

    result = session.execute(stmt).fetchone()
    if not result:
        return None

    session.commit()
    return UserOut.model_validate(result)


def change_user(
        session: Session,
        row_id: int,
        data: UserUpdate,
) -> UserOut:
    """
    Обновить пользователя в таблице Users по id.

    Args:
        session (Session): Активная SQLAlchemy-сессия.
        row_id (int): Идентификатор изменяемой записи.
        data (UserUpdate): Новые данные пользователя.

    Returns:
        UserOut: Обновлённая запись пользователя.
    """
    row = session.get(Users, row_id)
    row.username = data.username
    row.password_hash = hash_password(data.password)
    session.commit()
    session.refresh(row)
    return UserOut.model_validate(row)


def delete_user(
        session: Session,
        instance_id: int
) -> bool:
    """
    Удалить пользователя из таблицы Users по id.

    Args:
        session (Session): Активная SQLAlchemy-сессия.
        instance_id (int): Идентификатор удаляемой записи.

    Returns:
        bool: True, если пользователь был удалён, False — если не найден.
    """
    instance = session.get(Users, instance_id)
    if not instance:
        return False
    session.delete(instance)
    session.commit()
    return True
