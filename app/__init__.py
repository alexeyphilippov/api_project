import logging

from logging.config import dictConfig
from typing import Optional

from fastapi import FastAPI, Request
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware

from app.logging_config import loggingConfig
from config import Config

app: Optional[FastAPI] = None


def create_app() -> FastAPI:
    global app
    session_middleware = [
        Middleware(SessionMiddleware, secret_key=Config.SECRET_KEY)
    ]

    app = FastAPI(middleware=session_middleware)
    dictConfig(loggingConfig)
    logging.getLogger('werkzeug').disabled = True

    from app.routes import router

    app.include_router(router)

    return app
