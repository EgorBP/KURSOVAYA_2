from nicegui import ui, app
from app.styles import MAIN_COLOR_GRADIENT, MAIN_COLOR


def top_panel(label_name: str, label_width: int = 70, font_size: int = 6):
        ui.button(
            icon='home',
            on_click=lambda: ui.navigate.to(f'/{app.storage.user.get("user_type")}') if app.storage.user.get(
                "authenticated") else ui.navigate.to(f'/login')
        ).props('rounded').style(
            f'position: absolute; top: 3vh; left: 3vh; background: {MAIN_COLOR_GRADIENT} !important;'
        )

        ui.button(
            icon='person',
            on_click=lambda: ui.navigate.to('/login')
        ).props('rounded').style(
            f'position: absolute; top: 3vh; right: 3vh; background: {MAIN_COLOR_GRADIENT} !important;'
        )

        ui.label(label_name).style(f"""
            position: absolute;  
            top: -4vh;          
            left: 50%;
            transform: translateX(-50%); 
            font-size: {font_size}rem;
            text-align: center;
            border: 4px solid {MAIN_COLOR};
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
