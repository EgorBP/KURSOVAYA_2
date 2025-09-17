from nicegui import ui
from app.styles import MAIN_COLOR, MAIN_COLOR_GRADIENT, QUASAR_PURPLE
from app import ui_elements
from app.services.login import login


@ui.page('/login', title='Войти')
def admin_menu():
    ui_elements.top_panel('Вход в систему', 65)
    ui_elements.disable_scroll()

    with ui.column().style('width: 100%; height: 95vh; justify-content: center; align-items: center; overflow-y: hidden; transform: translateY(7vh);'):
        with ui.row().style(
                f'border: 4px solid {MAIN_COLOR}; padding: 2rem; border-radius: 1rem;'
        ).classes('items-center').style(''):
            with ui.column().style():
                username = ui.input('Логин').props(f'color={QUASAR_PURPLE}').style('width: 20rem; height: 3.5rem; font-size: 1.2rem')
                password = ui.input('Пароль', password=True).props(f'color={QUASAR_PURPLE}').style('width: 20rem; height: 3.5rem; font-size: 1.2rem')

        with ui.row():
            ui.button(
                'Войти',
                on_click=lambda: login(username=username.value, password=password.value),
            ).style(f'width: 20rem; height: 3.5rem; font-size: 1.2rem; background: {MAIN_COLOR_GRADIENT} !important;')
