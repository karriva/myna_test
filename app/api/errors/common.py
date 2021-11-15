from typing import Any, Dict, Optional, Type

from fastapi import HTTPException
from pydantic import BaseModel


class SchemaEnhancedHTTPException(HTTPException):
    """Exception which also generates schema of its response"""

    __model__: Type[BaseModel]

    default_status_code: int

    default_error_kind: str
    default_error_code: int

    message: Optional[str]

    def __init__(
        self,
        message: Optional[str] = None,
        headers: Optional[Dict[str, Any]] = None,
        details: Optional[Dict[str, Any]] = None,
    ) -> None:
        if self.default_status_code is None:
            raise ValueError('Default status code is empty')
        if self.default_error_kind is None:
            raise ValueError('Default error kind is empty')
        if self.default_error_code is None:
            raise ValueError('Default error code is empty')
        if self.message is None and message is None:
            raise ValueError('Default error message is empty')

        if message:
            self.message = message
        self.extra_details = details

        super().__init__(self.default_status_code, self.content, headers)

    @property
    def content(self) -> Dict[str, Any]:
        return {
            'kind': self.default_error_kind,
            'code': self.default_error_code,
            'message': self.message,
            'extra_details': self.extra_details,
        }

    @classmethod
    def get_openapi_model_type(cls) -> Type[BaseModel]:
        if getattr(cls, '__model__', None) is None:
            model = type(
                cls.__name__,
                (BaseModel,),
                {
                    'kind': cls.default_error_kind,
                    'code': cls.default_error_code,
                    'message': cls.message,
                    'extra_details': {},
                },
            )
            cls.__model__ = model
        return cls.__model__
