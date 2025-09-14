import datetime
from nicegui import ui
from app.styles import MAIN_COLOR, MAIN_COLOR_GRADIENT
from app import ui_elements
from app.decorators import required_status
from app.services.data import get_all_tickets_data, delete_on_tickets, get_all_users_data, delete_on_users
from app.utils import check_login_type
from app.models import UserRole, Tickets


@ui.page('/data/tickets', title='Данные театров')
@ui.page('/data/tickets/{column}/{value}', title='Данные театров')
@required_status()
def data_tickets(column: str | None = None, value: str | None = None):
    ui_elements.top_panel('Получение данных', 70)
    ui_elements.disable_scroll()

    if column:
        column = getattr(Tickets, column)
        if column.type.python_type is int:
            value = int(value)
        elif column.type.python_type is datetime.date:
            day, month, year = map(int, value.split('.'))
            value = datetime.datetime(year, month, day)
        data = get_all_tickets_data({column: value})
    else:
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
            columns = [
                {"name": "id", "label": "ID", 'field': 'id', 'sortable': True, 'align': 'center', 'style': f'width: 10%;'},
                {"name": "date", "label": "Дата", 'field': 'date', 'sortable': True, 'align': 'center', 'style': f'width: 20%;'},
                {"name": "theatre_name", "label": "Театр", 'field': 'theatre_name', 'sortable': True,
                 'align': 'center', 'style': f'width: 25%;'},
                {"name": "performance_name", "label": "Выступление", 'field': 'performance_name', 'sortable': True,
                 'align': 'center', 'style': f'width: 15%;'},
                {"name": "tickets_count", "label": "Билеты", 'field': 'tickets_count', 'sortable': True,
                 'align': 'center', 'style': f'width: 10%;'},
            ]
            table = ui.table(
                columns=columns,
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
                font-size: 1rem !important;
            }

            /* ячейки тела таблицы */
            .my-table tbody td {
                font-size: 0.8rem !important;
            }

            /* если нужно - шаги пагинации/футер */
            .my-table .q-table__bottom {
                font-size: 0.8rem !important;
            }
            """)

            if is_admin:
                table.columns.append({"name": "actions", "label": "Действия", "field": "actions", "align": "center"})
                # table.add_slot(f'body-cell-actions', """
                #     <q-td :props="props">
                #         <q-btn @click="$parent.$emit('toggle_edit', props)" icon="edit" flat dense color='blue'/>
                #         <q-btn @click="$parent.$emit('del', props)" icon="delete" flat dense color='red'/>
                #     </q-td>
                # """)
                table.add_slot("body", fr"""
                <q-tr :props="props">
                    <q-td class="text-center" style="width:10%;">{{{{ props.row.id }}}}</q-td>
                    <q-td class="text-center" style="width:20%;">{{{{ props.row.date }}}}</q-td>
                    <q-td class="text-center" style="width:20%;">{{{{ props.row.theatre_name }}}}</q-td>
                    <q-td class="text-center" style="width:25%;">{{{{ props.row.performance_name }}}}</q-td>
                    <q-td class="text-center" style="width:15%;">{{{{ props.row.tickets_count }}}}</q-td>
                    <q-td class="text-center" style="width:10%;">
                        <q-btn color="yellow" flat dense 
                            @click="props.expand = !props.expand"
                            :icon="props.expand ? 'remove' : 'edit'" />
                        <q-btn icon="delete" flat dense color='red' @click="$parent.$emit('del', props)" />
                    </q-td>
                </q-tr>

                <q-tr v-show="props.expand" :props="props">
                    <q-td colspan="100%" style="padding:0.25rem;">
                        <div style="display:flex; gap:0.5rem; width:100%;">
                            <q-input v-model="props.row.id" dense style="flex:0.10;" readonly input-class="text-center" />
                            <q-input v-model="props.row.date" dense style="flex:0.20;" input-class="text-center" />
                            <q-input v-model="props.row.theatre_name" dense style="flex:0.20;" input-class="text-center" />
                            <q-input v-model="props.row.performance_name" dense style="flex:0.26;" input-class="text-center" />
                            <q-input v-model="props.row.tickets_count" dense style="flex:0.15;" input-class="text-center" />
                            <q-btn icon="save" dense style="flex:0.09;" 
                                style="background: {MAIN_COLOR_GRADIENT}; color: white;"  
                                @click="($parent.$emit('save_row', props.row), props.expand = !props.expand)" />    
                        </div>
                    </q-td>
                </q-tr>
                """)
                def toggle_edit(msg):
                    row = msg.args['row']
                    row['editing'] = not row.get('editing', False)
                    table.update()

                def save_row(msg):
                    row = msg.args
                    ticket_id = row["id"]
                    # # update_ticket(row)
                    # row['editing'] = False
                    # table.update()
                    ui.notify(f"Запись {ticket_id} обновлена")

                table.on('save_row', save_row)
                table.on('del', lambda msg: delete_on_tickets(msg.args['row']['id'], table, {column: value} if column else None))


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

                table.on('edit', lambda msg: ui.navigate.to(f'/edit/users/{msg.args['row']['id']}'))
                table.on('del', lambda msg: delete_on_users(msg.args['row']['id'], table))