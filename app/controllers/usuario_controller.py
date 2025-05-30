from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from app.schemas.schemas import UsuarioCreate
from app.crud import usuario_crud
from app.database import get_db
from app.core.decoradores import manejar_errores

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.get("/{usuario_id}")
@manejar_errores
async def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    return usuario_crud.get_usuario(db, usuario_id)

@router.get("/email/{email}")
@manejar_errores
async def obtener_por_email(email: str, db: Session = Depends(get_db)):
    return usuario_crud.get_usuario_por_email(db, email)

@router.post("/")
@manejar_errores
async def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return usuario_crud.crear_usuario(db, usuario)
