from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field
from pydantic.alias_generators import to_camel


class UserSchema(BaseModel):
    """Base user schema."""
    email: EmailStr = Field(..., description='E-mail пользователя')
    is_active: bool = Field(..., description='Флаг активности пользователя')
    profile_id: int = Field(..., description='Профиль пользователя')
    registered_at: datetime = Field(..., description='Дата и время регистрации пользователя')
    updated_at: datetime = Field(..., description='Дата и время изменения данных пользователя')
    username: str = Field(..., lte=254, description='Имя пользователя')


class UserResponseSchema(UserSchema):
    """User response schema."""

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        json_schema_extra={
            'examples': [
                    {
                    'email': 'example@example.com',
                    'isActive': True,
                    'profileId': '1',
                    'registeredAt': '2025-06-15T18:29:56+00:00',
                    'updatedAt': '2025-06-15T18:29:56+00:00',
                    'username': 'user123',
                    },
                ],
        },
    )
