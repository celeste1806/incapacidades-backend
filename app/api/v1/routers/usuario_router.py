from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.usuario import UsuarioCreate, UsuarioOut, UsuarioUpdate
from app.services.usuario import UsuarioService

router = APIRouter()

def get_service(db: Session = Depends(get_db)) -> UsuarioService:
    return UsuarioService(db)


@router.post("/usuario", response_model=UsuarioOut)
def create_Usuario(
    payload: UsuarioCreate,
    service: UsuarioService = Depends(get_service),
):
    return service.create(payload)

@router.get("/usuario/{id_usuario}", response_model=UsuarioOut)
def get_usuario(
    id_usuario: int,
    service: UsuarioService = Depends(get_service),
):
    result = service.get(id_usuario)
    if result is None:  
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return result

@router.get("/usuario", response_model=list[UsuarioOut])
def list_usuario(
    skip: int = 0,
    limit: int = 100,
    service: UsuarioService = Depends(get_service),
):
    return service.list(skip=skip, limit=limit)
    
@router.put("/usuario/{id_usuario}", response_model=UsuarioOut)
def update_usuario(
    id_usuario: int,
    payload: UsuarioUpdate,
    service: UsuarioService = Depends(get_service),
):
    result = service.update(id_usuario, payload)
    if result is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return result

@router.delete("/usuario/{id_usuario}")
def delete_usuario(
    id_usuario: int,
    service: UsuarioService = Depends(get_service),
):
    success = service.delete(id_usuario)
    if not success:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"message": "Usuario eliminado correctamente"}