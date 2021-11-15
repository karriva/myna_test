from fastapi import APIRouter

from app.core.settings import settings

from . import answer

router = APIRouter()
router.include_router(answer.router)


@router.get('/ping', response_model=str)
async def ping() -> str:
    return settings.MICROSERVICE_NAME
