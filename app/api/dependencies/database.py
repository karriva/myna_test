from typing import Any, AsyncGenerator, Callable, Type, TypeVar

from aiopg.sa import Engine, SAConnection
from fastapi import Depends, Request

from app.api.errors.repository import RepositoryHTTPException
from app.core.schema_route import schema
from app.repositories.postgres.base import BasePostgresRepository


def _get_engine(request: Request) -> Engine:
    return request.app.state.db_engine


async def _get_connection(engine: Engine = Depends(_get_engine)) -> AsyncGenerator[SAConnection, None]:
    async with engine.acquire() as conn:
        yield conn


Repository = TypeVar('Repository', bound=BasePostgresRepository[Any, Any])


@schema(
    raises=[
        RepositoryHTTPException,
    ],
)
def get_repository(repository_type: Type[Repository]) -> Callable[[SAConnection], Repository]:
    def _get_repository(connection: SAConnection = Depends(_get_connection)) -> Repository:
        return repository_type(connection)

    return _get_repository
