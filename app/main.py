# - Punto de entrada del servidor FastAPI
# - Incluye routers (como pedidos)
from fastapi import FastAPI
from app.controllers import pedido_controller

app = FastAPI()

app.include_router(pedido_controller.router)







