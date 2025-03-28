from abc import abstractmethod, ABC
from typing import Any, Generic

from mg_api.utils.crud.types_ import C, R, U, RP


class ICrudSvc(ABC, Generic[C, R, U, RP]):
    @abstractmethod
    async def create(
            self,
            dto: C,
    ) -> R:
        pass

    @abstractmethod
    async def update(
            self,
            dto: U,
    ) -> R:
        pass

    @abstractmethod
    async def get(
            self,
            pk
    ) -> R:
        pass

    @abstractmethod
    async def delete(self, pk) -> None:
        pass

    @abstractmethod
    async def _before_flush(self, obj, dto, is_new: bool) -> None:
        pass

    @abstractmethod
    async def _before_commit(self, obj, dto, is_new: bool) -> None:
        pass
