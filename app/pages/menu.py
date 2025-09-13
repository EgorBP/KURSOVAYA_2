from nicegui import ui
from app.styles import MAIN_COLOR_GRADIENT, MAIN_COLOR
from app import ui_elements
from app.decorators import required_status
from app.models import UserRole


@ui.page('/admin', title='Меню администратора')
@required_status(UserRole.ADMIN)
def admin_menu():
    ui_elements.top_panel()

    with ui.column().style('align-items: center; width: 100%;'):
        with ui.column().style('position: relative; width: 100%; align-items: center;'):
            ui.label('Панель администратора').style(
                f'font-size: 6rem; '
                f'text-align: center; '
                f'border: 4px solid {MAIN_COLOR}; '
                f'padding: 2rem;'
                f'border-radius: 1rem;'
                f'transform: translateY(-10vh);'  # смещаем вверх на половину высоты экрана
                f'width: 83%;'  # чтобы боковые края не по центру полностью
            )
        with ui.row().style(
                'font-size: 15rem; '
                'width: 70%; '
                'justify-content: center; '
                'display: flex; '
                'align-items: stretch; '
                'flex-direction: row;'
                'margin-top: 2rem;'
        ):
            ui.button(
                text='Найти',
                on_click=lambda: ui.navigate.to('/find')
            ).props('rounded').style(f'font-size: 1.5rem; background: {MAIN_COLOR_GRADIENT} !important; flex: 1')
            ui.button(
                text='Просмотреть все данные',
                on_click=lambda: ui.navigate.to('/data')
            ).props('rounded').style(f'font-size: 1.5rem; background: {MAIN_COLOR_GRADIENT} !important; flex: 1')
            ui.button(
                text='Добавить',
                on_click=lambda: ui.navigate.to('/add')
            ).props('rounded').style(f'font-size: 1.5rem; background: {MAIN_COLOR_GRADIENT} !important; flex: 1')
        with ui.row().style(
                'font-size: 15rem; '
                'width: 60%; '
                'justify-content: center; '
                'display: flex; '
                'align-items: stretch; '
                'flex-direction: row;'
                'margin-top: 4rem;'
        ):
            ui.button(
                text='Узнать популярные театры',
                on_click=lambda: ui.navigate.to('/popular_theaters')
            ).props('rounded').style(f'font-size: 1.5rem; background: {MAIN_COLOR_GRADIENT} !important; flex: 1')
            ui.button(
                text='Узнать популярные спектакли',
                on_click=lambda: ui.navigate.to('/popular_performances')
            ).props('rounded').style(f'font-size: 1.5rem; background: {MAIN_COLOR_GRADIENT} !important; flex: 1')


@ui.page('/user', title='Меню пользователя')
@required_status(UserRole.USER)
def user_menu():
    ui_elements.top_panel()

    with ui.column().style(f'align-items: center; width: 100%;'):
        with ui.column().style(f'position: relative; width: 100%; align-items: center;'):
            ui.label('Панель пользователя').style(
                f'font-size: 6rem; '
                f'text-align: center; '
                f'border: 4px solid {MAIN_COLOR}; '
                f'padding: 2rem;'
                f'border-radius: 1rem;'
                f'transform: translateY(-10vh);'  # смещаем вверх на половину высоты экрана
                f'width: 83%;'  # чтобы боковые края не по центру полностью
            )
        with ui.row().style(
                'font-size: 15rem; '
                'width: 70%; '
                'justify-content: center; '
                'display: flex; '
                'align-items: stretch; '
                'flex-direction: row;'
                'margin-top: 2rem;'
        ):
            ui.button(
                text='Найти',
                on_click=lambda: ui.navigate.to('/find')
            ).props('rounded').style(f'font-size: 1.5rem; background: {MAIN_COLOR_GRADIENT} !important; flex: 1')
            ui.button(
                text='Просмотреть все данные',
                on_click=lambda: ui.navigate.to('/data')
            ).props('rounded').style(f'font-size: 1.5rem; background: {MAIN_COLOR_GRADIENT} !important; flex: 1')
        with ui.row().style(
                'font-size: 15rem; '
                'width: 60%; '
                'justify-content: center; '
                'display: flex; '
                'align-items: stretch; '
                'flex-direction: row; '
                'margin-top: 4rem;'
        ):
            ui.button(
                text='Узнать популярные театры',
                on_click=lambda: ui.navigate.to('/popular_theaters')
            ).props('rounded').style(f'font-size: 1.5rem; background: {MAIN_COLOR_GRADIENT} !important; flex: 1')
            ui.button(
                text='Узнать популярные спектакли',
                on_click=lambda: ui.navigate.to('/popular_performances')
            ).props('rounded').style(f'font-size: 1.5rem; background: {MAIN_COLOR_GRADIENT} !important; flex: 1')
