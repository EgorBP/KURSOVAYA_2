from sqlalchemy.orm import Session
from sqlalchemy.orm.attributes import InstrumentedAttribute
from typing import Sequence
from app.schemas import TicketCreate, TicketOut, PopularPerformanceOut, PopularTheatreOut
from app.utils.sqlalchemy_helpers import is_valid_column_for_model, prepare_to_send
from app.models import Tickets


def add_user(
        session: Session,
        data: TicketCreate,
):
    """
    Добавить новую запись в таблицу Tickets.

    Args:
        session: Активная SQLAlchemy-сессия.
        data: Данные новой записи (TicketCreate).

    Returns:
        TicketOut: Созданная запись.
    """
    data = Tickets(
    data=data.data,
    theatre_name=data.theatre_name,
    performance_name=data.performance_name,
    tickets_count=data.tickets_count,
    )
    session.add(data)
    session.commit()
    session.refresh(data)
    return TicketOut.model_validate(data)


def change_user(
        session: Session,
        row_id: int,
        data: TicketCreate,
):
    """
    Обновить запись в таблице Tickets по id.

    Args:
        session: Активная SQLAlchemy-сессия.
        row_id: Идентификатор изменяемой записи.
        data: Новые данные (TicketCreate).

    Returns:
        TicketOut: Обновлённая запись.
    """
    row = session.get(Tickets, row_id)
    row.data = data.data
    row.theatre_name = data.theatre_name
    row.performance_name = data.performance_name
    row.tickets_count = data.tickets_count
    session.commit()
    session.refresh(row)
    return TicketOut.model_validate(row)


def delete_user(
        session: Session,
        instance_id: int
):
    """
    Удалить запись из таблицы Tickets по id.

    Args:
        session: Активная SQLAlchemy-сессия.
        instance_id: Идентификатор удаляемой записи.

    Returns:
        bool: True если запись была удалена, False если запись не найдена.
    """
    instance = session.get(Tickets, instance_id)
    if not instance:
        return False
    session.delete(instance)
    session.commit()
    return True
