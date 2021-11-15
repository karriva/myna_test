from datetime import datetime
from fastapi import APIRouter

from app.models.domain.message import Message

router = APIRouter()


@router.get(
    '/answer',
    response_model=Message,
)
async def answer(
) -> Message:
    ## here will be generate message
    return Message(
        id=1,
        user_id='jhvvj',
        text='Hello',
        response='Hi darling',
        character='Kim',
        created_at=datetime.now()
    )
