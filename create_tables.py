# create_tables.py
# - Script de creación de tablas usando mysql.connector

from app.database import engine, Base
from app.models import models  # Importa tus modelos para que SQLAlchemy los reconozca

# Crea todas las tablas en la base de datos
Base.metadata.create_all(bind=engine)

print("✅ Tablas creadas correctamente en la base de datos.")
