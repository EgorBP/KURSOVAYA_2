from app.crud.users import add_user
from app.database import SessionLocal
from app.schemas import UserCreate
from app.models import UserRole


with SessionLocal() as session:
    add_user(
        session=session,
        data=UserCreate(
            username="admin",
            password="admin",
            role=UserRole.ADMIN,
        ),
    )
