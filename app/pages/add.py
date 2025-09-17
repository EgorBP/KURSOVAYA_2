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
            ui.notify('❌ Вы не добавили дату ❌')
            return
        if not theatre:
            ui.notify('❌ Вы не добавили название театра ❌')
            return
        if not performance:
            ui.notify('❌ Вы не добавили название выступления ❌')
            return
        if not tickets:
            ui.notify('❌ Вы не добавили количество билетов ❌')
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
            theatre = ui.input('Название театра').props(f'color={QUASAR_PURPLE}').style(input_style)
            ui_elements.clear_button_to_input(theatre)
            performance = ui.input('Название выступления').props(f'color={QUASAR_PURPLE}').style(input_style)
            ui_elements.clear_button_to_input(performance)
            tickets = ui.input('Количество билетов').props(f'color={QUASAR_PURPLE}').style(input_style)
            ui_elements.clear_button_to_input(tickets)


            ui_elements.calendar_to_input(date)
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
            """
        )


@ui.page('/add/user', title='Добавление пользователя')
def add_user():
    pass
