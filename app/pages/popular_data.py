from nicegui import ui
from app.styles import MAIN_COLOR
from app import ui_elements
from app.decorators import required_status
from app.services.popular_data import (get_popular_theaters_data, get_popular_performances_data,
                                       refresh_table_popular_theaters, refresh_table_popular_performances)


@ui.page('/popular_theaters', title='Популярные театры')
@required_status()
def data_theaters():
    ui_elements.top_panel('Популярные театры', 70)
    ui_elements.disable_scroll()

    data = get_popular_theaters_data()

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
            table = ui.table(
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
        with ui.column().style(
            f"""
            position: absolute;
            right: calc((100% - 70%) / 2);
            """
        ):
            months = ui.select(
                label='Выберите месяц',
                options=[
                    'Январь', 'Февраль', 'Март', 'Апрель',
                    'Май', 'Июнь', 'Июль', 'Август',
                    'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'
                ],
                value='Январь',
                on_change=lambda: refresh_table_popular_theaters(
                    month=months.options.index(months.value) + 1,
                    table=table,
                )
            ).style(f"""
                border: 0.15rem solid {MAIN_COLOR};
                border-radius: 1rem;
                padding: 1rem;
                font-size: 1.5rem;
                width: 15rem;
                transform: translateX(-0.6rem);
            """)


@ui.page('/popular_performances', title='Популярные спектакли')
@required_status()
def data_performances():
    ui_elements.top_panel('Популярные спектакли', 80)
    ui_elements.disable_scroll()

    data = get_popular_performances_data()

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
            table = ui.table(
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
        with ui.column().style(
            f"""
            position: absolute;
            right: calc((100% - 70%) / 2);
            """
        ):
            months = ui.select(
                label='Выберите месяц',
                options=[
                    'Январь', 'Февраль', 'Март', 'Апрель',
                    'Май', 'Июнь', 'Июль', 'Август',
                    'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'
                ],
                value='Январь',
                on_change=lambda: refresh_table_popular_performances(
                    month=months.options.index(months.value) + 1,
                    table=table,
                )
            ).style(f"""
                border: 0.15rem solid {MAIN_COLOR};
                border-radius: 1rem;
                padding: 1rem;
                font-size: 1.5rem;
                width: 15rem;
                transform: translateX(-0.6rem);
            """)