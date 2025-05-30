from fastapi import Depends, HTTPException, status
from app.schemas.schemas import Usuario, Rol

# Simula la obtención del usuario autenticado
async def obtener_usuario_actual() -> Usuario:
    return Usuario(
        id_usuario=1,
        nombres="Admin",
        apellidos="Test",
        email="admin@example.com",
        telefono="1234567890",
        direccion="Calle Falsa 123",
        rol=Rol(
            id_rol=1,
            tipo_rol="administrador"
        )
    )

def verificar_rol(roles_permitidos: list[str]):
    async def dependencia(usuario_actual: Usuario = Depends(obtener_usuario_actual)):
        if usuario_actual.rol.tipo_rol not in roles_permitidos:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No tienes permisos para realizar esta acción"
            )
        return usuario_actual
    return dependencia



