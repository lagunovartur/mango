from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter
from mg_api.router import auth
from mg_api.router import chat
from . import sio


def router_factory():
    router = APIRouter(route_class=DishkaRoute, prefix="/api")
    router.include_router(auth.router)
    router.include_router(chat.router)
    return router
