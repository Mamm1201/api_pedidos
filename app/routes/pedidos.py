from fastapi import APIRouter, Depends, HTTPException, status # permite definir rutas agrupadas
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db  # Función para obtener sesión DB
from app.models import Pedido  # Modelo SQLAlchemy
from app.schemas import PedidoCreate, PedidoOut  # Esquemas Pydantic

# Agrupo todas las rutas con el prefijo pedidos
router = APIRouter(
    prefix="/pedidos",
    tags=["pedidos"]
)

# Crear nuevo pedido
@router.post("/", response_model=PedidoOut, status_code=status.HTTP_201_CREATED)
def crear_pedido(pedido: PedidoCreate, db: Session = Depends(get_db)):
    nuevo_pedido = Pedido(
        producto=pedido.producto,
        cantidad=pedido.cantidad,
        precio=pedido.precio
    )
    db.add(nuevo_pedido)
    db.commit()
    db.refresh(nuevo_pedido)  # Refresca para obtener id generado
    return nuevo_pedido

# Obtener lista de pedidos
@router.get("/", response_model=List[PedidoOut])
def listar_pedidos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    pedidos = db.query(Pedido).offset(skip).limit(limit).all()
    return pedidos

# Obtener un pedido por id
@router.get("/{pedido_id}", response_model=PedidoOut)
def obtener_pedido(pedido_id: int, db: Session = Depends(get_db)):
    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return pedido

# Actualizar un pedido por id
@router.put("/{pedido_id}", response_model=PedidoOut)
def actualizar_pedido(pedido_id: int, pedido_update: PedidoCreate, db: Session = Depends(get_db)):
    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")

    pedido.producto = pedido_update.producto
    pedido.cantidad = pedido_update.cantidad
    pedido.precio = pedido_update.precio

    db.commit()
    db.refresh(pedido)
    return pedido

# Eliminar un pedido por id
@router.delete("/{pedido_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_pedido(pedido_id: int, db: Session = Depends(get_db)):
    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")

    db.delete(pedido)
    db.commit()
    return 
