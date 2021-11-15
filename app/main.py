from logging import basicConfig

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.routes import private_router, public_router
from app.core.events import create_start_app_handler, create_stop_app_handler
from app.core.settings import settings


def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.MICROSERVICE_NAME, debug=settings.DEBUG, version=settings.VERSION,
    )

    application.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )

    application.add_event_handler('startup', create_start_app_handler(application))
    application.add_event_handler('shutdown', create_stop_app_handler(application))

    application.include_router(private_router)
    application.include_router(public_router, prefix=settings.API_PREFIX)

    return application


app = get_application()
basicConfig(level=settings.LOG_LEVEL)
