from nicegui import ui
from app.styles import MAIN_COLOR_GRADIENT
from app import ui_elements


@ui.page('/admin', title='Меню администратора')
def admin_menu():
    ui_elements.top_panel()
    with ui.column().style('align-items: center; width: 100%;'):
        with ui.column().style('position: relative; width: 100%; align-items: center;'):
            ui.label('Панель админа').style('font-size: 9rem; text-align: center;')
        with ui.row().style('font-size: 15rem'):
            ui.button(
                text='sosatb',
                on_click=lambda: ui.notify('sosi')
            ).props('rounded').style(f'font-size: 1.5rem; background: {MAIN_COLOR_GRADIENT} !important;')


@ui.page('/user', title='Меню пользователя')
def user_menu():
    ui_elements.top_panel()
    with ui.column().style('align-items: center; width: 100%;'):
        with ui.column().style('position: relative; width: 100%; align-items: center;'):
            ui.label('Панель юзера').style('font-size: 9rem; text-align: center;')
        with ui.row().style('font-size: 15rem'):
            ui.button(
                text='sosatb',
                on_click=lambda: ui.notify('sosi')
            ).props('rounded').style(f'font-size: 1.5rem; background: {MAIN_COLOR_GRADIENT} !important;')
