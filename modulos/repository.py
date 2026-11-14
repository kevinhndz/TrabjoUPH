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
   def listar(db: Session) -> list[Producto]:
       return db.query(Producto).all()



