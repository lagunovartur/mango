import asyncio
import uvicorn

from mg_api.core.api import api_factory
from mg_api.core.config import ApiConfig
from mg_api.core.ioc import ioc_builder


async def make_api_server(ioc):
    app = await api_factory(ioc)

    config = await ioc.get(ApiConfig)

    uv_config = uvicorn.Config(
        app=app,
        host="0.0.0.0",
        port=config.PORT,
        ssl_keyfile="./ssl/private.key",
        ssl_certfile="./ssl/public.crt",
    )

    server = uvicorn.Server(uv_config)

    return server


async def run_servers():
    ioc = ioc_builder()()
    api_server = await make_api_server(ioc)

    await asyncio.gather(
        api_server.serve(),
    )


if __name__ == "__main__":
    asyncio.run(run_servers())
