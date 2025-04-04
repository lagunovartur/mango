import asyncio

from fastapi import FastAPI
from uvicorn import Server
from dishka.integrations.fastapi import setup_dishka

from mg_api.core.ioc import ioc_builder


async def run_servers():
    ioc = ioc_builder()()

    app = await ioc.get(FastAPI)
    setup_dishka(ioc, app)

    api_server = await ioc.get(Server)

    await asyncio.gather(
        api_server.serve(),
    )


if __name__ == "__main__":
    asyncio.run(run_servers())
