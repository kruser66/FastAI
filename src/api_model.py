from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, EmailStr, HttpUrl
from pydantic.types import PositiveInt, StrictBool, StrictStr, StringConstraints


class User(BaseModel):
    username: Annotated[str, StringConstraints(max_length=254)]
    """Имя пользователя"""
    email: EmailStr
    """E-mail пользователя"""
    is_active: StrictBool
    """Активный пользователь"""
    profile_id: PositiveInt
    """ID профиля пользователя"""
    registered_at: datetime
    """Дата и время регистрации пользователя"""
    updated_at: datetime
    """Дата и время изменения данных пользователя"""


class Site(BaseModel):
    id: PositiveInt
    """ID сайта"""
    prompt: StrictStr
    """Промпт создания сайта"""
    title: StrictStr
    """Заголовое сайта"""
    screenshot_url: HttpUrl | None = None
    """Ссылка на скриншот сайта"""
    html_code_download_url: HttpUrl | None = None
    """ссылка на загрузку файла"""
    html_code_url: HttpUrl | None = None
    """Ссылка на сайт"""
    created_at: datetime
    """Дата и время создания сайта"""
    updated_at: datetime
    """Дата и время изменения сайта"""
