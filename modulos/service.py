from modulos.repository import RepositoryProducto
from modulos.schema import ProductoCreate
from modulos.tabla import Producto


class ProductoService:
    def __init__(self, repository: RepositoryProducto):
        self.repository = repository

    def crear_producto(self, datos: ProductoCreate) -> Producto:
        return self.repository.crear(datos)