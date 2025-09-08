from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import select
from app.schemas import UserCreate, UserUpdate, UserOut
from app.utils import hash_password, verify_password, prepare_to_send
from app.models import Users
from app.utils import get_all_columns


def get_all_users(
        session: Session,
):
    stmt = select(Users)
    result = session.scalars(stmt)
    return prepare_to_send(result, UserOut)


def add_user(
        session: Session,
        data: UserCreate,
) -> UserOut | None:
    """
    Добавить новую запись в таблицу Users

    Args:
        session: Активная SQLAlchemy-сессия.
        data: Данные новой записи (TicketCreate).

    Returns:
        TicketOut: Созданная запись.
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
    Обновить запись в таблице Users по id.

    Args:
        session: Активная SQLAlchemy-сессия.
        row_id: Идентификатор изменяемой записи.
        data: Новые данные (TicketCreate).

    Returns:
        TicketOut: Обновлённая запись.
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
    Удалить запись из таблицы Users по id.

    Args:
        session: Активная SQLAlchemy-сессия.
        instance_id: Идентификатор удаляемой записи.

    Returns:
        bool: True если запись была удалена, False если запись не найдена.
    """
    instance = session.get(Users, instance_id)
    if not instance:
        return False
    session.delete(instance)
    session.commit()
    return True
