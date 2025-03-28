from abc import abstractmethod, ABC
from uuid import UUID
import asyncio
from attrs import define

from mg_api.infra.sio.di import AsyncServer
from mg_api.infra.sio.sid_registry import SidRegistry


class ISendWsEvent(ABC):
    @abstractmethod
    async def __call__(
        self, user_id: UUID, event: str, data: dict
    ) -> dict[str, Exception]:
        pass


@define
class SendWsEvent:
    _sio: AsyncServer
    _sid_registry: SidRegistry

    async def __call__(
        self, user_id: UUID, event: str, data: dict
    ) -> dict[str, Exception]:
        exceptions = {}

        sids = self._sid_registry[user_id]
        tasks = (
            asyncio.create_task(self._sio.emit(event, data, to=sid)) for sid in sids
        )
        results = await asyncio.gather(*tasks, return_exceptions=True)

        for sid, result in zip(sids, results):
            if isinstance(result, Exception):
                exceptions[sid] = result

        return exceptions
