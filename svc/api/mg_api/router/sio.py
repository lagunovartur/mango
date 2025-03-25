from dishka import AsyncContainer, Scope, FromDishka
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from mg_api.core.sio.app import sio
from mg_api.core.sio.di import inject


class MSG(BaseModel):
    text: str


@sio.event
async def connect(sid, environ, auth):
    sess_data = await sio.get_session(sid)
    app_cntr: AsyncContainer = environ['asgi.scope']['app'].state.dishka_container
    sess_data['dishka_container'] = await app_cntr(context={'sid': sid}, scope=Scope.SESSION).__aenter__()
    print(f"Connected {sid}")


@sio.event
@inject
async def msg(sid, data: MSG, db_sess: FromDishka[AsyncSession]):
    print(f"Received msg {sid} {data} {db_sess}")


@sio.event
async def disconnect(sid):
    sess_cntr: AsyncContainer = (await sio.get_session(sid))['dishka_container']
    await sess_cntr.close()
    print(f"Disconnected {sid}")
