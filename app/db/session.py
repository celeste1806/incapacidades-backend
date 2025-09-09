from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from app.config.settings import DATABASE_URL


engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def test_connection() -> None:
    # Ejecuta un ping simple a la base de datos
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


