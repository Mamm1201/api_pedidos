from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.schemas import Pedido, PedidoCreate
from app.crud import pedido_crud

router = APIRouter(
    prefix="/pedidos",
    tags=["pedidos"]
)

@router.post("/", response_model=Pedido)
def crear_pedido(pedido: PedidoCreate, db: Session = Depends(get_db)):
    return pedido_crud.crear_pedido(db, pedido)

@router.get("/", response_model=list[Pedido])
def obtener_pedidos(db: Session = Depends(get_db)):
    return pedido_crud.obtener_pedidos(db)

@router.get("/{pedido_id}", response_model=Pedido)
def obtener_pedido(pedido_id: int, db: Session = Depends(get_db)):
    pedido = pedido_crud.obtener_pedido(db, pedido_id)
    if pedido is None:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return pedido

@router.put("/{pedido_id}", response_model=Pedido)
def actualizar_pedido(pedido_id: int, pedido_update: PedidoCreate, db: Session = Depends(get_db)):
    pedido_actualizado = pedido_crud.actualizar_pedido(db, pedido_id, pedido_update)
    if pedido_actualizado is None:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return pedido_actualizado

@router.delete("/{pedido_id}", status_code=204)
def eliminar_pedido(pedido_id: int, db: Session = Depends(get_db)):
    eliminado = pedido_crud.eliminar_pedido(db, pedido_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return {"mensaje": "Pedido eliminado exitosamente"}


