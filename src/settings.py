from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    """Главные настройки приложения. Загружаются из .env."""

    ai_token: SecretStr = Field(
        ...,
        description="Токен для доступа к API. Никому не передавайте!",
    )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = AppSettings()
