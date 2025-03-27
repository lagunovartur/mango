from asyncio.taskgroups import TaskGroup

import sqlalchemy.orm as orm
from attrs import define

from mg_api import repo as r
from mg_api.dto.message import NewMessage, Message
from mg_api.infra.sio.di import AsyncServer
from mg_api.infra.sio.sid_registry import SidRegistry
from mg_api.svc.message.service import MessageSvc


@define
class SendMessageIA:

    _sio: AsyncServer
    _crud: MessageSvc
    _sid_registry: SidRegistry
    _chat_repo: r.Chat

    async def __call__(self, dto: NewMessage) -> None:
        message = await self._crud.create(dto)
        chat = await self._chat_repo.get(dto.chat_id, (orm.selectinload(self._chat_repo.model.users),))

        sids = (
            sid
            for user in chat.users
            if (user_sids := self._sid_registry[user.id])
            for sid in user_sids
        )

        async with TaskGroup() as tg:
            tasks = [
                tg.create_task(self._send_message(sid, message)) for sid in sids
            ]

    async def _send_message(self, sid: str, message: Message) -> None:
        try:
            await self._sio.emit('srv_new_message', message.model_dump(), to=sid)
            print(f"Message sent to {sid}")
        except Exception as e:
            print(f"Failed to send message to {sid}: {e}")