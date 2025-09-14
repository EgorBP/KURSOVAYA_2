from app.crud import tickets, users
from app.database import SessionLocal
from sqlalchemy.orm.attributes import InstrumentedAttribute
from typing import Sequence
from app.schemas import TicketOut, UserOut
from nicegui import ui


def get_all_tickets_data(
        filters: dict[InstrumentedAttribute, Sequence[int | str] | int | str] | None = None,
        sorting: Sequence[tuple[InstrumentedAttribute, bool]] | tuple[InstrumentedAttribute, bool] | None = None,
) -> list[TicketOut]:
    with SessionLocal() as session:
        data = tickets.get_tickets_data(
            session=session,
            filters=filters,
            sorting=sorting,
        )
    return data


def delete_on_tickets(
        instance_id: int,
        table: ui.table | None = None,
        filters: dict[InstrumentedAttribute, Sequence[int | str] | int | str] | None = None,
        sorting: Sequence[tuple[InstrumentedAttribute, bool]] | tuple[InstrumentedAttribute, bool] | None = None,
) -> bool:
    with SessionLocal() as session:
        result = tickets.delete_ticket_row(
            session=session,
            instance_id=instance_id,
        )
        if table and result:
            data = tickets.get_tickets_data(
                session=session,
                filters=filters,
                sorting=sorting,
            )
    if result:
        ui.notify("✅ Поле успешно удалено ✅")
        if table:
            table.rows = [t.model_dump() for t in data]
            table.update()
    else:
        ui.notify('❌ Поле не найдено ❌')
    return result


def get_all_users_data() -> list[UserOut]:
    with SessionLocal() as session:
        data = users.get_all_users(
            session=session,
        )
    return data


def delete_on_users(instance_id: int, table: ui.table | None = None) -> bool:
    with SessionLocal() as session:
        result = users.delete_user(
            session=session,
            instance_id=instance_id,
        )
        if table and result:
            data = users.get_all_users(session=session)
    if result:
        ui.notify("✅ Пользователь успешно удален ✅")
        if table:
            table.rows = [t.model_dump() for t in data]
            table.update()
    else:
        ui.notify('❌ Пользователь не найден ❌')
    return result
