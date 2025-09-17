import datetime
from nicegui import ui
from app.database import SessionLocal
from app.models import UserRole
from app.schemas import UserCreate, TicketCreate
from app.crud import tickets, users
from app.decorators import required_role


@required_role(UserRole.ADMIN)
def add_new_ticket(
        date: str,
        theatre_name: str,
        performance_name: str,
        tickets_count: str,
) -> bool:
    try:
        tickets_count = int(tickets_count)
    except ValueError:
        ui.notify('❌ Количеством билетов должно быть число ❌')
        return False

    try:
        date = datetime.datetime.fromisoformat(date)
    except ValueError:
        try:
            day, month, year = date.split('.')
            date = f'{year}-{month}-{day}'
            date = datetime.datetime.fromisoformat(date)
        except ValueError:
            ui.notify('❌ Не верный формат даты ❌')
            return False

    with SessionLocal() as session:
        result = tickets.add_ticket_row(
            session=session,
            data=TicketCreate(
                date=date,
                theatre_name=performance_name,
                performance_name=performance_name,
                tickets_count=tickets_count,
            ),
        )

    if result:
        ui.notify('✅ Данные успешно добавлены ✅')
    return True


@required_role(UserRole.ADMIN)
def add_new_user(
        username: str,
        password: str,
        role: str,
) -> bool:
    try:
        role = UserRole(role)
    except ValueError:
        ui.notify('❌ Не верная роль ❌')
        return False
    with SessionLocal() as session:
        result = users.add_user(
            session=session,
            data=UserCreate(
                username=username,
                password=password,
                role=role,
            ),
        )

    if result:
        ui.notify('✅ Данные успешно добавлены ✅')
    return True
