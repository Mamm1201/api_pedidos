# app/core/seguridad.py

from passlib.context import CryptContext

# Instancia del contexto de encriptación con bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hashear_password(password: str) -> str:
    """
    Hashea una contraseña usando bcrypt.
    """
    return pwd_context.hash(password)

def verificar_password(password_plano: str, password_hashed: str) -> bool:
    """
    Verifica si una contraseña plana coincide con el hash almacenado.
    """
    return pwd_context.verify(password_plano, password_hashed)
