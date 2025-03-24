from dishka import AsyncContainer
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from mg_api.core.config import ApiConfig
from mg_api.router import router_factory


async def api_factory(container: AsyncContainer) -> FastAPI:
    config = await container.get(ApiConfig)
    # auth_guard = await container.get(AuthGuard)

    app = FastAPI(
        title=config.TITLE,
        debug=config.DEBUG,
        openapi_url="/api/openapi.json",
        # lifespan=lifespan,
        # dependencies=[
        #     Depends(auth_guard),
        # ],
    )
    setup_dishka(container, app)

    app.include_router(router_factory())

    return app

