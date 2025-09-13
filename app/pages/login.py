from nicegui import ui
from app.styles import MAIN_COLOR, MAIN_COLOR_GRADIENT
from app import ui_elements
from app.services.login import login


@ui.page('/login', title='Войти')
def admin_menu():
    ui_elements.top_panel()
    ui_elements.disable_scroll()

    with ui.row().style('justify-content: center; width: 100%;'):
        ui.label('Вход в систему').style('font-size: 6rem; text-align: center; overflow-y: hidden;')

    with ui.column().style('width: 100%; height: 100vh; justify-content: center; align-items: center; overflow-y: hidden'):
        with ui.row().style(
                f'border: 4px solid {MAIN_COLOR}; padding: 2rem; border-radius: 1rem;'
        ).classes('items-center gap-10').style('margin-top: -20rem'):
            with ui.column():
                username = ui.input('username').style('width: 300px; height: 50px; font-size: 1.2rem')
                password = ui.input('password', password=True).style('width: 300px; height: 50px; font-size: 1.2rem')

        with ui.row():
            ui.button(
                'Войти',
                on_click=lambda: login(username=username.value, password=password.value),
            ).style(f'width: 300px; height: 50px; font-size: 1.2rem; background: {MAIN_COLOR_GRADIENT} !important;')