from sqlalchemy.orm import Session

from modulos.schema import ProductoCreate
from modulos.tabla import Producto


class RepositoryProducto:
    def __init__(self, db: Session):
        self.db = db

    def crear(self, datos: ProductoCreate) -> Producto:
        producto = Producto(nombre=datos.nombre, stock=datos.stock)
        self.db.add(producto)
        self.db.commit()
        self.db.refresh(producto)
        return producto