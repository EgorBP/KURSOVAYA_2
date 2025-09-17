from nicegui import ui
from app.styles import MAIN_COLOR
from app import ui_elements
from app.decorators import required_status
# from app.services.popular_data import


@ui.page('/add/ticket', title='Добавление данных')
def add_ticket():
    ui_elements.top_panel('Добавление данных', 70)

    with ui.column().style('align-items: center; width: 100%;'):
        with ui.row().style(
            """
            width: 100%;
            height: 95vh;
            align-items: center;
            justify-content: center;
            """
        ):
            date = ui.input('Date')
            with ui.menu().props('no-parent-event').style('transform: translateX(0rem);') as menu:
                with ui.date(mask='DD.MM.YYYY').bind_value(date):
                    with ui.row().classes('justify-end'):
                        ui.button('Close', on_click=menu.close).props('flat')
            with date.add_slot('append'):
                ui.icon('edit_calendar').on('click', menu.open).classes('cursor-pointer')
            # with ui.column():
            ui.input()


@ui.page('/add/user', title='Добавление пользователя')
def add_user():
    pass
