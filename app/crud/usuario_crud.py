# crud/usuario_crud.py

from sqlalchemy.orm import Session
from app.models.models import Usuario, Rol                  # Importar modelos necesarios
from app.schemas.schemas import UsuarioCreate               # Importar esquema para validar datos de entrada
from app.core import seguridad                              # Importar módulo para seguridad (hash de password)
from passlib.context import CryptContext                    # Librería para encriptar contraseñas

# Contexto para hashing, aunque usas el módulo seguridad, lo dejo por si quieres usarlo directamente
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# -------------------------------------------------------
# FUNCIONES CRUD PARA USUARIOS
# -------------------------------------------------------

# Obtener usuario por ID
def get_usuario(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id_usuario == usuario_id).first()

# Obtener usuario por correo electrónico
def get_usuario_por_email(db: Session, email: str):
    return db.query(Usuario).filter(Usuario.email == email).first()

# Crear un nuevo usuario
def crear_usuario(db: Session, usuario: UsuarioCreate):
    # Hashear la contraseña usando función del módulo seguridad
    hashed_password = seguridad.hashear_password(usuario.password)
    
    # Crear instancia del modelo Usuario con los datos recibidos y la contraseña encriptada
    db_usuario = Usuario(
        nombres=usuario.nombres,
        apellidos=usuario.apellidos,
        telefono=usuario.telefono,
        direccion=usuario.direccion,
        email=usuario.email,
        password=hashed_password,
        rol_id=usuario.rol_id
    )
    
    # Agregar el usuario a la sesión
    db.add(db_usuario)
    
    # Confirmar los cambios en la base de datos
    db.commit()
    
    # Actualizar la instancia para obtener datos como el id generado
    db.refresh(db_usuario)
    
    # Devolver el usuario creado
    return db_usuario



