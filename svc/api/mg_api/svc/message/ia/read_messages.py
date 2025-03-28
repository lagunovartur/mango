from attrs import define
import mg_api.repo as r
from mg_api.dto.message import ReadFilter


@define
class ReadMessagesIA:

    _msg_repo: r.Message

    async def __call__(self, dto: ReadFilter) -> None:
        pass







