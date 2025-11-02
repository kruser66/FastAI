from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, EmailStr
from pydantic.types import PositiveInt, StrictBool, StringConstraints


class User(BaseModel):
    """API user model."""
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
