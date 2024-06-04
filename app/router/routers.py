from fastapi import APIRouter
from app.entities.atletas.controller import router as atleta
from app.entities.categorias.controller import router as categoria
from app.entities.centros_treinamento.controller import router as centro_treinamento


api_router = APIRouter()

api_router.include_router(atleta, prefix='/atletas', tags=['atletas'])
api_router.include_router(categoria, prefix='/categorias', tags=['categorias'])
api_router.include_router(centro_treinamento, prefix='/centros_treinamento', tags=['centros_treinamento'])