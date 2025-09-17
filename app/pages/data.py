import datetime
from nicegui import ui
from app.styles import MAIN_COLOR, MAIN_COLOR_GRADIENT, QUASAR_PURPLE
from app import ui_elements
from app.decorators import required_role
from app.services.data import get_all_tickets_data, delete_on_tickets, get_all_users_data, delete_on_users, save_edited_ticket_data, save_edited_users_data
from app.utils import check_login_type
from app.models import UserRole, Tickets


@ui.page('/data/tickets', title='Данные театров')
@ui.page('/data/tickets/{column}/{value}', title='Данные театров')
@required_role()
def data_tickets(column: str | None = None, value: str | None = None):
    ui_elements.top_panel('Получение данных', 70)
    # ui_elements.disable_scroll()

    if column:
        column = getattr(Tickets, column)
        if column.type.python_type is int:
            value = int(value)
        elif column.type.python_type is datetime.date:
            value = datetime.datetime.fromisoformat(value)
        data = get_all_tickets_data({column: value})
    else:
        data = get_all_tickets_data()

    is_admin = check_login_type(UserRole.ADMIN)

    with ui.column().style('align-items: center; width: 100%;'):
        with ui.row().style(
            """
            position: absolute;
            top: 30vh;
            width: 30%;
            justify-content: center;
            align-items: flex-start;   
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
                rows=[{**t.model_dump(), 'date': t.date.strftime('%d.%m.%Y')} for t in data],
                pagination=7,
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
                font-size: 0.85rem !important;
            }

            /* если нужно - шаги пагинации/футер */
            .my-table .q-table__bottom {
                font-size: 0.8rem !important;
            }
            """)

            if is_admin:
                table.columns.append({"name": "actions", "label": "Действия", "field": "actions", "align": "center"})
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
                            <q-input color={QUASAR_PURPLE} v-model="props.row.id" dense style="flex:0.10;" readonly input-class="text-center" />
                            <q-input color={QUASAR_PURPLE} v-model="props.row.date" dense style="flex:0.20;" input-class="text-center" />
                            <q-input color={QUASAR_PURPLE} v-model="props.row.theatre_name" dense style="flex:0.19;" input-class="text-center" />
                            <q-input color={QUASAR_PURPLE} v-model="props.row.performance_name" dense style="flex:0.26;" input-class="text-center" />
                            <q-input color={QUASAR_PURPLE} v-model="props.row.tickets_count" dense style="flex:0.16;" input-class="text-center" />
                            <q-btn icon="save" dense style="flex:0.09;" 
                                style="background: {MAIN_COLOR_GRADIENT}; color: white;"  
                                @click="($parent.$emit('save_row', props.row), props.expand = !props.expand)" />    
                        </div>
                    </q-td>
                </q-tr>
                """)

                table.on('save_row', lambda msg: save_edited_ticket_data(msg.args, table, {column: value} if column else None))
                table.on('del', lambda msg: delete_on_tickets(msg.args['row']['id'], table, {column: value} if column else None))


@ui.page('/data/users', title='Данные пользователей')
@required_role(UserRole.ADMIN)
def data_users():
    ui_elements.top_panel('Пользователи', 65)
    # ui_elements.disable_scroll()

    data = get_all_users_data()
    is_admin = check_login_type(UserRole.ADMIN)

    with ui.column().style('align-items: center; width: 100%;'):
        with ui.row().style(
            """
            position: absolute;
            top: 30vh;
            width: 30%;
            justify-content: center;
            align-items: flex-start;   
            """
        ):
            table = ui.table(
                columns=[
                    {"name": "id", "label": "ID", 'field': 'id', 'sortable': True, 'align': 'center'},
                    {"name": "username", "label": "Логин", 'field': 'username', 'sortable': True, 'align': 'center'},
                    {"name": "role", "label": "Роль", 'field': 'role', 'sortable': True, 'align': 'center'},
                ],
                rows=[t.model_dump() for t in data],
                pagination=7,
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
                table.add_slot("body", fr"""
                <q-tr :props="props">
                    <q-td class="text-center" style="width:20%;">{{{{ props.row.id }}}}</q-td>
                    <q-td class="text-center" style="width:30%;">{{{{ props.row.username }}}}</q-td>
                    <q-td class="text-center" style="width:30%;">{{{{ props.row.role }}}}</q-td>
                    <q-td class="text-center" style="width:20%;">
                        <q-btn color="yellow" flat dense 
                            @click="props.expand = !props.expand"
                            :icon="props.expand ? 'remove' : 'edit'" />
                        <q-btn icon="delete" flat dense color='red' @click="$parent.$emit('del', props)" />
                    </q-td>
                </q-tr>

                <q-tr v-show="props.expand" :props="props">
                    <q-td colspan="100%" style="padding:0.25rem;">
                        <div style="display:flex; gap:0.5rem; width:100%;">
                            <q-input color={QUASAR_PURPLE} v-model="props.row.id" dense style="flex:0.20; font-size:1rem;" readonly input-class="text-center" />
                            <q-input color={QUASAR_PURPLE} v-model="props.row.username" dense style="flex:0.31; font-size:1rem;" input-class="text-center" />
                            <q-select
                              color={QUASAR_PURPLE} 
                              v-model="props.row.role"
                              dense
                              style="flex:0.3; font-size:1rem;"
                              input-class="text-center !important"
                              popup-content-class="text-center"
                              :options="{list(UserRole._value2member_map_.keys())}"
                              emit-value
                              map-options
                            />
                            <q-btn icon="save" dense style="flex:0.19; font-size:1rem;" 
                                style="background: {MAIN_COLOR_GRADIENT}; color: white;"  
                                @click="($parent.$emit('save_row', props.row), props.expand = !props.expand)" />    
                        </div>
                    </q-td>
                </q-tr>
                """)
                ui.add_css("""
                    .q-select .q-field__native {
                      display: flex;
                      justify-content: center;
                    }
                """)

                table.on('save_row', lambda msg: save_edited_users_data(msg.args, table))
                table.on('del', lambda msg: delete_on_users(msg.args['row']['id'], table))
