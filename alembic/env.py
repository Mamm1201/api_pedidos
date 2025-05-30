from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool, create_engine
from alembic import context

import sys
import os
from dotenv import load_dotenv

# 🔧 Aseguramos que Python pueda encontrar app/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ✅ Cargar variables desde .env
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# ✅ Importamos los modelos
from app.database import Base
from app.models import models  # Esto importa todos los modelos para autogenerar

# Alembic Config
config = context.config

# Logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata para autogenerar migraciones
target_metadata = Base.metadata

# ✅ Modo OFFLINE (usado con alembic revision --autogenerate --sql)
def run_migrations_offline() -> None:
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

# ✅ Modo ONLINE (usado con alembic upgrade head)
def run_migrations_online() -> None:
    engine = create_engine(DATABASE_URL, poolclass=pool.NullPool)

    with engine.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

# Ejecutar migraciones según el modo
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

