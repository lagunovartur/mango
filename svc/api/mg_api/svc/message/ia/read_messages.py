from attrs import define
import mg_api.repo as r
from mg_api.dto.message import ReadFilter
from mg_api.infra.db import models as m

@define
class ReadMessagesIA:

    _msg_repo: r.Message

    async def __call__(self, dto: ReadFilter) -> None:
        pass
        # model: m.Message = self._msg_repo.model
        # await self._msg_repo.filter(model.chat_id == dto.chat_id)









