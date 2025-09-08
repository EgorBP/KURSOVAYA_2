from nicegui import ui
from app.schemas import TicketOut
import datetime

# допустим, у вас есть список объектов TicketOut
tickets = [
    TicketOut(data=datetime.date(2025, 9, 6), theatre_name='Большой Театр', performance_name='МегаПон^3', tickets_count=10, id=6),
    TicketOut(data=datetime.date(2025, 9, 6), theatre_name='Большой Театр', performance_name='МегаПон^3', tickets_count=15, id=7),
    TicketOut(data=datetime.date(2025, 9, 6), theatre_name='Большой Театр', performance_name='МегаПон^3', tickets_count=20, id=8),
    TicketOut(data=datetime.date(2025, 9, 6), theatre_name='ааааа', performance_name='МегаПон^3', tickets_count=10, id=1012),
    TicketOut(data=datetime.date(2025, 9, 7), theatre_name='ааааа', performance_name='МегаПон^4', tickets_count=50, id=11),
]
def render_button(row):
    return ui.button(f"Buy {row['tickets_count']}", on_click=lambda: print(f"Clicked {row['id']}"))
# создаём таблицу
table = ui.table(
    columns=[
        {"name": "id", "label": "ID", 'field': 'id', 'sortable': True, 'align': 'center'},
        {"name": "data", "label": "Дата", 'field': 'data', 'align': 'center'},
        {"name": "theatre_name", "label": "Театр", 'field': 'theatre_name', 'align': 'center'},
        {"name": "performance_name", "label": "Выступление", 'field': 'performance_name', 'align': 'center'},
        {"name": "tickets_count", "label": "Количество билетов", 'field': 'tickets_count', 'sortable': True, 'align': 'center'},

    ],
    rows = [t.model_dump() for t in tickets],  # список словарей
)
table.classes('text-center')  # применяет центрирование ко всем колонкам
ui.run(port=8081)
