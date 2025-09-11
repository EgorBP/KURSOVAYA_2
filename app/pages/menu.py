from nicegui import ui


@ui.page('/admin')
def admin_menu():
    with ui.column().style('align-items: center; width: 100%;'):
        with ui.column().style('position: relative; width: 100%; align-items: center;'):
            ui.label('Панель админа').style('font-size: 9rem; text-align: center;')
            ui.button(icon='person', on_click=lambda: ui.navigate.to('/login')).props('rounded').style('position: absolute; top: 0; right: 0;')
        with ui.row().style('font-size: 15rem'):
            ui.button(text='sosatb', on_click=lambda: ui.notify('sosi'), color='orange').props('rounded').style('font-size: 1.5rem')


@ui.page('/user')
def user_menu():
    with ui.column().style('align-items: center; width: 100%;'):
        with ui.column().style('position: relative; width: 100%; align-items: center;'):
            ui.label('Панель админа').style('font-size: 9rem; text-align: center;')
            ui.button(icon='person', on_click=lambda: ui.navigate.to('/login')).props('rounded').style('position: absolute; top: 0; right: 0;')
        with ui.row().style('font-size: 15rem'):
            ui.button(text='sosatb', on_click=lambda: ui.notify('sosi'), color='orange').props('rounded').style('font-size: 1.5rem')
