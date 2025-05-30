# schemas.py

# schemas.py

from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum

# -------------------------------
# ENUMS para Pydantic (idénticos a los del modelo)
# -------------------------------
class RolEnum(str, Enum):
    admiistrador = "administrador"
    gerente_zona = "gerente_zona"
    vendedor = "vendedor"
    cliente = "cliente"

class EstadoPedidoEnum(str, Enum):
     pagado = "pagado"
     reenviado = "reenviado"
     enviado = "enviado"
     entregado = "entregado"
     cancelado = "cancelado"

# -------------------------------
# ESQUEMAS: Rol
# -------------------------------
class RolBase(BaseModel):
    tipo_rol: RolEnum  # Enum restringe a vendedor o comprador

class RolCreate(RolBase):
    pass  # Es igual a RolBase, útil para crear nuevos roles

class Rol(RolBase):
    id_rol: int  # Devuelto por la BD al consultar

    class Config:
        orm_mode = True  # Habilita compatibilidad con modelos de SQLAlchemy

# -------------------------------
# ESQUEMAS: Usuario
# -------------------------------
class UsuarioBase(BaseModel):
    nombres: str
    apellidos: str
    telefono: str
    direccion: str
    email: EmailStr
    rol_id: int  # debe coincidir con tu modelo (rol_id)
    rol: Rol

class UsuarioCreate(UsuarioBase):
    password: str  # Igual a UsuarioBase para crearlo
    
# UsuarioOut para retornar el usuario sin exponer la contraseña    
class UsuarioOut(UsuarioBase):
    id_usuario: int
    email: str
    rol: Optional[Rol]

    class Config:
        orm_mode = True


class Usuario(UsuarioBase):
    id_usuario: int  # Clave primaria devuelta por la BD
    email: str
    rol_id: Optional[int]
    rol: Optional[Rol]  # Relación con Rol (devuelta en la respuesta)

    class Config:
        orm_mode = True

# -------------------------------
# ESQUEMAS: EstadoPedido
# -------------------------------
class EstadoPedidoBase(BaseModel):
    estado: EstadoPedidoEnum  # Enum con estados válidos

class EstadoPedidoCreate(EstadoPedidoBase):
    pass

class EstadoPedido(EstadoPedidoBase):
    id_estado: int  # Clave primaria del estado

    class Config:
        orm_mode = True

# -------------------------------
# ESQUEMAS: Pedido
# -------------------------------
class PedidoBase(BaseModel):
    producto: str
    cantidad: int
    precio: float
    usuario_id: int  # Relación con Usuario
    estado_id: int   # Relación con EstadoPedido

class PedidoCreate(PedidoBase):
    pass

class Pedido(PedidoBase):
    id: int  # ID del pedido generado por la BD
    usuario: Optional[Usuario]  # Devuelve detalles del usuario si se desea
    estado: Optional[EstadoPedido]  # Devuelve detalles del estado

    class Config:
        orm_mode = True