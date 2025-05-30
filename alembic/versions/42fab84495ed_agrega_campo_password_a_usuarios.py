"""Agrega campo password a usuarios

Revision ID: 42fab84495ed
Revises: be634af32633
Create Date: 2025-05-27 13:04:54.824815

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '42fab84495ed'
down_revision: Union[str, None] = 'be634af32633'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('usuarios', sa.Column(
        'password', 
        sa.String(length=255), 
        nullable=False, 
        server_default='' # usa server default para no fallar la migración
    ))
    # Luego podrías remover el server_default si no deseas dejarlo

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('usuarios', 'password')

