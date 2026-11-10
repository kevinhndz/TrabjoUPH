from pydantic import BaseModel, ConfigDict, Field

class Revisar_Json_Crear(BaseModel):
   nombre: str = Field(..., min_length=3, max_length=255)
   #Aplicando el principio de la TRIADA (INTEGRACION)
   stock: int = Field(..., ge=0)



class ProductoResponse(BaseModel):
   model_config = ConfigDict(from_attributes=True)

   id: int
   nombre: str
   stock: int
