from pydantic_settings import BaseSettings
from pathlib import Path
PROJECT_BASE_DIR = Path(__file__).parent.resolve()

class Settings(BaseSettings):
    DEFAULT_JSON_INGREDIENT_DB_PATH: str = f"{PROJECT_BASE_DIR}/ingredients/db/herbs.json"
    DEFAULT_JSON_RECIPE_DB_PATH: str = f"{PROJECT_BASE_DIR}/recipes/db/recipes.json"
    DEFAULT_JSON_TOOL_DB_PATH: str = f"{PROJECT_BASE_DIR}/tools/db/tools.json"


settings = Settings()
