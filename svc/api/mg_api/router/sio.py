from dishka import FromDishka as Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from mg_api.infra.sio.app import sio
from mg_api.infra.sio.connect_ws import IConnectWS
from mg_api.infra.sio.di import inject
from mg_api.infra.sio.sid_registry import SidRegistry


class MSG(BaseModel):
    text: str


@sio.event
@inject
async def connect(sid, environ, connector: Depends[IConnectWS]):
    return await connector(environ['HTTP_COOKIE'], sid)


@sio.event
@inject
async def msg(sid, data: MSG, db_sess: Depends[AsyncSession]):
    print(f"Received msg {sid} {data} {db_sess}")


@sio.event
@inject
async def disconnect(sid, sid_registry: Depends[SidRegistry]):
    sid_registry.remove(sid)
    print(f"Disconnected {sid}")
