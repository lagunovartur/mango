from dishka import AsyncContainer
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from mg_api.core.config import ApiConfig
from mg_api.errors.handlers import add_exc_handlers
from mg_api.infra.sio import sio_app
from mg_api.router import router_factory
from mg_api.svc.auth.guard import AuthGuard


async def api_factory(container: AsyncContainer) -> FastAPI:
    config = await container.get(ApiConfig)
    auth_guard = await container.get(AuthGuard)

    app = FastAPI(
        title=config.TITLE,
        debug=config.DEBUG,
        openapi_url="/api/openapi.json",
        # lifespan=lifespan,
        dependencies=[
            Depends(auth_guard),
        ],
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origin_regex=r"https://localhost:\d+",
        allow_headers=["*"],
        allow_methods=["*"],
        allow_credentials=True,
        expose_headers=["Set-Cookie"],
    )

    add_exc_handlers(app)

    app.mount("/ws", app=sio_app)
    app.state.sio = sio_app.engineio_server

    setup_dishka(container, app)

    app.include_router(router_factory())

    return app
