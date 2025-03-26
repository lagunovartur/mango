from abc import abstractmethod
from typing import Generic, TypeVar

import sqlalchemy as sa
from attrs import define
from sqlalchemy import desc
from sqlalchemy.ext.asyncio import AsyncSession

from mg_api.utils.crud.list_abc import IListSvc
from mg_api.utils.crud.query_utils import QueryUtils
from mg_api.utils.crud.types_ import R, M, LP, ListSlice, BaseLP


@define
class ListSvc(IListSvc, Generic[R, M, LP]):
    _db_sess: AsyncSession

    def __attrs_post_init__(self):
        self._R, self._M, self._LP = self.__orig_bases__[0].__args__

    async def __call__(self, params: LP) -> ListSlice[R]:
        stmt = sa.select(self._M).options(*(await self._load_opts()))

        if params.search:
            stmt = await self._apply_search(stmt, params.search)

        stmt = await self._apply_filters(stmt, params)
        stmt = await self._apply_order(stmt, params)

        return await QueryUtils.list_slice(self._db_sess, stmt, params, self._R)

    async def _apply_order(self, stmt, params: BaseLP):
        if attr := getattr(self._M, "created_at", None):
            stmt = stmt.order_by(desc(attr))
        return stmt

    async def _apply_filters(self, stmt, params: BaseLP):
        filters = QueryUtils.parse_filters(self._M, params.model_dump(mode='python'))
        return stmt.filter(*filters)

    async def _apply_search(self, stmt, search):
        return stmt

    async def _load_opts(self):
        return self._R.load_opts()()


LS = TypeVar("LS", bound=ListSvc)
