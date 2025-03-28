from asyncio.taskgroups import TaskGroup

from attrs import define

from mg_api import repo as r
from mg_api.dto.message import NewMessage
from mg_api.infra.sio.send_event import ISendWsEvent
from mg_api.svc.message.service import MessageSvc


@define
class SendMessageIA:
    _crud: MessageSvc
    _user_repo: r.User
    _sender: ISendWsEvent

    async def __call__(self, dto: NewMessage) -> None:
        message = await self._crud.create(dto)
        users = await self._user_repo.get_by_chat(message.chat.id)

        async with TaskGroup() as tg:
            tasks = [
                tg.create_task(
                    self._sender(user.id, "srv_new_message", message.model_dump())
                )
                for user in users
            ]
