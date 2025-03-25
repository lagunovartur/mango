from dishka import FromDishka
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from mg_api.core.sio.app import sio
from mg_api.core.sio.di import inject


class MSG(BaseModel):
    text: str


@sio.event
async def connect(sid, environ, auth):
    print(f"Connected {sid}")


@sio.event
@inject
async def msg(sid, data: MSG, db_sess: FromDishka[AsyncSession]):
    print(f"Received msg {sid} {data} {db_sess}")


@sio.event
async def disconnect(sid):
    print(f"Disconnected {sid}")
