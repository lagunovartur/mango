from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter
from mg_api.router import auth

def router_factory():
    router = APIRouter(route_class=DishkaRoute, prefix="/api")
    router.include_router(auth.router, tags=["auth"])

    # router.include_router(auth.router, tags=["auth"])
    # router.include_router(auth_sess.router, tags=["auth_sessions"])

    return router

