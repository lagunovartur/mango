from attrs import define

from mg_api.infra.sio.di import AsyncServer
from mg_api.infra.sio.sid_registry import SidRegistry


@define
class ReadMessagesIA:
    _sio: AsyncServer
    _sid_registry: SidRegistry
