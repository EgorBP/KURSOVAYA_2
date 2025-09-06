from datetime import date
from app.crud.crud import *
from app.database import SessionLocal
from app.schemas import TicketCreate
from app.models import Tickets


with SessionLocal() as session:
    result1 = get_rows(session)
    data = TicketCreate(
        data=date.today(),
        theatre_name='ааааа',
        performance_name='МегаПон^3',
        tickets_count=10,
    )
    # result2 = add_row(session, data)
    # result3 = delete_row(session, 9)
    result11 = get_rows(session)
    # result4 = get_rows(session, filters={Tickets.performance_name:'МегаПон^3'})
    result4 = get_rows(session, sorting=((Tickets.theatre_name, False), (Tickets.tickets_count, True)))
    print(result1)
    # print(result3)
    print(result11)
    print(result4)
