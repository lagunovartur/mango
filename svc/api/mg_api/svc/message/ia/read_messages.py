from attrs import define

import mg_api.repo as r
from mg_api.dto.message import ReadFilter
from asyncio.taskgroups import TaskGroup

from mg_api.infra.sio.send_event import ISendWsEvent


@define
class ReadMessagesIA:
    _user_repo: r.User
    _sender: ISendWsEvent

    async def __call__(self, dto: ReadFilter) -> None:
        users = await self._user_repo.get_by_chat(dto.chat_id)

        async with TaskGroup() as tg:
            tasks = [
                tg.create_task(self._sender(user.id, 'srv_read_messages', dto.model_dump()))
                for user in users
            ]

