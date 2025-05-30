# models.py
# - Contiene clases que representan las entidades (Usuario, Pedido, etc.)
# - Aplica herencia (Persona → Usuario)
# - Aplica relaciones y enums de forma estructurada y clara

from sqlalchemy import Column, Integer, String, Boolean, Date, Enum, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base
from datetime import date
import enum  # Módulo estándar para crear enumeraciones en Python

# --------------------------------------------
# SUPERCLASE: Persona (NO se convierte en tabla)
# --------------------------------------------
class Persona(Base):
    __abstract__ = True  # Esta clase no se mapea como tabla en la base de datos

    # Campos comunes que pueden heredar otras clases
    nombres = Column(String(255), nullable=False)
    apellidos = Column(String(255), nullable=False)
    telefono = Column(String(20), nullable=False)
    direccion = Column(String(255), nullable=False)

# --------------------------------------------
# MODELO: Usuario (hereda de Persona)
# --------------------------------------------
class Usuario(Persona):
    __tablename__ = "usuarios"  # Nombre real de la tabla en la BD

    id_usuario = Column(Integer, primary_key=True, index=True, autoincrement=True)  # Clave primaria
    email = Column(String(255), unique=True, index=True, nullable=False)  # Email único
    password = Column(String, nullable=False) # estará en la tabla 'usuarios'

    # Relación con Rol
    rol_id = Column(Integer, ForeignKey("roles.id_rol"))  # Llave foránea
    rol = relationship("Rol", back_populates="usuarios")  # Relación inversa con Roles

    # Relación con Pedido (uno a muchos)
    pedidos = relationship("Pedido", back_populates="usuario")  # Un usuario puede tener muchos pedidos

# --------------------------------------------
# ENUM: RolEnum (para representar roles de usuario)
# --------------------------------------------
class RolEnum(enum.Enum):
    admiistrador = "administrador"
    gerente_zona = "gerente_zona"
    vendedor = "vendedor"
    cliente = "cliente"
    
# --------------------------------------------
# MODELO: Rol
# --------------------------------------------

class Rol(Base):
    __tablename__ = "roles"  # Nombre de la tabla

    id_rol = Column(Integer, primary_key=True, index=True)  # Clave primaria
    tipo_rol = Column(Enum(RolEnum), nullable=False)  # Campo Enum para restringir valores

    # Relación con Usuario (uno a muchos)
    usuarios = relationship("Usuario", back_populates="rol")  # Un rol puede estar en varios usuarios

# --------------------------------------------
# MODELO: Pedido
# --------------------------------------------

class Pedido(Base):
    __tablename__ = "pedidos"  # Nombre de la tabla

    id = Column(Integer, primary_key=True, index=True)  # Clave primaria
    producto = Column(String(255), index=True, nullable=False)  # Nombre del producto
    cantidad = Column(Integer, nullable=False)  # Cantidad pedida
    precio = Column(Float, nullable=False)  # Precio del pedido

    # Relación con Usuario (muchos a uno)
    usuario_id = Column(Integer, ForeignKey("usuarios.id_usuario"))  # Llave foránea a Usuario
    usuario = relationship("Usuario", back_populates="pedidos")  # Relación inversa

    # Relación con EstadoPedido (muchos a uno)
    estado_id = Column(Integer, ForeignKey("estados_pedido.id_estado"))  # Llave foránea a EstadoPedido
    estado = relationship("EstadoPedido", back_populates="pedidos")  # Relación inversa

# --------------------------------------------
# ENUM: EstadoPedidoEnum (estados posibles del pedido)
# --------------------------------------------

class EstadoPedidoEnum(enum.Enum):
    pagado = "pagado"
    reenviado = "reenviado"
    enviado = "enviado"
    entregado = "entregado"
    cancelado = "cancelado"

# --------------------------------------------
# MODELO: EstadoPedido
# --------------------------------------------

class EstadoPedido(Base):
    __tablename__ = "estados_pedido"  # Nombre de la tabla

    id_estado = Column(Integer, primary_key=True, index=True)  # Clave primaria
    estado = Column(Enum(EstadoPedidoEnum), nullable=False)  # Campo Enum con estados definidos

    # Relación con Pedido (uno a muchos)
    pedidos = relationship("Pedido", back_populates="estado")  # Un estado puede tener muchos pedidos
