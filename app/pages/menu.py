from nicegui import ui
from app.styles import MAIN_COLOR_GRADIENT, MAIN_COLOR
from app import ui_elements
from app.decorators import required_status
from app.models import UserRole


@ui.page('/admin', title='Меню администратора')
@required_status(UserRole.ADMIN)
def admin_menu():
    ui_elements.top_panel('Панель администратора', 83)

    with ui.column().style('align-items: center; width: 100%; justify-content: center; height: 95vh'):
        with ui.row().style(
            'font-size: 15rem; '
            'width: 60%; '
            'justify-content: center; '
            'display: flex; '
            'align-items: stretch; '
            'flex-direction: row;'
            'margin-top: 19vh;'
        ):
            ui.button(
                text='Просмотреть всех пользователей',
                on_click=lambda: ui.navigate.to('/data/users')
            ).props('rounded').style(f'font-size: 1.5rem; background: {MAIN_COLOR_GRADIENT} !important; flex: 1')
            ui.button(
                text='Добавить пользователя',
                on_click=lambda: ui.navigate.to('/add/user')
            ).props('rounded').style(f'font-size: 1.5rem; background: {MAIN_COLOR_GRADIENT} !important; flex: 1')
        with ui.row().style(
                'font-size: 15rem; '
                'width: 70%; '
                'justify-content: center; '
                'display: flex; '
                'align-items: stretch; '
                'flex-direction: row;'
                'margin-top: 2.5rem;'
        ):
            ui.button(
                text='Найти',
                on_click=lambda: ui.navigate.to('/search')
            ).props('rounded').style(f'font-size: 1.5rem; background: {MAIN_COLOR_GRADIENT} !important; flex: 1')
            ui.button(
                text='Просмотреть все данные',
                on_click=lambda: ui.navigate.to('/data/tickets')
            ).props('rounded').style(f'font-size: 1.5rem; background: {MAIN_COLOR_GRADIENT} !important; flex: 1')
            ui.button(
                text='Добавить',
                on_click=lambda: ui.navigate.to('/add/tickets')
            ).props('rounded').style(f'font-size: 1.5rem; background: {MAIN_COLOR_GRADIENT} !important; flex: 1')
        with ui.row().style(
                'font-size: 15rem; '
                'width: 60%; '
                'justify-content: center; '
                'display: flex; '
                'align-items: stretch; '
                'flex-direction: row;'
                'margin-top: 2.5rem;'
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
@required_status()
def user_menu():
    ui_elements.top_panel('Панель пользователя', 83)

    with ui.column().style('align-items: center; width: 100%; justify-content: center; height: 95vh'):
        with ui.row().style(
            'font-size: 15rem; '
            'width: 60%; '
            'justify-content: center; '
            'display: flex; '
            'align-items: stretch; '
            'flex-direction: row;'
            'margin-top: 19vh;'
        ):
            ui.button(
                text='Найти',
                on_click=lambda: ui.navigate.to('/search')
            ).props('rounded').style(f'font-size: 1.5rem; background: {MAIN_COLOR_GRADIENT} !important; flex: 1')
            ui.button(
                text='Просмотреть все данные',
                on_click=lambda: ui.navigate.to('/data/tickets')
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
