# - Define los endpoints relacionados a pedidos
# - Usa APIRouter y decoradores como @validar_api_key
from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from typing import List
from fastapi import APIRouter
from app.database import get_db
from app.schemas.schemas import PedidoCreate, Pedido
from app.crud.pedido_crud import (
    crear_pedido,
    obtener_pedidos,
    obtener_pedido_por_id,
    actualizar_pedido,
    eliminar_pedido
)
from app.core.decoradores import validar_api_key

router = APIRouter(
    prefix="/pedidos",
    tags=["Pedidos"]
)

@router.post("/", response_model=Pedido, status_code=status.HTTP_201_CREATED)
@validar_api_key
async def crear_pedido_endpoint(
    request: Request,
    pedido: PedidoCreate,
    db: Session = Depends(get_db)
):
    return crear_pedido(db, pedido)

@router.get("/", response_model=List[Pedido])
@validar_api_key
async def listar_pedidos(
    request: Request,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return obtener_pedidos(db, skip, limit)

@router.get("/{pedido_id}", response_model=Pedido)
@validar_api_key
async def obtener_pedido_endpoint(
    request: Request,
    pedido_id: int,
    db: Session = Depends(get_db)
):
    return obtener_pedido_por_id(db, pedido_id)

@router.put("/{pedido_id}", response_model=Pedido)
@validar_api_key
async def actualizar_pedido_endpoint(
    request: Request,
    pedido_id: int,
    pedido_update: PedidoCreate,
    db: Session = Depends(get_db)
):
    return actualizar_pedido(db, pedido_id, pedido_update)

@router.delete("/{pedido_id}", status_code=status.HTTP_204_NO_CONTENT)
@validar_api_key
async def eliminar_pedido_endpoint(
    request: Request,
    pedido_id: int,
    db: Session = Depends(get_db)
):
    eliminar_pedido(db, pedido_id)
    return None



