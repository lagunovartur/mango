from attrs import define
from sqlalchemy.ext.asyncio import AsyncSession

import mg_api.dto as d
import mg_api.infra.db.models as m
import mg_api.repo as r
from mg_api.dto.message import MessageLP
from mg_api.infra.sio.di import AccessTokenWS
from mg_api.utils.crud.crud_svc import CrudSvc
from mg_api.utils.crud.list_svc import ListSvc
from mg_api.utils.crud.types_ import C, U


@define
class MessageList(ListSvc[d.Message, m.Message, MessageLP]):
    _db_sess: AsyncSession


@define
class MessageSvc(CrudSvc[d.NewMessage, d.Message, None, r.Message]):
    _token: AccessTokenWS
    _db_sess: AsyncSession
    _repo: r.Message

    async def _before_flush(self, obj, dto: C | U, cur_obj=None) -> None:
        obj.sender_id = self._token.payload.sub
