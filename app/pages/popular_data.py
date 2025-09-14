from nicegui import ui
from app.styles import MAIN_COLOR
from app import ui_elements
from app.decorators import required_status
from app.crud import tickets
from app.database import SessionLocal


@ui.page('/popular_theaters', title='Популярные театры')
@required_status()
def data():
    ui_elements.top_panel('Популярные театры', 70)
    ui_elements.disable_scroll()

    with SessionLocal() as session:
        data = tickets.get_popular_theaters(session)

    with ui.column().style('align-items: center; width: 100%;'):
        with ui.row().style(
            f"""
            width: 30%;
            height: 100vh;
            align-items: center;
            justify-content: center;
            display: flex;
            flex-direction: row;
            transform: translateY(-40vh);
            """
        ):
            ui.table(
                columns=[
                    {"name": "theatre_name", "label": "Театр", 'field': 'theatre_name', 'align': 'center'},
                    {"name": "all_tickets_count", "label": "Всего билетов", 'field': 'all_tickets_count', 'align': 'center'},
                ],
                rows=[t.model_dump() for t in data],
                pagination=5,
            ).classes('my-table').style(
                f"""
                flex: 1;
                border: 0.15rem solid {MAIN_COLOR};
                border-radius: 1rem;
                padding: 1rem;
                box-shadow: none;
                """
            )
            ui.add_css("""
            /* заголовки таблицы */
            .my-table thead th {
                font-size: 1.4rem !important;
            }

            /* ячейки тела таблицы */
            .my-table tbody td {
                font-size: 1rem !important;
            }

            /* если нужно - шаги пагинации/футер */
            .my-table .q-table__bottom {
                font-size: 0.8rem !important;
            }
            """)


@ui.page('/popular_performances', title='Популярные спектакли')
@required_status()
def data():
    ui_elements.top_panel('Популярные спектакли', 80)
    ui_elements.disable_scroll()

    with SessionLocal() as session:
        data = tickets.get_popular_performances(session)

    with ui.column().style('align-items: center; width: 100%;'):
        with ui.row().style(
            f"""
            width: 30%;
            height: 100vh;
            align-items: center;
            justify-content: center;
            display: flex;
            flex-direction: row;
            transform: translateY(-40vh);
            """
        ):
            ui.table(
                columns=[
                    {"name": "performance_name", "label": "Спектакль", 'field': 'performance_name', 'align': 'center'},
                    {"name": "all_tickets_count", "label": "Всего билетов", 'field': 'all_tickets_count', 'align': 'center'},
                ],
                rows=[t.model_dump() for t in data],
                pagination=5,
            ).classes('my-table').style(
                f"""
                flex: 1;
                border: 0.15rem solid {MAIN_COLOR};
                border-radius: 1rem;
                padding: 1rem;
                box-shadow: none;
                """
            )
            ui.add_css("""
            /* заголовки таблицы */
            .my-table thead th {
                font-size: 1.4rem !important;
            }

            /* ячейки тела таблицы */
            .my-table tbody td {
                font-size: 1rem !important;
            }

            /* если нужно - шаги пагинации/футер */
            .my-table .q-table__bottom {
                font-size: 0.8rem !important;
            }
            """)
