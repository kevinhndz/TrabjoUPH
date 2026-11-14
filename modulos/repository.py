from sqlalchemy.orm import Session
from modulos.tabla import Producto

class RepositoryProducto:
   @staticmethod
   def crear(db: Session, json: Producto) -> Producto:
       db.add(json)
       db.commit()
       db.refresh(json)
       return json


   @staticmethod
   def validar(db: Session, json) -> Producto | None:
       return db.query(Producto).filter(Producto.nombre == json.nombre).first()


   @staticmethod
<<<<<<< HEAD
   def buscar_por_id(db: Session, id: int) -> Producto | None:
       return db.query(Producto).filter(Producto.id == id).first()


   @staticmethod
   def eliminar(db: Session, producto: Producto) -> None:
       db.delete(producto)
       db.commit()

=======
   def listar(db: Session) -> list[Producto]:
       return db.query(Producto).all()


>>>>>>> 0a7c9ee0d4ef5bb4b1f92116d1cb197ca664b375

