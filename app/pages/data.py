from nicegui import ui
from app.styles import MAIN_COLOR
from app import ui_elements
from app.decorators import required_status
from app.services.data import get_all_data, delete_instance
from app.utils import check_login_type
from app.models import UserRole


@ui.page('/data', title='Данные театров')
@required_status()
def data():
    ui_elements.top_panel()
    ui_elements.disable_scroll()

    data = get_all_data()
    is_admin = check_login_type(UserRole.ADMIN)

    with ui.column().style('align-items: center; width: 100%;'):
        with ui.column().style('position: relative; width: 100%; align-items: center;'):
            ui.label('Получение данных').style(
                f'font-size: 6rem; '
                f'text-align: center; '
                f'border: 4px solid {MAIN_COLOR}; '
                f'padding: 2rem;'
                f'border-radius: 1rem;'
                f'transform: translateY(-10vh);'
                f'width: 70%;'
            )
        with ui.row().style(
            f"""
            width: 70%;
            height: 100vh;
            align-items: center;
            justify-content: center;
            display: flex;
            flex-direction: row;
            transform: translateY(-30vh);
            """
        ):
            table = ui.table(
                columns=[
                    {"name": "id", "label": "ID", 'field': 'id', 'sortable': True, 'align': 'center'},
                    {"name": "data", "label": "Дата", 'field': 'data', 'align': 'center'},
                    {"name": "theatre_name", "label": "Театр", 'field': 'theatre_name', 'align': 'center'},
                    {"name": "performance_name", "label": "Выступление", 'field': 'performance_name', 'align': 'center'},
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
                table.on('del', lambda msg: delete_instance(msg.args['row']['id'], table))