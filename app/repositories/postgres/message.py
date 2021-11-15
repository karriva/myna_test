from app.models.domain.message import Message, MessageCreate

from .base import BasePostgresRepository
from .models.message import message


class MessageRepository(BasePostgresRepository[Message, MessageCreate]):
    """
    Postgres repo for games.
    """
    _table = message
    _select_type = Message
