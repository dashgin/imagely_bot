from fastapi import APIRouter
from imagely.entrypoints.api.api_v1.endpoints import remove_bg

api_router = APIRouter()
api_router.include_router(remove_bg.router, prefix="/remove-bg", tags=["Editing"])
