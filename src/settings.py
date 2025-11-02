from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    """Главные настройки приложения. Загружаются из .env."""

    PROJECT_ROOT: Path = Path(__file__).parent
    MOCK_DIR: Path = PROJECT_ROOT / 'mock'
    AI_TOKEN: SecretStr
    """Токен для доступа к API. Никому не передавайте!"""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = AppSettings()
