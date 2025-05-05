from pydantic_settings import BaseSettings
from pathlib import Path
PROJECT_BASE_DIR = Path(__file__).parent.resolve()

class Settings(BaseSettings):
    DEFAULT_JSON_DB_PATH: str = f"{PROJECT_BASE_DIR}/ingredients/db/herbs.json"


settings = Settings()
