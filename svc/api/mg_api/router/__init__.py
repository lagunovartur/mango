from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter
from mg_api.router import auth
from mg_api.router import chat
from mg_api.router import message
from mg_api.router import user
from . import sio


def root_router() -> APIRouter:
    router = APIRouter(route_class=DishkaRoute, prefix="/api")
    router.include_router(auth.router)
    router.include_router(chat.router)
    router.include_router(message.router)
    router.include_router(user.router)
    return router
