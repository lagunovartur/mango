from asyncio.taskgroups import TaskGroup

import sqlalchemy.orm as orm
from attrs import define

from mg_api import repo as r
from mg_api.dto.message import NewMessage
from mg_api.infra.sio.send_event import ISendWsEvent
from mg_api.svc.message.service import MessageSvc


@define
class SendMessageIA:
    _crud: MessageSvc
    _chat_repo: r.Chat
    _sender: ISendWsEvent

    async def __call__(self, dto: NewMessage) -> None:
        message = await self._crud.create(dto)
        chat = await self._chat_repo.get(
            dto.chat_id, (orm.selectinload(self._chat_repo.model.users),)
        )

        async with TaskGroup() as tg:
            tasks = [
                tg.create_task(self._sender(user.id, 'srv_new_message', message.model_dump())) for user in chat.users
            ]

