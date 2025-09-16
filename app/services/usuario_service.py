from typing import List
from sqlalchemy.orm import Session

from app.models.usuario import Usuario
from app.repositories.usuario_repository import UsuarioRepository
from app.schemas.usuario import UsuarioCreate, UsuarioOut, UsuarioUpdate

class UsuarioService:
    def __init__(self, db: Session) -> None:
        self.repou = UsuarioRepository(db)
        
    def create(self, payload: UsuarioCreate) -> UsuarioOut:
        entity = self.repou.create(payload)
        return UsuarioOut.model_validate(entity)

    def get(self, id_usuario: int) -> UsuarioOut | None:
        tipo = self.repou.obtener_id(id_usuario)
        return None if tipo is None else UsuarioOut.model_validate(tipo)

    def list(self, skip: int = 0, limit: int = 100) -> List[UsuarioOut]:
        items = self.repou.list(skip=skip, limit=limit)
        return [UsuarioOut.model_validate(x) for x in items]

    def update(self, id_usuario: int, payload: UsuarioUpdate) -> UsuarioOut | None:
        entity = self.repou.update(
            id_usuario,
            nombre_completo=payload.nombre_completo,
            numero_identificacion=payload.numero_identificacion,
            tipo_identificacion_id=payload.tipo_identificacion_id,
            tipo_empleador_id=payload.tipo_empleador_id,
            cargo_interno=payload.cargo_interno,
            correo_electronico=payload.correo_electronico,
            password=payload.password,
            rol_id=payload.rol_id,
            estado=payload.estado,
        )
        return None if entity is None else UsuarioOut.model_validate(entity)

    def delete(self, id_usuario: int) -> bool:
        return self.repou.delete(id_usuario)