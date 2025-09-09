from fastapi import FastAPI

from app.db.session import test_connection
from app.models.base import Base
from app.models import parametro as _parametro  # noqa: F401  Ensure model import for metadata
from app.db.session import engine
from app.api.v1.routers.parametro_router import router as parametro_router


app = FastAPI(title="API Incapacidades")


@app.on_event("startup")
def on_startup() -> None:
    try:
        test_connection()
        print("[OK] Base de datos conectada correctamente.")
    except Exception as exc:  # noqa: BLE001
        print(f"[ERROR] Falló la conexión a la base de datos: {exc}")
        raise
    # Crear tablas si no existen
    Base.metadata.create_all(bind=engine)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}

# Registrar routers
app.include_router(parametro_router, prefix="/api")


