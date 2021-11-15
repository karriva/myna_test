import os
from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Global project settings, from .env
    """

    DEBUG: bool = True
    LOG_LEVEL: str = 'INFO'

    # common
    MICROSERVICE_NAME: str = 'myna test'
    VERSION: str = '0.0.1'
    API_PREFIX: str = '/public/api/v1'

    # database
    POSTGRES_USER: str = 'postgres'
    POSTGRES_PASSWORD: Optional[str] = 'postgres'
    POSTGRES_DB: str = 'postgres'
    POSTGRES_HOST: str = 'postgres'
    POSTGRES_PORT: int = 5432

    class Config:
        """Config"""

        env_file = os.getenv('ENV', '.env')


settings = Settings()
