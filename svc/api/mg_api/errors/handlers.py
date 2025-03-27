from fastapi import FastAPI

from mg_api.errors import ExcHttp
from mg_api.errors.http import http_handler


def add_exc_handlers(app: FastAPI) -> None:
    app.add_exception_handler(ExcHttp, http_handler)