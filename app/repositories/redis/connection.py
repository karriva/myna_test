from types import TracebackType
from typing import Optional, Type

import aioredis
from aioredis import Redis

from app.core.settings import settings


async def get_redis_connection() -> Redis:
    return await aioredis.create_redis(
        settings.REDIS_URL, db=settings.REDIS_DB, password=settings.REDIS_PASSWORD,
    )


class RedisCtxManager:
    """Redis context manager"""

    def __init__(self) -> None:
        self.redis: Redis

    async def __aenter__(self) -> Redis:
        self.redis = await get_redis_connection()
        return self.redis

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> bool:
        self.redis.close()
        await self.redis.wait_closed()
        return False
