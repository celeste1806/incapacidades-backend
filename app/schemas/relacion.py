from pydantic import BaseModel, Field


class RelacionBase(BaseModel):
    tipo_incapacidad_id: int 
    archivo_id: int


class RelacionUpdate(BaseModel):
    pass
class RelacionCreate(RelacionBase):
    pass

class RelacionOut(RelacionBase):
    pass

    