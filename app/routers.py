from fastapi import APIRouter
from app.api import home_router


api_router = APIRouter()

api_router.include_router(home_router, prefix='/api')
