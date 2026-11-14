from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from modulos.repository import RepositoryProducto as repo
from modulos.schema import Revisar_Json_Crear
from modulos.tabla import Producto


class ProductoService:
   @staticmethod
   def crear_producto_service(
       db: Session, json: Revisar_Json_Crear
   ) -> Producto:
       look = repo.validar(db, json)


       if look is not None:
           raise HTTPException(
               status_code=status.HTTP_409_CONFLICT,
               detail="Ya existe un producto con ese nombre.",
           )


       producto = Producto(nombre=json.nombre, stock=json.stock)
       return repo.crear(db, producto)

   @staticmethod
   def listar_productos_service(db: Session) -> list[Producto]:
       return repo.listar(db)
