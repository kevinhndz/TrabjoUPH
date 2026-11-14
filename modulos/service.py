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

<<<<<<< HEAD

   @staticmethod
   def eliminar_producto_service(db: Session, id: int) -> None:
       producto = repo.buscar_por_id(db, id)

       if producto is None:
           raise HTTPException(
               status_code=status.HTTP_404_NOT_FOUND,
               detail="No existe un producto con ese id.",
           )

       repo.eliminar(db, producto)
=======
   @staticmethod
   def listar_productos_service(db: Session) -> list[Producto]:
       return repo.listar(db)
>>>>>>> 0a7c9ee0d4ef5bb4b1f92116d1cb197ca664b375
