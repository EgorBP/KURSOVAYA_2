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
