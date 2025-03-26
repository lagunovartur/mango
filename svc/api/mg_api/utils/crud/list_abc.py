from typing import Generic, TypeVar
from sqlalchemy.sql.selectable import Select
from attrs import define

from mg_api.utils.crud.types_ import R, M, LP, ListSlice

S = TypeVar('S', bound=Select)

@define
class IListSvc(Generic[R, M, LP]):

    async def __call__(self, params: LP) -> ListSlice[R]:
        pass

    async def _apply_order(self, stmt: S, params: LP) -> S:
        pass

    async def _apply_filters(self, stmt: S, params: LP) -> S:
        pass

    async def _apply_search(self, stmt: S, search: str, fields) -> S:
        pass

