from pydantic import BaseModel
from datetime import date


class TicketCreate(BaseModel):
    data: date
    theatre_name: str
    performance_name: str
    tickets_count: int

class TicketUpdate(TicketCreate):
    pass

class TicketOut(TicketCreate):
    id: int

    model_config = {
        "from_attributes": True
    }


class BasePopularDataOut(BaseModel):
    all_tickets_count: int

    model_config = {
        "from_attributes": True
    }

class PopularPerformanceOut(BasePopularDataOut):
    performance_name: str

class PopularTheatreOut(BasePopularDataOut):
    theatre_name: str


class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserCreate):
    id: int

class UserOut(UserBase):
    id: int

    model_config = {
        "from_attributes": True
    }
