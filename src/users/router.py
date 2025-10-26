from fastapi import APIRouter

from users.schemas import UserResponseSchema

user_router = APIRouter(prefix='/api/v1')


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
