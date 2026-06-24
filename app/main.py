from fastapi import FastAPI

from app.api.routes import router
from app.logging_config import setup_logging


def create_app() -> FastAPI:
    setup_logging()

    app = FastAPI(
        title="AI Incident Agent",
        version="0.1.0",
        description="FastAPI service for AI-assisted technical incident analysis.",
    )

    app.include_router(router)
    return app


app = create_app()