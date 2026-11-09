import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine


load_dotenv()

UBICACION_ALMACEN = os.getenv("DATABASE_URL", "sqlite:///base.db")

motor = create_engine(UBICACION_ALMACEN, connect_args={"check_same_thread": False})
llaves = sessionmaker(bind=motor)


class miclaseBase(DeclarativeBase):
    pass


def abrir_puerta():
    db = llaves()
    try:
        yield db
    finally:
        db.close()
