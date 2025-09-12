from nicegui import ui
from app.styles import MAIN_COLOR, MAIN_COLOR_GRADIENT


@ui.page('/login')
def admin_menu():
    with ui.column().classes('w-full h-screen items-center justify-center'):
        with ui.row().style(
                f'border: 4px solid {MAIN_COLOR}; padding: 2rem; border-radius: 1rem;'
        ).classes('items-center gap-10').style('margin-top: -10rem'):
            with ui.column():
                ui.input('username').style('width: 300px; height: 50px; font-size: 1.2rem')
                ui.input('password', password=True).style('width: 300px; height: 50px; font-size: 1.2rem')

        with ui.row():
            ui.button('Войти').style(f'width: 300px; height: 50px; font-size: 1.2rem; background: {MAIN_COLOR_GRADIENT} !important;')