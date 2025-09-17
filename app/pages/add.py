from nicegui import ui
from app.models import UserRole
from app.styles import MAIN_COLOR, MAIN_COLOR_GRADIENT, QUASAR_PURPLE
from app import ui_elements
from app.decorators import required_role
from app.services.add import add_new_ticket, add_new_user


@ui.page('/add/ticket', title='Добавление данных')
@required_role(UserRole.ADMIN)
def add_ticket():
    input_style = f'flex: 1; font-size: 1.15rem;'

    ui_elements.top_panel('Добавление данных', 70)

    def handle_add_ticket(date: str, theatre: str, performance: str, tickets: str):
        if not date:
            ui.notify(
                'Вы не добавили дату',
                type = 'warning',
            )
            return
        if not theatre:
            ui.notify(
                'Вы не добавили название театра',
                type = 'warning',
            )
            return
        if not performance:
            ui.notify(
                'Вы не добавили название выступления',
                type = 'warning',
            )
            return
        if not tickets:
            ui.notify(
                'Вы не добавили количество билетов',
                type = 'warning',
            )
            return

        add_new_ticket(
            date,
            theatre,
            performance,
            tickets,
        ),

    with ui.column().style(
            """
            width: 100%;
            height: 95vh;
            min-height: 30vh;
            align-items: center;
            justify-content: center;
            """
    ):
        with ui.row().style(
            f"""
            width: 40%;
            border: 0.2rem solid {MAIN_COLOR};
            padding: 1.5rem;
            border-radius: 1rem;
            display: flex;
            align-items: stretch;
            flex-direction: column;
            margin-top: 15vh;
            """
        ):
            date = ui.input('Дата').props(f'color={QUASAR_PURPLE}').style(input_style)
            ui_elements.calendar_to_input(date, set_data=True)
            theatre = ui.input('Название театра').props(f'color={QUASAR_PURPLE}').style(input_style)
            ui_elements.clear_button_to_input(theatre)
            performance = ui.input('Название выступления').props(f'color={QUASAR_PURPLE}').style(input_style)
            ui_elements.clear_button_to_input(performance)
            tickets = ui.input('Количество билетов').props(f'color={QUASAR_PURPLE}').style(input_style)
            ui_elements.clear_button_to_input(tickets)

        ui.button(
            text='Добавить',
            on_click=lambda: handle_add_ticket(
                date.value,
                theatre.value,
                performance.value,
                tickets.value
            ),
        ).style(
            f"""
            width: 37%; 
            height: 3.5rem;
            font-size: 1.3rem; 
            background: {MAIN_COLOR_GRADIENT} !important;
            border-radius: 0.3rem;
            """
        )


@ui.page('/add/user', title='Добавление пользователей')
@required_role(UserRole.ADMIN)
def add_user():
    input_style = f'flex: 1; font-size: 1.15rem;'

    ui_elements.top_panel('Добавить пользователя', 80)

    def handle_add_user(username: str, password: str, password_confirm: str, role: str):
        if not username:
            ui.notify(
                'Вы не ввели роль',
                type = 'warning',
            )
            return
        if not password:
            ui.notify(
                'Вы не ввели пароль',
                type = 'warning',
            )
            return
        if not role:
            ui.notify(
                'Вы не выбрали роль',
                type = 'warning',
            )
            return
        if password != password_confirm:
            ui.notify(
                'Пароли не совпадают',
                type = 'warning',
            )
            return

        add_new_user(
            username,
            password,
            role
        ),

    with ui.column().style(
            """
            width: 100%;
            height: 95vh;
            min-height: 30vh;
            align-items: center;
            justify-content: center;
            """
    ):
        with ui.row().style(
            f"""
            width: 30%;
            border: 0.2rem solid {MAIN_COLOR};
            padding: 1.5rem;
            border-radius: 1rem;
            display: flex;
            align-items: stretch;
            flex-direction: column;
            margin-top: 15vh;
            """
        ):
            username = ui.input('Имя нового пользователя').props(f'color={QUASAR_PURPLE}').style(input_style)
            ui_elements.clear_button_to_input(username)
            password = ui.input('Пароль', password=True).props(f'color={QUASAR_PURPLE}').style(input_style)
            ui_elements.clear_button_to_input(password)
            password_confirm = ui.input('Подтверждение пароля', password=True).props(f'color={QUASAR_PURPLE}').style(input_style)
            ui_elements.clear_button_to_input(password_confirm)
            role = ui.select(
                label='Выберите роль',
                options=list(UserRole._value2member_map_.keys())
            ).props(f'color={QUASAR_PURPLE}').style(input_style)
            ui_elements.clear_button_to_input(role)

        ui.button(
            text='Добавить',
            on_click=lambda: handle_add_user(
                username.value,
                password.value,
                password_confirm.value,
                role.value,
            ),
        ).style(
            f"""
            width: 27%; 
            height: 3.5rem;
            font-size: 1.3rem; 
            background: {MAIN_COLOR_GRADIENT} !important;
            border-radius: 0.3rem;
            """
        )