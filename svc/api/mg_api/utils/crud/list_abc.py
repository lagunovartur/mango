from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Any
from sqlalchemy.sql.selectable import Select
from attrs import define, field

from mg_api.utils.crud.types_ import R, M, LP, ListSlice, BaseLP

S = TypeVar('S', bound=Select)

@define
class IListSvc(ABC,Generic[R, M, LP]):

    _params: BaseLP = field(init=False)


    @abstractmethod
    async def __call__(self, params: LP) -> ListSlice[R]:
        pass

    @abstractmethod
    async def _apply_order(self, stmt: S) -> S:
        pass

    @abstractmethod
    async def _apply_filters(self, stmt: S) -> S:
        pass

    @abstractmethod
    async def _apply_search(self, stmt: S) -> S:
        pass

    @abstractmethod
    async def _load_opts(self):
        pass


