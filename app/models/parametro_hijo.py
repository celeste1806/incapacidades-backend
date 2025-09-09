from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column


from app.models.base import Base

class ParametroHijo(Base):
    __tablename__ = "parametro_hijo"

    id_parametrohijo:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    parametro_id:Mapped[int] = mapped_column(Integer, ForeignKey("parametro.id_parametro"))
    nombre:Mapped[str] = mapped_column(String(50), nullable=False)
    descripcion:Mapped[str] = mapped_column(String(50), nullable=False)
    estado:Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

