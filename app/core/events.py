from typing import Any, Callable

from fastapi import FastAPI

from . import db


def create_start_app_handler(app: FastAPI) -> Callable[[], Any]:
    async def start_app() -> None:
        app.state.db_engine = await db.get_engine()
    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable[[], Any]:
    async def stop_app() -> None:
        await db.release_engine(app.state.db_engine)
    return stop_app
