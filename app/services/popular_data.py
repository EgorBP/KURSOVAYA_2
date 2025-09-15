from app.crud import tickets
from app.database import SessionLocal
from app.schemas import PopularTheatreOut, PopularPerformanceOut
from nicegui import ui


def get_popular_theaters_data() -> list[PopularTheatreOut]:
    with SessionLocal() as session:
        data = tickets.get_popular_theaters(
            session=session,
        )
    return data


def refresh_table_popular_theaters(
        month: int,
        table: ui.table,
) -> bool:
    with SessionLocal() as session:
        data = tickets.get_popular_theaters(
            session=session,
            month=month,
        )
    if data:
        ui.notify("✅ Данные для выбранного месяца успешно обновлены ✅")
        table.rows = [t.model_dump() for t in data]
        table.update()
        return True
    else:
        ui.notify('❌ Данные не найдены ❌')
        table.rows.clear()
        table.update()
        return False


def get_popular_performances_data() -> list[PopularPerformanceOut]:
    with SessionLocal() as session:
        data = tickets.get_popular_performances(
            session=session,
        )
    return data


def refresh_table_popular_performances(
        month: int,
        table: ui.table,
) -> bool:
    with SessionLocal() as session:
        data = tickets.get_popular_performances(
            session=session,
            month=month,
        )
    if data:
        ui.notify("✅ Данные для выбранного месяца успешно обновлены ✅")
        table.rows = [t.model_dump() for t in data]
        table.update()
        return True
    else:
        ui.notify('❌ Данные не найдены ❌')
        table.rows.clear()
        table.update()
        return False
