from typing import List
from sqlalchemy.orm import Session

from app.models.relacion import Relacion


class RelacionRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    # Read
    def list(self, *, skip: int = 0, limit: int = 1000) -> List[Relacion]:
        return (
            self.db.query(Relacion)  # type: ignore[attr-defined]
            .offset(skip)
            .limit(limit)
            .all()
        )

    # Create
    def create(self, *, tipo_incapacidad_id: int, archivo_id: int) -> Relacion:
        entity = Relacion(
            tipo_incapacidad_id=tipo_incapacidad_id,
            archivo_id=archivo_id,
        )
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity

    # Delete (by composite keys)
    def delete(self, *, tipo_incapacidad_id: int, archivo_id: int) -> bool:
        entity = (
            self.db.query(Relacion)
            .filter(
                Relacion.tipo_incapacidad_id == tipo_incapacidad_id,
                Relacion.archivo_id == archivo_id,
            )
            .first()
        )
        if entity is None:
            return False
        self.db.delete(entity)
        self.db.commit()
        return True

    # Read by tipo_incapacidad_id
    def list_by_tipo_incapacidad(self, *, tipo_incapacidad_id: int) -> List[Relacion]:
        return (
            self.db.query(Relacion)
            .filter(Relacion.tipo_incapacidad_id == tipo_incapacidad_id)
            .all()
        )
