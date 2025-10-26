from fastapi import APIRouter, FastAPI
from fastapi.staticfiles import StaticFiles

from schemas.sites import SiteRequestSchema, SiteResponseSchema
from schemas.users import UserResponseSchema

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


@api_router.post('/sites/create', response_model=SiteResponseSchema)
def mock_site_create(request: SiteRequestSchema):
    mock_site_created = {
        'id': 1,
        'title': 'Фан клуб Домино',
        'prompt': 'Сайт любителей играть в домино',
        'screenshotUrl': 'http://example.com/media/index.png',
        'htmlCodeDownloadUrl': 'http://example.com/media/index.html?response-content-disposition=attachment',
        'htmlCodeUrl': 'http://example.com/media/index.html',
        'createdAt': '2025-06-15T18:29:56+00:00',
        'updatedAt': '2025-06-15T18:29:56+00:00',
    }
    return mock_site_created


app = FastAPI(title='FastAI kruser app')
app.include_router(api_router)
app.mount('/assets', StaticFiles(directory='frontend/assets'), name='assets')
app.mount('/', StaticFiles(directory='frontend', html=True), name='static')
