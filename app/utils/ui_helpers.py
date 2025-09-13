from nicegui import app
from app.models import UserRole


def check_login_type(type_: UserRole) -> bool:
    storage = app.storage.user
    if storage.get('authenticated') and storage.get('user_type') == type_.value:
        return True
    else:
        return False

