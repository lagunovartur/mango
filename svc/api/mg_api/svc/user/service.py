from attrs import define
from sqlalchemy.ext.asyncio import AsyncSession

import mg_api.dto as d
import mg_api.infra.db.models as m
from mg_api.svc.crud.list_svc import ListSvc
from mg_api.svc.crud.types_ import BaseLP
from sqlalchemy import or_


@define
class UserList(ListSvc[d.User, m.User, BaseLP]):
    _db_sess: AsyncSession

    async def _apply_search(self, search: str) -> None:
        if search.isdigit():
            self._stmt = self._stmt.filter(self._M.phone.ilike(f"%{search}%"))

        elif search.isalnum():
            self._stmt = self._stmt.filter(
                or_(
                    self._M.first_name.ilike(f"%{search}%"),
                    self._M.last_name.ilike(f"%{search}%"),
                    self._M.email.ilike(f"%{search}%"),
                )
            )

        else:
            self._stmt = self._stmt.filter(self._M.email.ilike(f"%{search}%"))
