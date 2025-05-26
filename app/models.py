# models.py

from sqlalchemy import Column, Integer, String, Boolean, Date, Enum, Float
from .database import Base
from datetime import date
import enum  # Importamos el módulo enum estándar de Python

# --------------------------------------------
# MODELO: Usuario
# --------------------------------------------

class Usuario(Base):
    __tablename__ = "usuarios"  # Nombre de la tabla

    id_usuario = Column(Integer, primary_key=True, index=True)
    nombres = Column(String(255), nullable=False)
    apellidos = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    telefono_usuario = Column(String(20), nullable=False)
    direccion_usuario = Column(String(255), nullable=False)

# --------------------------------------------
# ENUM: RolEnum (para campo tipo Enum en SQLAlchemy)
# --------------------------------------------

class RolEnum(enum.Enum):
    vendedor = "vendedor"
    comprador = "comprador"

# --------------------------------------------
# MODELO: Rol
# --------------------------------------------

class Roles(Base):
    __tablename__ = "roles"

    id_rol = Column(Integer, primary_key=True, index=True)
    tipo_rol = Column(Enum(RolEnum), nullable=False)  # Campo Enum usando RolEnum

# --------------------------------------------
# MODELO: Pedido
# --------------------------------------------

class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    producto = Column(String(255), index=True, nullable=False)
    cantidad = Column(Integer, nullable=False)
    precio = Column(Float, nullable=False)

# --------------------------------------------
# ENUM: EstadoPedidoEnum
# --------------------------------------------

class EstadoPedidoEnum(enum.Enum):
    pendiente = "pendiente"
    en_proceso = "en_proceso"
    enviado = "enviado"
    entregado = "entregado"
    cancelado = "cancelado"

# --------------------------------------------
# MODELO: EstadoPedido
# --------------------------------------------

class EstadoPedido(Base):
    __tablename__ = "estados_pedido"

    id_estado = Column(Integer, primary_key=True, index=True)
    estado = Column(Enum(EstadoPedidoEnum), nullable=False)
