from nicegui import ui, app
from app.pages import data, login, menu, popular_data, search, add


@ui.page('/')
def main_page():
    if app.storage.user.get("authenticated"):
        ui.navigate.to(f'/{app.storage.user.get("user_type")}')
    else:
        ui.navigate.to('/login')


if __name__ == '__main__':
    ui.run(
        port=8082,
        dark=True,
        show=False,
        reload=False,
        storage_secret='1',
        language='ru',
    )
