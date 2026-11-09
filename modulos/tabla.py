from sqlalchemy import Column, Integer, String

from database.almacen import miclaseBase


class Producto(miclaseBase):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    stock = Column(Integer, nullable=False, default=0)
