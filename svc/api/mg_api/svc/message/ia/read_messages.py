from attrs import define

from mg_api.dto.message import ReadFilter


@define
class ReadMessagesIA:

    async def __call__(self, dto: ReadFilter) -> None:
        pass




