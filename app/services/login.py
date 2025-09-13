from app.crud.users import validate_user_password
from app.database import SessionLocal
from app.schemas import UserLogin
from nicegui import ui, app
from app.models import UserRole


def login(username: str, password: str) -> UserRole | None:
    """
    Выполняет проверку логина пользователя.

    Args:
        username (str): Имя пользователя.
        password (str): Пароль пользователя.

    Returns:
        UserRole | None:
            - экземпляр `UserRole` (например, `UserRole.USER` или `UserRole.ADMIN`),
              если проверка успешна;
            - None, если имя пользователя или пароль неверные.
    """
    data = UserLogin(username=username, password=password)

    with SessionLocal() as session:
        user_type = validate_user_password(session, data)

    if not user_type:
        ui.notify('❌ Неверные данные для входа ❌')
        return None
    else:
        app.storage.user.update({'username': username, 'authenticated': True, 'user_type': user_type.value})
        ui.navigate.to(f'/{user_type.value}')
        # ui.notify(f'✅ Вы вошли как {user_type.value} ✅')
        return user_type
