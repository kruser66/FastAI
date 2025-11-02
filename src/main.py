from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from sites import site_router
from users import user_router

app = FastAPI(title='FastAI kruser app')

app.include_router(user_router)
app.include_router(site_router)

app.mount('/assets', StaticFiles(directory='frontend/assets'), name='assets')
app.mount('/', StaticFiles(directory='frontend', html=True), name='static')
