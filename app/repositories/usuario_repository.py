from typing import Optional,List
from sqlalchemy.orm import Session


from app.models.usuario import Usuario

class UsuarioRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    # Read
    def list(self, *, skip: int = 0, limit: int = 1000) -> List[Usuario]:
        return (
            self.db.query(Usuario)  # type: ignore[attr-defined]
            .offset(skip)
            .limit(limit)
            .all()
        )


def create(self, *, id_usuario: int, nombre_completo: str, numero_identificacion: str, tipo_identificacion_id: int, tipo_empleador_id: int, cargo_interno: str, correo_electronico: str, password: str, rol_id: int, estado: bool ) -> Usuario:
        entity = Usuario(
            id_usuario=id_usuario,
            nombre_completo=nombre_completo,
            numero_identificacion=numero_identificacion,
            tipo_identificacion_id=tipo_identificacion_id,
            tipo_empleador_id=tipo_empleador_id,
            cargo_interno=cargo_interno,
            correo_electronico=correo_electronico,
            password=password,
            rol_id=rol_id,
            estado=estado,
        )
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity

def get(self, id_usuario: int) -> Usuario | None:
        return self.db.get(Usuario, id_usuario)

def obtener_id(self, id_usuario: int) -> Usuario | None:
        return self.get(id_usuario)

def list(self, *, skip: int = 0, limit: int = 1000) -> List[Usuario]:
        return (
            self.db.query(Usuario)  # type: ignore[attr-defined]
            .offset(skip)
            .limit(limit)
            .all()
        )

def update(self, id_usuario: int, *, nombre_completo: str | None, numero_identificacion: str | None, tipo_identificacion_id: int | None, tipo_empleador_id: int | None, cargo_interno: str | None, correo_electronico: str | None, password: str | None, rol_id: int | None, estado: bool | None) -> Usuario | None:
        entity = self.get(id_usuario)
        if entity is None:
            return None
        if nombre_completo is not None:
            entity.nombre_completo = nombre_completo
        if numero_identificacion is not None:
            entity.numero_identificacion = numero_identificacion
        if tipo_identificacion_id is not None:
            entity.tipo_identificacion_id = tipo_identificacion_id
        if tipo_empleador_id is not None:
            entity.tipo_empleador_id = tipo_empleador_id
        if cargo_interno is not None:
            entity.cargo_interno = cargo_interno
        if correo_electronico is not None:
            entity.correo_electronico = correo_electronico
        if password is not None:
            entity.password = password
        if rol_id is not None:
            entity.rol_id = rol_id
        if estado is not None:
            entity.estado = estado
        self.db.commit()
        self.db.refresh(entity)
        return entity       

def delete(self, id_usuario: int) -> bool:
        entity = self.get(id_usuario)
        if entity is None:
            return False
        self.db.delete(entity)
        self.db.commit()
        return True 

def list_usuarios(
    db: Session,
    rol_id: Optional[int] = None,
    estado: Optional[bool] = None,
    nombre_completo: Optional[str] = None,
    numero_identificacion: Optional[str] = None,
    correo_electronico: Optional[str] = None,
    password: Optional[str] = None,
    tipo_identificacion_id: Optional[int] = None,
    tipo_empleador_id: Optional[int] = None
) -> List[Usuario]:
    query = db.query(Usuario)

    if rol_id is not None:
        query = query.filter(Usuario.rol_id == rol_id)
    if estado is not None:
        query = query.filter(Usuario.estado == estado)
    if nombre_completo is not None:
        query = query.filter(Usuario.nombre_completo == nombre_completo)
    if numero_identificacion is not None:
        query = query.filter(Usuario.numero_identificacion == numero_identificacion)
    if correo_electronico is not None:
        query = query.filter(Usuario.correo_electronico == correo_electronico)
    if password is not None:
        query = query.filter(Usuario.password == password)
    if tipo_identificacion_id is not None:
        query = query.filter(Usuario.tipo_identificacion_id == tipo_identificacion_id)
    if tipo_empleador_id is not None:
        query = query.filter(Usuario.tipo_empleador_id == tipo_empleador_id)

    return query.all()




def update_usuario(
    self,
    id_usuario: int,
    estado: Optional[bool] = None,
    nombre_completo: Optional[str] = None,
    correo_electronico: Optional[str] = None,
    password: Optional[str] = None
) -> bool:
    # Buscar el usuario
    entity = self.get(id_usuario)
    if entity is None:
        return False  # Usuario no encontrado

    # Actualizar solo los campos proporcionados
    if estado is not None:
        entity.estado = estado
    if nombre_completo is not None:
        entity.nombre_completo = nombre_completo
    if correo_electronico is not None:
        entity.correo_electronico = correo_electronico
    if password is not None:
        entity.password = password

    # Guardar los cambios
    self.db.commit()
    return True

def delete_usuario(self, id_usuario: int) -> bool:
    entity = self.get(id_usuario)
    if entity is None:
        return False
    self.db.delete(entity)
    self.db.commit()
    return True
