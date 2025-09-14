from nicegui import ui
from app.models import UserRole, Users, Tickets
from app.styles import MAIN_COLOR, MAIN_COLOR_GRADIENT
from app import ui_elements


@ui.page('/search', title='Поиск данные')
def admin_menu():
    ui_elements.top_panel('Поиск данных', label_width=65)
    ui_elements.disable_scroll()

    btn_style = f'height: 4.5rem; font-size: 1.2rem; background: {MAIN_COLOR_GRADIENT} !important; flex: 1'

    def go_to_search(column, value, road='tickets'):
        if not value:
            ui.navigate.to(f'/data/{road}')
        ui.navigate.to(f'/data/{road}/{column}/{value}')

    with ui.column().style('width: 100%; height: 100vh; justify-content: center; align-items: center; transform: translateY(-30vh);'):
        with ui.row().style(
                f'border: 4px solid {MAIN_COLOR}; padding: 2rem; border-radius: 1rem;'
        ).classes('items-center').style(''):
            with ui.column().style():
                value = ui.input('Запрос').style('width: 30rem; height: 4rem; font-size: 1.2rem;').classes('centered-input')
                ui.add_css("""
                .centered-input .q-field__native {
                    text-align: center;
                }
                """)

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


