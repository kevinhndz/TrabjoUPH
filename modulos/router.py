from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database import abrir_puerta
from modulos.repository import RepositoryProducto
from modulos.schema import ProductoCreate, ProductoResponse
from modulos.service import ProductoService

router = APIRouter(prefix="/productos", tags=["Productos"])


def get_producto_service(db: Session = Depends(abrir_puerta)) -> ProductoService:
    return ProductoService(RepositoryProducto(db))


@router.post(
    "/",
    response_model=ProductoResponse,
    status_code=status.HTTP_201_CREATED,
)
def crear_producto(
    datos: ProductoCreate,
    service: ProductoService = Depends(get_producto_service),
):
    return service.crear_producto(datos)