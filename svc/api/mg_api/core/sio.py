import socketio
from dishka import AsyncContainer, Scope
from pydantic import BaseModel


class AsyncServer(socketio.AsyncServer):

    async def _trigger_event(self, event, namespace, *args):
        sid = args[0]
        sess_data = (await self.get_session(sid))
        sess_cntr = sess_data.get('dishka_container', None)
        if sess_cntr is None:
            return await super()._trigger_event(event, namespace, *args)

        async with sess_cntr(scope=Scope.REQUEST) as req_cntr:
            return await super()._trigger_event(event, namespace, *args)


sio = AsyncServer(
    async_mode="asgi",
    cors_allowed_origins=[],
)

sio_app = socketio.ASGIApp(
    socketio_server=sio,
    socketio_path='ws',
)


# def inject(func):
#
#
#     async def cntr_getter(*args, **kwargs):
#         sid = kwargs.get('sid') or args[0]
#         sess_cntr = (await sio.get_session(sid))['dishka_container']
#         async with sess_cntr(scope=Scope.REQUEST) as cntr:
#             yield cntr
#
#     def decorator(func):
#
#
#         @wraps(func)
#         async def wrapper(*args, **kwargs):
#
#             sid = kwargs.get('sid') or args[0]
#             sess_cntr = (await sio.get_session(sid))['dishka_container']
#
#             async with sess_cntr(scope=Scope.REQUEST) as cntr:
#                 req_cntr = cntr
#                 res = await func (*args, **kwargs)
#
#             return res
#
#         return wrapper
#
#     return wrap_injection(func=func, container_getter=cntr_getter, is_async=True)


class MSG(BaseModel):
    text: str


@sio.event
async def connect(sid, environ, auth):
    sess_data = await sio.get_session(sid)
    app_cntr: AsyncContainer = environ['asgi.scope']['app'].state.dishka_container
    sess_data['dishka_container'] = await app_cntr(context={'sid': sid}, scope=Scope.SESSION).__aenter__()
    print(f"Connected {sid}")


@sio.event
async def msg(sid, data):
    print(f"Received msg {sid} {data}")


# @sio.event
# @inject
# async def msg(sid, data, db_sess: FromDishka[AsyncSession]):
#     print(f"Received msg {sid} {data}")

@sio.event
async def disconnect(sid):
    sess_cntr: AsyncContainer = (await sio.get_session(sid))['dishka_container']
    await sess_cntr.close()
    print(f"Disconnected {sid}")
