from nicegui import ui
from app.styles import MAIN_COLOR, MAIN_COLOR_GRADIENT
from app import ui_elements
from app.services.login import login


@ui.page('/search', title='Поиск данные')
def admin_menu():
    ui_elements.top_panel('Поиск данных', label_width=65)
    ui_elements.disable_scroll()


    with ui.column().style('width: 100%; height: 100vh; justify-content: center; align-items: center; overflow-y: hidden; transform: translateY(-35vh);'):
        with ui.row().style(
                f'border: 4px solid {MAIN_COLOR}; padding: 2rem; border-radius: 1rem;'
        ).classes('items-center').style(''):
            with ui.column().style():
                username = ui.input('Запрос').style('width: 30rem; height: 4rem; font-size: 1.2rem;').classes('centered-input')
                ui.add_css("""
                .centered-input .q-field__native {
                    text-align: center;
                }
                """)

        with ui.row():
            ui.button(
                'Войти',
                on_click=lambda: login(username=username.value, password=password.value),
            ).style(f'width: 30rem; height: 4rem; font-size: 1.2rem; background: {MAIN_COLOR_GRADIENT} !important;')
