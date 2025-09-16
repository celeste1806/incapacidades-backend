from sqlalchemy import Boolean, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, func

from app.models.base import Base

class Incapacidad(Base):
    __tablename__ = "incapacidad_archivo"

    id_incapacidad_archivo: Mapped [int]= mapped_column(Integer, primary_key=True, autoincrement=True)
    incapacidad_id: Mapped[int] = mapped_column(Integer, ForeignKey("id_incapacidad"))
    archivo_id: Mapped[int] = mapped_column(Integer, ForeignKey("id_incapacidad"))
    url_documento:Mapped[str] = mapped_column(String(280); nullable= False)
    fecha_subida: Mapped[datetime | None] = mapped_column(DateTime, nullable=True, default=func.now())

