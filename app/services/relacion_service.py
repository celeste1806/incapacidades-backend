from typing import List
from sqlalchemy.orm import Session

from app.repositories.relacion_repository import RelacionRepository
from app.schemas.relacion import RelacionCreate, RelacionOut


class RelacionService:
    def __init__(self, db: Session) -> None:
        self.repo = RelacionRepository(db)

    # 1) Obtener todos los objetos, con opción de validar si existen
    def list(self, *, skip: int = 0, limit: int = 100, raise_if_empty: bool = False) -> List[RelacionOut]:
        items = self.repo.list(skip=skip, limit=limit)
        if raise_if_empty and not items:
            raise LookupError("No existen relaciones registradas")
        return [RelacionOut.model_validate(x) for x in items]

    # 2) Crear un objeto relacion
    def create(self, payload: RelacionCreate) -> RelacionOut:
        # Si el repositorio expone un exists, se podría validar duplicados
        if hasattr(self.repo, "exists") and self.repo.exists(payload.tipo_incapacidad_id, payload.archivo_id):
            raise ValueError("La relación ya existe para los identificadores proporcionados")
        entity = self.repo.create(
            tipo_incapacidad_id=payload.tipo_incapacidad_id,
            archivo_id=payload.archivo_id,
        )
        return RelacionOut.model_validate(entity)

    # 3) Eliminar un objeto relacion por (tipo_incapacidad_id, archivo_id)
    def delete(self, tipo_incapacidad_id: int, archivo_id: int) -> bool:
        return self.repo.delete(tipo_incapacidad_id=tipo_incapacidad_id, archivo_id=archivo_id)

    # 4) Obtener todos los objetos con el mismo tipo_incapacidad_id
    def list_by_tipo_incapacidad(self, tipo_incapacidad_id: int, *, raise_if_empty: bool = False) -> List[RelacionOut]:
        items = self.repo.list_by_tipo_incapacidad(tipo_incapacidad_id)
        if raise_if_empty and not items:
            raise LookupError("No existen relaciones para el tipo_incapacidad_id proporcionado")
        return [RelacionOut.model_validate(x) for x in items]