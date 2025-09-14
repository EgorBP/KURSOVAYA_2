from app.crud import tickets
from app.database import SessionLocal
from sqlalchemy.orm.attributes import InstrumentedAttribute
from typing import Sequence
from app.schemas import TicketCreate, TicketOut, TicketUpdate, PopularPerformanceOut, PopularTheatreOut
from nicegui import ui


def get_all_data(
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


def delete_instance(instance_id: int, table: ui.table | None = None) -> bool:
    with SessionLocal() as session:
        result = tickets.delete_ticket_row(
            session=session,
            instance_id=instance_id,
        )
        if table and result:
            data = tickets.get_tickets_data(session=session)
    if result:
        ui.notify("✅ Пользователь успешно удален ✅")
        if table:
            table.rows = [t.model_dump() for t in data]
            table.update()
    else:
        ui.notify('❌ Пользователь не найден ❌')
    return result
