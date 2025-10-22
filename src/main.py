from fastapi import APIRouter, FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

api_router = APIRouter(prefix="/api/v1")


@api_router.get('/users/me')
def mock_get_users_me():
    mock_user_me = {
        "email": "kruser@yandex.ru",
        "isActive": True,
        "profileId": "1",
        "registeredAt": "2025-06-15T18:29:56+00:00",
        "updatedAt": "2025-06-15T18:29:56+00:00",
        "username": "kruser",
    }
    return JSONResponse(content=mock_user_me, status_code=200)


app = FastAPI(title="FastAI kruser app")
app.include_router(api_router)
app.mount("/assets", StaticFiles(directory="frontend/assets"), name="assets")
app.mount("/", StaticFiles(directory="frontend", html=True), name="static")
