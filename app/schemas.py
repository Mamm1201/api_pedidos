# schemas.py

from pydantic import BaseModel, EmailStr
from enum import Enum as PydanticEnum

# -----------------------------
# ENUMS PARA LOS ESQUEMAS
# -----------------------------

# Enum para Rol (compatible con Pydantic y FastAPI)
class RolEnumPydantic(str, PydanticEnum):
    vendedor = "vendedor"
    comprador = "comprador"

# Enum para EstadoPedido
class EstadoPedidoEnumPydantic(str, PydanticEnum):
    pendiente = "pendiente"
    en_proceso = "en_proceso"
    enviado = "enviado"
    entregado = "entregado"
    cancelado = "cancelado"

# -----------------------------
# ESQUEMAS PARA USUARIO
# -----------------------------

class UsuarioBase(BaseModel):
    nombres_usuario: str
    apellidos_usuario: str
    email_usuario: EmailStr  # Validación automática de email
    telefono_usuario: str
    direccion_usuario: str
    is_active: bool = True

class UsuarioCreate(UsuarioBase):
    password_usuario: str  # Se incluye la contraseña para crear usuario

class UsuarioOut(UsuarioBase):
    id_usuario: int

    class Config:
        orm_mode = True  # Permite leer de ORM SQLAlchemy directamente

# -----------------------------
# ESQUEMAS PARA ROL
# -----------------------------

class RolBase(BaseModel):
    tipo_rol: RolEnumPydantic

class RolCreate(RolBase):
    pass

class RolOut(RolBase):
    id_rol: int

    class Config:
        orm_mode = True

# -----------------------------
# ESQUEMAS PARA PEDIDO
# -----------------------------

class PedidoBase(BaseModel):
    producto: str
    cantidad: int
    precio: float

class PedidoCreate(PedidoBase):
    pass

class PedidoOut(PedidoBase):
    id: int

    class Config:
        orm_mode = True

# -----------------------------
# ESQUEMAS PARA ESTADO PEDIDO
# -----------------------------

class EstadoPedidoBase(BaseModel):
    estado: EstadoPedidoEnumPydantic

class EstadoPedidoCreate(EstadoPedidoBase):
    pass

class EstadoPedidoOut(EstadoPedidoBase):
    id_estado: int

    class Config:
        orm_mode = True
