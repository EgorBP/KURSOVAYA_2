from app.crud import tickets, users
from app.database import SessionLocal
from sqlalchemy.orm.attributes import InstrumentedAttribute
from typing import Sequence
from app.schemas import TicketOut, UserOut, TicketUpdate, UserUpdate
from nicegui import ui
from datetime import datetime
from app.decorators import required_role
from app.models import UserRole


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


@required_role(UserRole.ADMIN)
def save_edited_ticket_data(
        ticket: dict,
        table: ui.table | None = None,
        filters: dict[InstrumentedAttribute, Sequence[int | str] | int | str] | None = None,
        sorting: Sequence[tuple[InstrumentedAttribute, bool]] | tuple[InstrumentedAttribute, bool] | None = None,
) -> bool:
    ticket_id = int(ticket['id'])
    date = ticket['date']
    try:
        datetime.fromisoformat(date)
    except ValueError:
        try:
            day, month, year = date.split('.')
            date = f'{year}-{month}-{day}'
            datetime.fromisoformat(date)
        except ValueError:
            ui.notify(
                'Не верный формат даты',
                type='negative',
            )
            ui.notification(
                'Данные могли устареть, обновите страницу',
                type='info',
                actions=[{
                    "icon": 'refresh',
                    "color": "white",
                    "onclick": 'emitEvent("go_users_data")'
                }]
            )
            ui.on('go_users_data', lambda: ui.navigate.reload())
            return False
    with SessionLocal() as session:
        result = tickets.change_ticket_row(
            session=session,
            row_id=ticket_id,
            data=TicketUpdate(
                date=date,
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
        ui.notify(
            'Поле успешно изменено',
            type='positive',
        )
        if table:
            table.rows = [{**t.model_dump(), 'date': t.date.strftime('%d.%m.%Y')} for t in data]
            table.update()
        return True
    else:
        ui.notify(
            'Поле не найдено',
            type='negative',
        )
        return False


@required_role(UserRole.ADMIN)
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
        ui.notify(
            'Поле успешно удалено',
            type='positive',
        )
        if table:
            table.rows = [t.model_dump() for t in data]
            table.update()
    else:
        ui.notify(
            'Поле не найдено',
            type='negative',
        )
    return result


def get_all_users_data() -> list[UserOut]:
    with SessionLocal() as session:
        data = users.get_all_users(
            session=session,
        )
    return data


@required_role(UserRole.ADMIN)
def save_edited_users_data(
        user: dict,
        table: ui.table | None = None,
) -> bool:
    user_id = int(user['id'])
    with SessionLocal() as session:
        result = users.change_user(
            session=session,
            row_id=user_id,
            data=UserUpdate(
                username=user['username'],
                role=user['role'],
            )
        )
        if table and result:
            data = users.get_all_users(session=session)
    if result:
        ui.notify(
            'Пользователь успешно изменен',
            type='positive',
        )
        if table:
            table.rows = [t.model_dump() for t in data]
            table.update()
        return True
    else:
        ui.notify(
            'Пользователь не найден',
            type='negative',
        )
        return False


@required_role(UserRole.ADMIN)
def delete_on_users(instance_id: int, table: ui.table | None = None) -> bool:
    with SessionLocal() as session:
        result = users.delete_user(
            session=session,
            instance_id=instance_id,
        )
        if table and result:
            data = users.get_all_users(session=session)
    if result:
        ui.notify(
            'Пользователь успешно удален',
            type='positive',
        )
        if table:
            table.rows = [t.model_dump() for t in data]
            table.update()
    else:
        ui.notify(
            'Пользователь не найден',
            type='negative',
        )
    return result
