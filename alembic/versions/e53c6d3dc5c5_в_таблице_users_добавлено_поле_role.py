"""в таблице Users добавлено поле role

Revision ID: e53c6d3dc5c5
Revises: 18132252bfd2
Create Date: 2025-09-10 13:15:17.292996
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = 'e53c6d3dc5c5'
down_revision: Union[str, Sequence[str], None] = '18132252bfd2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # 1. Создаём ENUM-тип
    userrole_enum = postgresql.ENUM('USER', 'ADMIN', name='userrole')
    userrole_enum.create(op.get_bind())

    # 2. Добавляем колонку
    op.add_column(
        'users',
        sa.Column('role', userrole_enum, nullable=False, server_default='USER')
    )
    op.create_index(op.f('ix_users_role'), 'users', ['role'], unique=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f('ix_users_role'), table_name='users')
    op.drop_column('users', 'role')

    # Удаляем ENUM-тип
    userrole_enum = postgresql.ENUM('USER', 'ADMIN', name='userrole')
    userrole_enum.drop(op.get_bind())
