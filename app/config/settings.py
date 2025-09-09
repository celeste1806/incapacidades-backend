import os
from typing import Final

from dotenv import load_dotenv


load_dotenv()


def get_database_url() -> str:
    database_url = os.getenv("DATABASE_URL", "").strip()
    if not database_url:
        raise RuntimeError(
            "DATABASE_URL no está definido en el archivo .env"
        )
    return database_url


# Exponer constante útil para otros módulos
DATABASE_URL: Final[str] = get_database_url()


