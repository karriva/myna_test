from abc import ABC, abstractmethod
from typing import Any, Dict, Generic, List, Type, TypeVar

from aiopg.sa import SAConnection
from psycopg2.errors import ForeignKeyViolation, UniqueViolation
from pydantic import BaseModel
from sqlalchemy import Table, delete, func, insert, select, update

from .errors import NotFoundError, UniqueViolationError

ModelSelectType = TypeVar('ModelSelectType', bound=BaseModel)
ModelCreateType = TypeVar('ModelCreateType', bound=BaseModel)


class BasePostgresRepository(Generic[ModelSelectType, ModelCreateType], ABC):
    """
    Base CRUD Repository for Postgres
    """

    @property
    @abstractmethod
    def _table(self) -> Table:
        ...

    @property
    @abstractmethod
    def _select_type(self) -> Type[ModelSelectType]:
        ...

    def __init__(self, connection: SAConnection):
        self._connection = connection

    async def count_all(self) -> int:
        query = select([func.count(self._table.c.id)])
        rows = await self._connection.execute(query)
        entities = await rows.fetchone()
        return entities[0]

    async def get(self, entity_id: int) -> ModelSelectType:
        query = select([self._table]).where(self._table.c.id == entity_id).limit(1)
        rows = await self._connection.execute(query)
        row = await rows.first()
        if row is None:
            raise NotFoundError(message=f'Not found {self._table} with id {entity_id}')
        return self._select_type(**row)

    async def create(self, entity: ModelCreateType) -> int:
        try:
            statement = (
                insert(self._table).values(**entity.dict()).returning(self._table.c.id)
            )
            return await self._connection.scalar(statement)
        except UniqueViolation as exception:
            raise UniqueViolationError(
                message=exception.diag.message_detail,
            ) from exception
        except ForeignKeyViolation as exception:
            raise NotFoundError(message=exception.diag.message_detail) from exception

    async def create_many(self, entities: List[ModelCreateType]) -> List[int]:
        try:
            statement = (
                insert(self._table)
                .values([entity.dict() for entity in entities])
                .returning(self._table.c.id)
            )
            cur = await self._connection.execute(statement)
            return await cur.fetchall()
        except UniqueViolation as exception:
            raise UniqueViolationError(
                message=exception.diag.message_detail,
            ) from exception
        except ForeignKeyViolation as exception:
            raise NotFoundError(
                message=exception.diag.message_detail,
            ) from exception

    async def update(self, entity_id: int, **kwargs: Dict[str, Any]) -> None:
        """
        Update an entity of given `id` with given fields.
        """
        try:
            statement = (
                update(self._table)
                .where(self._table.c.id == entity_id)
                .values(kwargs)
            )
            cur = await self._connection.execute(statement)
            if cur.rowcount == 0:
                raise NotFoundError(message=f'Not found {self._table} with id {entity_id}')
        except UniqueViolation as exception:
            raise UniqueViolationError(
                message=exception.diag.message_detail,
            ) from exception

    async def delete(self, entity_id: int) -> None:
        """
        Delete an entity of given `id`.
        """
        statement = (
            delete(self._table)
            .where(self._table.c.id == entity_id)
        )
        cur = await self._connection.execute(statement)
        if cur.rowcount == 0:
            raise NotFoundError(message=f'Not found {self._table} with id {entity_id}')
