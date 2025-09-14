from nicegui import ui
from app.styles import MAIN_COLOR
from app import ui_elements
from app.decorators import required_status
from app.services.data import get_all_tickets_data, delete_on_tickets, get_all_users_data, delete_on_users
from app.utils import check_login_type
from app.models import UserRole


@ui.page('/data/tickets', title='Данные театров')
@required_status()
def data_tickets():
    ui_elements.top_panel('Получение данных', 70)
    ui_elements.disable_scroll()

    data = get_all_tickets_data()
    is_admin = check_login_type(UserRole.ADMIN)

    with ui.column().style('align-items: center; width: 100%;'):
        with ui.row().style(
            f"""
            width: 70%;
            height: 100vh;
            align-items: center;
            justify-content: center;
            display: flex;
            flex-direction: row;
            transform: translateY(-35vh);
            """
        ):
            table = ui.table(
                columns=[
                    {"name": "id", "label": "ID", 'field': 'id', 'sortable': True, 'align': 'center'},
                    {"name": "data", "label": "Дата", 'field': 'data', 'sortable': True, 'align': 'center'},
                    {"name": "theatre_name", "label": "Театр", 'field': 'theatre_name', 'sortable': True, 'align': 'center'},
                    {"name": "performance_name", "label": "Выступление", 'field': 'performance_name', 'sortable': True, 'align': 'center'},
                    {"name": "tickets_count", "label": "Количество билетов", 'field': 'tickets_count', 'sortable': True, 'align': 'center'},
                ],
                rows=[t.model_dump() for t in data],
                pagination=5,
            ).style(
                f"""
                flex: 1;
                border: 0.15rem solid {MAIN_COLOR};
                border-radius: 1rem;
                padding: 1rem;
                box-shadow: none;
                """
            )

            if is_admin:
                table.columns.append({"name": "actions", "label": "Действия", "field": "actions", "align": "center"})
                table.add_slot(f'body-cell-actions', """
                    <q-td :props="props">
                        <q-btn @click="$parent.$emit('edit', props)" icon="edit" flat dense color='blue'/>
                        <q-btn @click="$parent.$emit('del', props)" icon="delete" flat dense color='red'/>
                    </q-td>
                """)

                table.on('edit', lambda msg: ui.navigate.to(f'/change/tickets/{msg.args['row']['id']}'))
                table.on('del', lambda msg: delete_on_tickets(msg.args['row']['id'], table))


@ui.page('/data/users', title='Данные пользователей')
@required_status(UserRole.ADMIN)
def data_users():
    ui_elements.top_panel('Пользователи', 65)
    ui_elements.disable_scroll()

    data = get_all_users_data()
    is_admin = check_login_type(UserRole.ADMIN)

    with ui.column().style('align-items: center; width: 100%;'):
        with ui.row().style(
            f"""
            width: 65%;
            height: 100vh;
            align-items: center;
            justify-content: center;
            display: flex;
            flex-direction: row;
            transform: translateY(-35vh);
            """
        ):
            table = ui.table(
                columns=[
                    {"name": "id", "label": "ID", 'field': 'id', 'sortable': True, 'align': 'center'},
                    {"name": "username", "label": "Логин", 'field': 'username', 'sortable': True, 'align': 'center'},
                    {"name": "role", "label": "Роль", 'field': 'role', 'sortable': True, 'align': 'center'},
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
                font-size: 1.2rem !important;
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


            if is_admin:
                table.columns.append({"name": "actions", "label": "Действия", "field": "actions", "align": "center"})
                table.add_slot(f'body-cell-actions', """
                    <q-td :props="props">
                        <q-btn @click="$parent.$emit('edit', props)" icon="edit" flat dense color='blue'/>
                        <q-btn @click="$parent.$emit('del', props)" icon="delete" flat dense color='red'/>
                    </q-td>
                """)

                table.on('edit', lambda msg: ui.navigate.to(f'/change/users/{msg.args['row']['id']}'))
                table.on('del', lambda msg: delete_on_users(msg.args['row']['id'], table))