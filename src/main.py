from fastapi import APIRouter, FastAPI
from fastapi.staticfiles import StaticFiles

from schemas import UserResponseSchema

api_router = APIRouter(prefix='/api/v1')


@api_router.get('/users/me', response_model=UserResponseSchema)
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


app = FastAPI(title='FastAI kruser app')
app.include_router(api_router)
app.mount('/assets', StaticFiles(directory='frontend/assets'), name='assets')
app.mount('/', StaticFiles(directory='frontend', html=True), name='static')
