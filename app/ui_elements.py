from nicegui import ui, app
from app.styles import MAIN_COLOR_GRADIENT, MAIN_COLOR


def top_panel(label_name: str, label_width: int = 70, font_size: int = 6):
    with ui.column().style('align-items: center; width: 100%; z-index: 1000;'):
        with ui.column().style('position: relative; width: 100%; align-items: center;'):
            ui.button(
                icon='home',
                on_click=lambda: ui.navigate.to(f'/{app.storage.user.get("user_type")}') if app.storage.user.get("authenticated") else ui.navigate.to(f'/login')
            ).props('rounded').style(
                f'position: absolute; top: 10px; left: 10px; background: {MAIN_COLOR_GRADIENT} !important;')
            ui.button(
                icon='person',
                on_click=lambda: ui.navigate.to('/login')
            ).props('rounded').style(
                f'position: absolute; top: 10px; right: 10px; background: {MAIN_COLOR_GRADIENT} !important;')

        with ui.row().style('justify-content: center; width: 100%;'):
            ui.label(label_name).style(
                f'font-size: {font_size}rem;'
                f'text-align: center;'
                f'border: 4px solid {MAIN_COLOR};'
                f'padding: 2rem;'
                f'border-radius: 1rem;'
                f'transform: translateY(-10vh);'  # смещаем вверх
                f'width: {label_width}%;'  # ширина
            )

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
