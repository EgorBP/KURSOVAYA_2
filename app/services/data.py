from app.crud import tickets, users
from app.database import SessionLocal
from sqlalchemy.orm.attributes import InstrumentedAttribute
from typing import Sequence
from app.schemas import TicketOut, UserOut, TicketUpdate
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


def save_edited_ticket_data(
        ticket: dict,
        table: ui.table | None = None,
        filters: dict[InstrumentedAttribute, Sequence[int | str] | int | str] | None = None,
        sorting: Sequence[tuple[InstrumentedAttribute, bool]] | tuple[InstrumentedAttribute, bool] | None = None,
) -> bool:
    ticket_id = int(ticket['id'])
    with SessionLocal() as session:
        result = tickets.change_ticket_row(
            session=session,
            row_id=ticket_id,
            data=TicketUpdate(
                date=ticket['date'],
                theatre_name=ticket['theatre_name'],
                performance_name=ticket['performance_name'],
                tickets_count=ticket['tickets_count']
            ),
        )
        if table and result:
            data = tickets.get_tickets_data(
                session=session,
                filters=filters,
                sorting=sorting,
            )
    if result:
        ui.notify('✅ Поле успешно изменено ✅')
        if table:
            table.rows = [t.model_dump() for t in data]
            table.update()
        return True
    else:
        ui.notify('❌ Поле не найдено ❌')
        return False


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
