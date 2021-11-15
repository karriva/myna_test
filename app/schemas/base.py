from typing import Generic, List, Optional, TypeVar

from pydantic import BaseModel
from pydantic.generics import GenericModel

Entity = TypeVar('Entity', bound=BaseModel)


class Pagination(GenericModel, Generic[Entity]):
    """ Base class for pagination entities """

    limit: Optional[int]
    offset: int
    total: int
    objects: List[Entity]
