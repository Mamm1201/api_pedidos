# - Contiene funciones como get_all_pedidos(), create_pedido(), etc.
# - Es la capa de acceso a datos
from sqlalchemy.orm import Session
from app.models.models import Pedido
from app.schemas.schemas import PedidoCreate
from fastapi import HTTPException, status

def crear_pedido(db: Session, pedido: PedidoCreate) -> Pedido:
    nuevo_pedido = Pedido(
        producto=pedido.producto,
        cantidad=pedido.cantidad,
        precio=pedido.precio
    )
    db.add(nuevo_pedido)
    db.commit()
    db.refresh(nuevo_pedido)
    return nuevo_pedido

def obtener_pedidos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Pedido).offset(skip).limit(limit).all()

def obtener_pedido_por_id(db: Session, pedido_id: int) -> Pedido:
    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()
    if not pedido:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pedido no encontrado")
    return pedido

def actualizar_pedido(db: Session, pedido_id: int, pedido_update: PedidoCreate) -> Pedido:
    pedido = obtener_pedido_por_id(db, pedido_id)
    pedido.producto = pedido_update.producto
    pedido.cantidad = pedido_update.cantidad
    pedido.precio = pedido_update.precio
    db.commit()
    db.refresh(pedido)
    return pedido

def eliminar_pedido(db: Session, pedido_id: int):
    pedido = obtener_pedido_por_id(db, pedido_id)
    db.delete(pedido)
    db.commit()
