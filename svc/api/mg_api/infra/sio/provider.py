from dishka import Provider, provide, Scope
from socketio import ASGIApp

from mg_api.infra.sio import sio_app
from mg_api.infra.sio.app import sio
from mg_api.infra.sio.di import AsyncServer
from mg_api.infra.sio.sid_registry import SidRegistry


class SioProv(Provider):

    @provide(scope=Scope.APP)
    def server(self) -> AsyncServer:
        return sio

    @provide(scope=Scope.APP)
    def app(self) -> ASGIApp:
        return sio_app

    sid_registry = provide(SidRegistry, scope=Scope.APP)
