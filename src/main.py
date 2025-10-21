from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()


# API endpoints


app.mount("/assets", StaticFiles(directory="frontend/assets"), name="assets")
app.mount("/", StaticFiles(directory="frontend", html=True), name="static")
