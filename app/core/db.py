import aiopg.sa

from .settings import settings


async def get_engine() -> aiopg.sa.Engine:
    return await aiopg.sa.create_engine(
        database=settings.POSTGRES_DB,
        user=settings.POSTGRES_USER,
        password=settings.POSTGRES_PASSWORD,
        host=settings.POSTGRES_HOST,
        port=settings.POSTGRES_PORT,
        echo=settings.DEBUG,
    )


async def release_engine(engine: aiopg.sa.Engine) -> None:
    engine.close()
    await engine.wait_closed()
