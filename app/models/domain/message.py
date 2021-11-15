from datetime import datetime

from pydantic import BaseModel, Extra, root_validator


class MessageBase(BaseModel):
    """
    Base entity with fields & validation.
    """
    user_id: str
    text: str
    response: str
    character: str


class MessageCreate(MessageBase):
    """
    Entity for db record creation.
    """


class Message(MessageBase):
    """
    Entity with played game info persisted to db.
    """
    id: int  # noqa: A003; because `id` is table primary key
    created_at: datetime
