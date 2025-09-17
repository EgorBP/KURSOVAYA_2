from nicegui import ui
from app.models import UserRole
from app.styles import MAIN_COLOR, MAIN_COLOR_GRADIENT
from app import ui_elements
from app.decorators import required_status


@ui.page('/add/ticket', title='Добавление данных')
@required_status(UserRole.ADMIN)
def add_ticket():
    input_style = f'flex: 1; font-size: 1.15rem;'

    ui_elements.top_panel('Добавление данных', 70)

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
            """
        ):
            date = ui.input('Дата').style(input_style)
            theatre = ui.input('Название театра').style(input_style)
            performance = ui.input('Название выступления').style(input_style)
            tickest = ui.input('Количество билетов').style(input_style)

            ui_elements.calendar_to_input(date)
        ui.button('Добавить').style(
            f"""
            width: 37%; 
            font-size: 1.15rem; 
            background: {MAIN_COLOR_GRADIENT} !important;
            """
        )


@ui.page('/add/user', title='Добавление пользователя')
def add_user():
    pass
