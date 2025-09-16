from pydantic import BaseModel, Field


class TipoIncapacidadBase(BaseModel):
    id_tipo_incapacidad: int
    nombre: str = Field(min_length=1, max_length=150)
    descripcion: str | None = Field(default=None, max_length=255)
    estado: bool = True


class TipoIncapacidadCreate(TipoIncapacidadBase):
    pass


class TipoIncapacidadUpdate(BaseModel):
    id_tipo_incapacidad: int | None = Field(default=None)
    nombre: str | None = Field(default=None, min_length=1, max_length=150)
    descripcion: str | None = Field(default=None, max_length=255)
    estado: bool | None = None


class TipoIncapacidadOut(TipoIncapacidadBase):
    id_tipo_incapacidad: int

    class Config:
        from_attributes = True
