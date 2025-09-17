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
        ui.notify(
            'Количеством билетов должно быть число',
            type='negative',
        )
        return False

    try:
        date = datetime.datetime.fromisoformat(date)
    except ValueError:
        try:
            day, month, year = date.split('.')
            date = f'{year}-{month}-{day}'
            date = datetime.datetime.fromisoformat(date)
        except ValueError:
            ui.notify(
                'Не верный формат даты',
                type = 'negative',
            )
            return False

    with SessionLocal() as session:
        result = tickets.add_ticket_row(
            session=session,
            data=TicketCreate(
                date=date,
                theatre_name=theatre_name,
                performance_name=performance_name,
                tickets_count=tickets_count,
            ),
        )

    if result:
        ui.notification(
            'Данные успешно добавлены',
            type='positive',
            actions=[{
                "icon": 'storage',
                "color": "white",
                "onclick": 'emitEvent("go_tickets_data")'
            }]
        )
        ui.on('go_tickets_data', lambda: ui.navigate.to('/data/tickets'))
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
        ui.notify(
            'Данной роли не существует',
            type = 'negative',
        )
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
        ui.notification(
            'Пользователь успешно добавлен',
            type='positive',
            actions=[{
                "icon": 'storage',
                "color": "white",
                "onclick": 'emitEvent("go_users_data")'
            }]
        )
        ui.on('go_users_data', lambda: ui.navigate.to('/data/users'))
    else:
        ui.notification(
            'Пользователь с данным никнеймом уже существует',
            type='negative',
            actions=[{
                "icon": 'storage',
                "color": "white",
                "onclick": 'emitEvent("go_users_data")'
            }]
        )
        ui.on('go_users_data', lambda: ui.navigate.to('/data/users'))
    return True
