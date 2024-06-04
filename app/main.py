from fastapi import FastAPI
from app.router.routers import api_router

app = FastAPI(title='Api do exercício')

app.include_router(api_router)
