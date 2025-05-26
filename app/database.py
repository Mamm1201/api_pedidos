from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Formato de URL:
# mysql+pymysql://usuario:contraseña@host:puerto/base_de_datos

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:Mario1201*@localhost:3306/pandatat"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

