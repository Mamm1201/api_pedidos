from fastapi import FastAPI
from app import database
from app import models
from app.routes import pedidos

app = FastAPI()

# Crear tablas en la base de datos
models.Base.metadata.create_all(bind=database.engine)

# Incluir rutas del router de pedidos
app.include_router(pedidos.router)

@app.get("/")
def root():
    return {"mensaje": "API de Pedidos funcionando"}

