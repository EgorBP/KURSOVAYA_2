from datetime import datetime

from nicegui import ui, app
from app.styles import MAIN_COLOR_GRADIENT, MAIN_COLOR, QUASAR_PURPLE


def top_panel(label_name: str, label_width: int = 70, font_size: int = 6):
        ui.button(
            icon='home',
            on_click=lambda: ui.navigate.to(f'/{app.storage.user.get("user_type")}') if app.storage.user.get(
                "authenticated") else ui.navigate.to(f'/login')
        ).props('rounded').style(
            f'position: fixed; top: 3vh; left: 3vh; background: {MAIN_COLOR_GRADIENT} !important;'
        )

        ui.button(
            icon='person',
            on_click=lambda: ui.navigate.to('/login')
        ).props('rounded').style(
            f'position: fixed; top: 3vh; right: 3vh; background: {MAIN_COLOR_GRADIENT} !important;'
        )

        ui.label(label_name).style(f"""
            position: absolute;  
            top: -4vh;          
            left: 50%;
            transform: translateX(-50%); 
            font-size: {font_size}rem;
            text-align: center;
            border: 0.3rem solid {MAIN_COLOR};
            padding: 2rem;
            border-radius: 1rem;
            width: {label_width}%;
        """)

        # ui.switch(
        #     value=True if ui.dark_mode else False,
        #     on_change=lambda e: ui.dark_mode(True) if e.value else ui.dark_mode(False),
        # ).props(f'color=orange').style(
        #     f'position: fixed; bottom: 10px; right: 10px;')


def disable_scroll():
    ui.add_head_html('''
    <style>
    html, body {
        overflow: hidden;
    }
    </style>
    ''')


def calendar_to_input(input_element: ui.input):
    input_element.value = datetime.now().date().strftime('%d.%m.%Y')
    with input_element.add_slot('append'):
        with ui.menu().props('no-parent-event anchor="center right" self="center start"').style(
                f'transform: translateX(1rem)') as menu:
            with ui.date(
                mask='DD.MM.YYYY',
                on_change=lambda: menu.close()
            ).props(f'today-btn color="{QUASAR_PURPLE}"').bind_value(input_element):
                # with ui.row().classes('justify-end'):
                #     ui.button('Закрыть', on_click=menu.close).props(f'flat color={QUASAR_PURPLE}')
                pass
        ui.icon('edit_calendar', color=QUASAR_PURPLE).on('click', lambda: menu.open() if not menu.value else menu.close())
