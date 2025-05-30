from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.schemas import UsuarioCreate, Usuario, UsuarioOut  # Pydantic
from app.models.models import Usuario as UsuarioModel  # SQLAlchemy
from app.crud.usuario_crud import crear_usuario
from app.database import get_db
from app.dependencias import verificar_rol
from app.core.decoradores import manejar_errores

router = APIRouter(tags=["Usuarios"])

@router.post("/", response_model=Usuario)
@manejar_errores
async def crear_usuario_endpoint(
    datos: UsuarioCreate,
    db: Session = Depends(get_db),
    usuario_actual: Usuario = Depends(verificar_rol(["admin"]))
):
    nuevo_usuario = crear_usuario(db, datos)
    if not nuevo_usuario:
        raise HTTPException(status_code=500, detail="Error al crear el usuario")
    return nuevo_usuario


@router.get("/", response_model=List[UsuarioOut])
@manejar_errores
async def obtener_usuarios(
    db: Session = Depends(get_db),
    usuario_actual: Usuario = Depends(verificar_rol(["admin"]))
):
    usuarios = db.query(UsuarioModel).all()
    return usuarios










