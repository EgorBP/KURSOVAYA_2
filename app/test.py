from datetime import date
from app.crud.tickets import *
from app.database import SessionLocal
from app.schemas import TicketCreate
from app.models import Tickets


with SessionLocal() as session:
    result1 = get_rows(session)
    data = TicketCreate(
        data=date.today(),
        theatre_name='ааааа',
        performance_name='МегаПон^4',
        tickets_count=50,
    )
    # result2 = add_row(session, data)
    # result3 = delete_row(session, 9)
    result11 = get_rows(session)
    # result4 = get_rows(session, filters={Tickets.performance_name:'МегаПон^3'})
    # result4 = get_rows(session, sorting=((Tickets.theatre_name, False), (Tickets.tickets_count, True)))
    # result4 = get_popular_performances(session)
    result4 = get_popular_theaters(session)
    print()
    # print(result3)
    print(result11)
    print(result4)
