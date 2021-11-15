from sqlalchemy import Column, DateTime, Integer, String, Table, func

from .base import metadata

message = Table(
    'message',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user_id', String),
    Column('text', String, nullable=False),
    Column('response', String, nullable=False),
    Column('character', String, nullable=False),

    Column('created_at', DateTime, nullable=False, index=True, server_default=func.now()),
)
