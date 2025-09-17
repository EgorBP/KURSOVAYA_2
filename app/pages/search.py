from nicegui import ui
from app.decorators import required_status
from app.models import Tickets
from app.styles import MAIN_COLOR, MAIN_COLOR_GRADIENT, QUASAR_PURPLE
from app import ui_elements
from datetime import datetime


@ui.page('/search', title='Поиск данные')
@required_status()
def admin_menu():
    ui_elements.top_panel('Поиск данных', label_width=65)
    ui_elements.disable_scroll()

    btn_style = f'height: 4.5rem; font-size: 1.2rem; background: {MAIN_COLOR_GRADIENT} !important; flex: 1; border-radius: 0.5rem;'

    def go_to_search(column, value, road='tickets'):
        if column == Tickets.date.key:
            try:
                datetime.fromisoformat(value)
            except ValueError:
                try:
                    day, month, year = value.split('.')
                    value = f'{year}-{month}-{day}'
                    datetime.fromisoformat(value)
                except ValueError:
                    ui.notify('❌ Не верный формат даты ❌')
                    return
        if column == Tickets.tickets_count.key:
            try:
                int(value)
            except ValueError:
                ui.notify('❌ Количество билетов должно быть числом ❌')
                return
        if not value:
            ui.navigate.to(f'/data/{road}')
        ui.navigate.to(f'/data/{road}/{column}/{value}')

    with ui.column().style('width: 100%; height: 95vh; justify-content: center; align-items: center; transform: translateY(6vh);'):
        with ui.row().style(
                f'border: 4px solid {MAIN_COLOR}; padding: 2rem; border-radius: 1rem;'
        ).classes('items-center').style(''):
            with ui.column().style():
                value = ui.input().props(f'color={QUASAR_PURPLE} placeholder="Введите запрос"').style('width: 30rem; height: 4rem; font-size: 1.5rem;').classes('centered-input')
                ui.add_css("""
                .centered-input .q-field__native {
                    text-align: center;
                }
                """)
            # Выдвижная панель даты
            ui_elements.calendar_to_input(value)

        with ui.row().style(
                'width: 34rem; '
                'justify-content: center; '
                'display: flex; '
                'align-items: stretch; '
                'flex-direction: row;'
        ):
            ui.button(
                'Поиск по театрам',
                on_click=lambda: go_to_search(Tickets.theatre_name.key, value.value),
            ).style(btn_style)
            ui.button(
                'Поиск по выступлениям',
                on_click=lambda: go_to_search(Tickets.performance_name.key, value.value),
            ).style(btn_style)
        with ui.row().style(
                'width: 34rem; '
                'justify-content: center; '
                'display: flex; '
                'align-items: stretch; '
                'flex-direction: row;'
        ):
            ui.button(
                'Поиск по дате',
                on_click=lambda: go_to_search(Tickets.date.key, value.value),
            ).style(btn_style)
            ui.button(
                'Поиск по количеству билетов',
                on_click=lambda: go_to_search(Tickets.tickets_count.key, value.value),
            ).style(btn_style)
