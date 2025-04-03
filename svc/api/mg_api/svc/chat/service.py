from attrs import define
import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession

from mg_api.svc.jwt.schemas import AccessToken
from mg_api.svc.crud.crud_svc import CrudSvc
import mg_api.dto as d
import mg_api.repo as r
import mg_api.infra.db.models as m
from mg_api.svc.crud.list_svc import ListSvc
from mg_api.svc.crud.types_ import BaseLP, C, U


@define
class ChatList(ListSvc[d.Chat, m.Chat, BaseLP]):
    _access_token: AccessToken
    _db_sess: AsyncSession

    async def _set_stmt(self) -> None:
        self._stmt = (
            sa.select(self._M)
            .select_from(m.user_chat)
            .where(m.user_chat.c.user_id == self._access_token.payload.sub)
            .join(m.Chat)
        )

@define
class ChatSvc(CrudSvc[d.NewChat, d.Chat, d.EditChat, r.Chat]):
    _db_sess: AsyncSession
    _repo: r.Chat
    _cur_user: m.CurrentUser

    async def _before_flush(self, obj: m.Chat, dto: C | U, cur_obj=None) -> None:

        if not cur_obj:
            obj.users.append(self._cur_user)



