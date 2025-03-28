from typing import AsyncIterator

from dishka import Provider, provide, Scope, from_context
from socketio import ASGIApp

from mg_api.infra.sio.app import sio, sio_app
from mg_api.infra.sio.connect_ws import ConnectWS, IConnectWS, WSConnectManager
from mg_api.infra.sio.di import AsyncServer, CurSid, AccessTokenWS
from mg_api.infra.sio.sid_registry import SidRegistry


class SioProv(Provider):
    cur_sid = from_context(provides=CurSid, scope=Scope.SESSION)

    @provide(scope=Scope.APP)
    def server(self) -> AsyncServer:
        return sio

    @provide(scope=Scope.APP)
    def app(self) -> ASGIApp:
        return sio_app

    sid_registry = provide(SidRegistry, scope=Scope.APP)

    @provide(scope=Scope.SESSION)
    async def access_token(self, sid: CurSid, sio: AsyncServer) -> AccessTokenWS:
        sess_data = await sio.get_session(sid)
        return sess_data["access_token"]

    connect_ws = provide(ConnectWS, scope=Scope.SESSION)

    @provide(scope=Scope.SESSION, provides=IConnectWS)
    async def ws_connect_manager(
        self, conn: ConnectWS
    ) -> AsyncIterator[WSConnectManager]:
        async with conn as conn:
            yield conn
