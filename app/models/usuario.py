from sqlalchemy import Boolean, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


from app.models.base import Base

class Usuario(Base):
    __tablename__ = "Usuario"

    id_usuario:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre_completo: Mapped[str] = mapped_column(String(150), nullable=False)
    numero_identificacion:Mapped[str] = mapped_column(String(150), nullable=False)
    tipo_identificacion_id:Mapped[int] = mapped_column(Integer, ForeignKey("tipo_identificacion.id_tipo_identificacion"))
    tipo_empleador_id:Mapped[int] = mapped_column(Integer, ForeignKey("tipo_empleador.id_tipo_empleador"))
    cargo_interno:Mapped[str] = mapped_column(String(150), nullable=False)
    correo_electronico:Mapped[str] = mapped_column(String(150), nullable=False)
    password:Mapped[str] = mapped_column(String(150), nullable=False)
    rol_id:Mapped[int] = mapped_column(Integer, ForeignKey("rol.id_rol"))
    estado:Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    