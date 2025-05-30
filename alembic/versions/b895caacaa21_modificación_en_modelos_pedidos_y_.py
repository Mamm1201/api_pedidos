"""modificación en modelos: pedidos y usuarios

Revision ID: b895caacaa21
Revises: a148b3395e4e
Create Date: 2025-05-27 09:06:40.605141

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'b895caacaa21'
down_revision: Union[str, None] = 'a148b3395e4e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('estados_pedido', 'estado',
               existing_type=mysql.ENUM('pendiente', 'en_proceso', 'enviado', 'entregado', 'cancelado', collation='utf8mb4_unicode_ci'),
               type_=sa.Enum('pagado', 'reenviado', 'enviado', 'entregado', 'cancelado', name='estadopedidoenum'),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('estados_pedido', 'estado',
               existing_type=sa.Enum('pagado', 'reenviado', 'enviado', 'entregado', 'cancelado', name='estadopedidoenum'),
               type_=mysql.ENUM('pendiente', 'en_proceso', 'enviado', 'entregado', 'cancelado', collation='utf8mb4_unicode_ci'),
               existing_nullable=False)
    # ### end Alembic commands ###
