# create_tables.py

from app.database import engine, Base
from app import models  # Importa tus modelos para que SQLAlchemy los reconozca

# Crea todas las tablas en la base de datos
Base.metadata.create_all(bind=engine)

print("✅ Tablas creadas correctamente en la base de datos.")
