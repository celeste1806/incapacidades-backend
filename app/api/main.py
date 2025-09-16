from fastapi import FastAPI

from app.db.session import test_connection
from app.models.base import Base
from app.models import parametro as _parametro  # noqa: F401  Ensure model import for metadata
from app.models import tipo_incapacidad as _tipo_incapacidad  # noqa: F401  Ensure model import for metadata
from app.models import archivo as _archivo  # noqa: F401  Ensure model import for metadata
from app.db.session import engine
from app.api.v1.routers.parametro_router import router as parametro_router
from app.api.v1.routers.parametro_hijo_router import router as parametro_hijo_router
from app.api.v1.routers.tipo_incapacidad_router import router as tipo_incapacidad_router
from app.api.v1.routers.relacion_router import router as relacion_router
from app.api.archivo_router import router as archivo_router


app = FastAPI(title="API Incapacidades")


@app.on_event("startup")
def on_startup() -> None:
    try:
        test_connection()
        print("[OK] Base de datos conectada correctamente.")
    except Exception as exc:  # noqa: BLE001
        # No abortar la app por fallo de conexión; permitir que /health responda
        print(f"[WARN] Falló la conexión a la base de datos: {exc}")
    # Crear tablas si no existen
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as exc:  # noqa: BLE001
        print(f"[WARN] No fue posible crear/verificar tablas: {exc}")


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}

# Registrar routers
app.include_router(parametro_router, prefix="/api")
app.include_router(parametro_hijo_router, prefix="/api")
app.include_router(tipo_incapacidad_router, prefix="/api")
app.include_router(archivo_router, prefix ="/api" )
app.include_router(relacion_router, prefix="/api")



