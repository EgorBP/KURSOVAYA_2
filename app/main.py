from nicegui import ui
from pages import data, login, menu, popular_data


@ui.page('/')
def main_page():
    ui.navigate.to('/login')


ui.run(port=8082, dark=True, show=False, reload=False, storage_secret='1')
