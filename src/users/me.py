from pydantic import ConfigDict
from pydantic.alias_generators import to_camel

from api_model import User

from .router import user_router


class UserResponseSchema(User):
    """User response schema."""

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        use_attribute_docstrings=True,
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


@user_router.get('/users/me', response_model=UserResponseSchema)
def mock_get_users_me():
    mock_user_me = {
        'email': 'kruser@yandex.ru',
        'is_active': True,
        'profile_id': '1',
        'registered_at': '2025-06-15T18:29:56+00:00',
        'updated_at': '2025-06-15T18:29:56+00:00',
        'username': 'kruser',
    }
    return mock_user_me
