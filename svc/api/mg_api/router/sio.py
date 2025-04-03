from dishka import FromDishka as Depends

from mg_api.dto.message import NewMessage, ReadFilter
from mg_api.infra.sio.app import sio
from mg_api.infra.sio.connect_ws import IConnectWS
from mg_api.infra.sio.di import inject
from mg_api.svc.message.ia.read_messages import ReadMessagesIA
from mg_api.svc.message.ia.send_message import SendMessageIA


@sio.event
@inject
async def connect(sid, environ, connector: Depends[IConnectWS]):
    return await connector(environ["HTTP_COOKIE"], sid)


@sio.event
@inject
async def cl_new_message(sid, data: NewMessage, ia: Depends[SendMessageIA]):
    await ia(data)


@sio.event
@inject
async def cl_read_messages(sid, data: ReadFilter, ia: Depends[ReadMessagesIA]):
    await ia(data)

