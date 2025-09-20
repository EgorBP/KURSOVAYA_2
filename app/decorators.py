from nicegui import ui, app
import functools
from app.models import UserRole
from app.utils import check_login_type


def required_role(status: UserRole | None = None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if check_login_type(status):
                return func(*args, **kwargs)
            else:
                ui.navigate.to('/login')
                return None
        return wrapper
    return decorator
