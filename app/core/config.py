from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

BASE_DIR = Path(__file__).resolve().parents[2]

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=(BASE_DIR / ".env", ".env"), extra="ignore")

    APP_NAME: str = "Accessible E-Learning API"
    ENV: str = "development"
    DEBUG: bool = False

    DATABASE_URL: str

    JWT_SECRET: str = Field(..., min_length=16)
    JWT_ALG: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    AUTO_CREATE_TABLES: bool = True

    CORS_ORIGINS: str = "http://localhost:3000,http://127.0.0.1:3000,http://localhost:5500,http://127.0.0.1:5500,null"

settings = Settings()
