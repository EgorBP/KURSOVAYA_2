from nicegui import ui
from app.styles import MAIN_COLOR


@ui.page('/login')
def admin_menu():
    with ui.column().classes('w-full h-screen items-center justify-center'):
        with ui.row().style(
                f'border: 3px solid {MAIN_COLOR}; padding: 2rem; border-radius: 1rem;'
        ).classes('items-center gap-10').style('margin-top: -10rem'):
            with ui.column():
                ui.input('username').style('width: 300px; height: 50px; font-size: 1.2rem')
                ui.input('password', password=True).style('width: 300px; height: 50px; font-size: 1.2rem')

        with ui.row():
            ui.button('Войти', color=MAIN_COLOR).style(f'width: 300px; height: 50px; font-size: 1.2rem')