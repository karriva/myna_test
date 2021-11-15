from admin_lib import SettingsRepository

from app.core.settings import settings
from app.models.schemas.settings import GameAdminSettings


def get_settings_repository() -> SettingsRepository:
    return SettingsRepository(
        settings_model=GameAdminSettings,
        minio_endpoint=settings.MINIO_ENDPOINT,
        minio_access_key=settings.MINIO_ACCESS_KEY,
        minio_secret_key=settings.MINIO_SECRET_KEY,
        minio_bucket_name=settings.MINIO_BUCKET_NAME,
        minio_secure=settings.MINIO_SECURE,
        partner_api_key=settings.PARTNER_API_KEY,
        partner_game_name=settings.PARTNER_GAME_NAME,
    )
