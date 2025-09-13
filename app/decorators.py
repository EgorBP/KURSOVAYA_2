from nicegui import ui, app
import functools
from app.models import UserRole


def required_status(status: UserRole):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            storage = app.storage.user
            if storage.get('authenticated') and storage.get('user_type') == status.value:
                return func(*args, **kwargs)
            else:
                ui.navigate.to('/login')
                return None
        return wrapper
    return decorator
