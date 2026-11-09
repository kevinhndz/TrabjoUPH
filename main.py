from fastapi import FastAPI

from database import miclaseBase, motor
from modulos.router import router as productos_router
from modulos import tabla  # noqa: F401  (registra la tabla en la Base)

miclaseBase.metadata.create_all(bind=motor)

app = FastAPI(title="API de Productos")
app.include_router(productos_router)