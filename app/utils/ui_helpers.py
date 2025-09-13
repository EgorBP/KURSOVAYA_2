from nicegui import app
from app.models import UserRole


def check_login_type(type_: UserRole | None = None) -> bool:
    storage = app.storage.user
    if storage.get('authenticated'):
        if type_ and storage.get('user_type') == type_.value:
            return True
        elif type_ is None:
            return True
        else:
            return False
    else:
        return False

