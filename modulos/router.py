from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import abrir_puerta
from modulos.schema import ProductoResponse, Revisar_Json_Crear
from modulos.service import ProductoService as service

router = APIRouter(prefix="/productos", tags=["Productos"])


@router.post(
   "/",
   response_model=ProductoResponse,
   status_code=status.HTTP_201_CREATED,
)
def crear_producto(
   json: Revisar_Json_Crear,
   db: Session = Depends(abrir_puerta),
):
   return service.crear_producto_service(db, json)
