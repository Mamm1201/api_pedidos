# - Define decoradores reutilizables como validación de API Key

from fastapi import Request, HTTPException, status
from functools import wraps
import traceback

def validar_api_key(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        # Busca el objeto Request en los argumentos (que FastAPI pasa automáticamente)
        request: Request = None
        for arg in args:
            if isinstance(arg, Request):
                request = arg
                break
        if not request:
            request = kwargs.get("request")
        if not request:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Request no encontrado"
            )
        api_key = request.headers.get("x-api-key")
        if api_key != "tu_api_key_secreta":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="API key inválida"
            )
        return await func(*args, **kwargs)
    return wrapper

def manejar_errores(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except HTTPException:
            raise  # deja pasar errores FastAPI normales
        except Exception as e:
            # Puedes loguear aquí si quieres
            traceback.print_exc()
            raise HTTPException(
                status_code=500,
                detail=f"Error interno del servidor: {str(e)}"
            )
    return wrapper



