from sqlalchemy.orm import Session
from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlalchemy import asc, desc
from typing import Sequence
from app.schemas import TicketCreate, TicketOut
from app.utils.sqlalchemy_helpers import is_valid_column_for_model
from app.models import Tickets


def get_rows(
        session: Session,
        filters: dict[InstrumentedAttribute, Sequence[int | str] | int | str] | None = None,
        sorting: Sequence[tuple[InstrumentedAttribute, bool]] | tuple[InstrumentedAttribute, bool] | None = None,
):
    """
    Получить строки из таблицы Tickets с фильтрацией и сортировкой.

    Args:
        session: Активная SQLAlchemy-сессия.
        filters: Словарь {колонка: значение или список значений} для фильтрации (по условию IN).
        sorting: Кортеж или список кортежей (колонка, bool), где bool — False=ASC, True=DESC.

    Returns:
        list[TicketOut]: Список строк валидационной модели TicketOut.

    Raises:
        TypeError: Если сортировка или её флаг имеют неверный тип.
        ValueError: Если колонка не принадлежит Tickets или значение невалидно.
    """
    if sorting:
        if not isinstance(sorting, (list, tuple)):
            raise TypeError(f"Значением сортировки ожидается кортеж или список кортежей, а не {type(sorting)}.")
        elif not isinstance(sorting[0], (list, tuple)):
            sorting = (sorting, )

    query = session.query(Tickets)

    if filters:
        for column, values in filters.items():
            if not is_valid_column_for_model(column, Tickets):
                raise ValueError(f"В ключе для фильтрации ожидается колонка таблицы {Tickets.__name__}. "
                                 f"Вы передали {type(column)}, а именно {column}.")
            if not isinstance(values, (list, tuple)):
                values = (values,)

            for value in values:
                if not isinstance(value, column.type.python_type):
                    raise ValueError(f'Значением колонки {column} должен быть класс {column.type.python_type},'
                                     f' а не {type(value)} ({value}).')

            query = query.filter(column.in_(values))

    sorters = []
    if sorting:
        for item in sorting:
            if len(item) != 2:
                raise ValueError(f'В одном кортеже сортировки ожидается только одна колонка.')
            if not isinstance(item[1], bool):
                raise TypeError(f'Вторым значением кортежей всегда должен быть тип bool.')
            column = item[0]
            sorting_type = item[1]
            if not is_valid_column_for_model(column, Tickets):
                raise ValueError(f"В ключе для сортировки ожидается колонка таблицы {Tickets.__name__}. "
                                 f"Вы передали {type(column)}, а именно {column}.")

            if sorting_type == False:
                sorters.append(asc(column))
            else:
                sorters.append(desc(column))

        query = query.order_by(*sorters)

    return [TicketOut.model_validate(row) for row in query.all()]


def add_row(
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


def change_row(
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


def delete_row(
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
