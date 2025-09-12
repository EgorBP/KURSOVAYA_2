from nicegui import ui
from app.styles import MAIN_COLOR_GRADIENT


def top_panel():
    with ui.column().style('align-items: center; width: 100%;'):
        with ui.column().style('position: relative; width: 100%; align-items: center;'):
            ui.button(
                icon='home',
                on_click=lambda: ui.navigate.to('/')
            ).props('rounded').style(
                f'position: absolute; top: 10px; left: 10px; background: {MAIN_COLOR_GRADIENT} !important;')
            ui.button(
                icon='person',
                on_click=lambda: ui.navigate.to('/login')
            ).props('rounded').style(
                f'position: absolute; top: 10px; right: 10px; background: {MAIN_COLOR_GRADIENT} !important;')

        ui.switch(
            value=True if ui.dark_mode else False,
            on_change=lambda e: ui.dark_mode(True) if e.value else ui.dark_mode(False),
        ).props(f'color=orange').style(
            f'position: fixed; bottom: 10px; right: 10px;')
