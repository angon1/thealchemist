from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEFAULT_JSON_DB_PATH: str = "the_alchemist/ingredients/db/herbs.json"


settings = Settings()
