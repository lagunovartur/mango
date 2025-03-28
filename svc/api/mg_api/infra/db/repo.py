from typing import Any, Generic, Sequence, Tuple, Type, TypeVar, overload

import sqlalchemy as sa
from attrs import define
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm.interfaces import ORMOption
from mg_api.errors.http import ExcNotFound

Model = TypeVar("Model", bound=DeclarativeBase)
PK = Any | Tuple[Any, ...]


@define
class Repo(Generic[Model]):
    _db_sess: AsyncSession

    @property
    def model(self) -> Type[Model]:
        return self.__orig_bases__[0].__args__[0]  # type: ignore[attr-defined]

    # CREATE
    async def add(self, **kw) -> Model:
        obj = self.model(**kw)
        self._db_sess.add(obj)
        return obj

    async def get_or_create(
        self, *, defaults: dict[str, Any] | None = None, **filters
    ) -> Tuple[Model, bool]:
        defaults = defaults or {}
        obj = await self.one_or_none(**filters)
        if obj:
            return obj, False
        obj = self.model(**filters, **defaults)
        self._db_sess.add(obj)
        return obj, True

    # READ
    async def get(
        self,
        pk: PK,
        opts: Sequence[ORMOption] | None = None,
    ) -> Model:
        obj = await self.get_or_none(pk, opts)
        if not obj:
            raise ExcNotFound(extra={"key": "pk", "value": str(pk)})
        return obj

    async def get_or_none(
        self,
        pk: PK,
        opts: Sequence[ORMOption] | None = None,
    ) -> Model | None:
        opts = opts or []
        return await self._db_sess.get(self.model, pk, options=opts)

    async def one(self, opts: Sequence[ORMOption] | None = None, **filters) -> Model:
        obj = await self.one_or_none(opts, **filters)
        if not obj:
            key = ", ".join(str(key) for key in filters.keys())
            value = ", ".join(str(key) for key in filters.values())
            raise ExcNotFound(extra={"key": key, "value": value})
        return obj

    async def one_or_none(
        self, opts: Sequence[ORMOption] | None = None, **filters
    ) -> Model | None:
        opts = opts or []
        stmt = sa.select(self.model).options(*opts)
        stmt = stmt.filter_by(**filters)
        return await self._db_sess.scalar(stmt)

    async def count(self, **filters) -> int:
        stmt = sa.select(sa.func.count()).select_from(self.model).filter_by(**filters)
        result = await self._db_sess.scalar(stmt)
        return result or 0

    async def filter(
        self, opts: Sequence[ORMOption] | None = None, *filters
    ) -> Sequence[Model]:
        opts = opts or []
        stmt = sa.select(self.model).options(*opts)
        if filters:
            stmt = stmt.filter(*filters)
        return (await self._db_sess.scalars(stmt)).all()

    async def filter_by(
        self, opts: Sequence[ORMOption] | None = None, **filters
    ) -> Sequence[Model]:
        opts = opts or []
        stmt = sa.select(self.model).options(*opts)
        if filters:
            stmt = stmt.filter_by(**filters)
        return (await self._db_sess.scalars(stmt)).all()

    async def all(self, opts: Sequence[ORMOption] | None = None) -> Sequence[Model]:
        return await self.filter_by(opts=opts)

    # UPDATE

    @overload
    async def update(self, pk: PK, **kw) -> Model: ...

    @overload
    async def update(self, pk: Model, **kw) -> Model: ...

    async def update(self, pk: Model | PK, **kw) -> Model:
        obj = pk if isinstance(pk, self.model) else await self.get(pk)

        for key, value in kw.items():
            setattr(obj, key, value)

        self._db_sess.add(obj)

        return obj

    # DELETE

    @overload
    async def delete(self, pk: PK) -> None: ...

    @overload
    async def delete(self, pk: Model) -> None: ...

    async def delete(self, pk: Model | PK) -> None:
        if isinstance(pk, self.model):
            await self._db_sess.delete(pk)
        else:
            stmt = sa.delete(self.model).filter_by(id=pk)
            await self._db_sess.execute(stmt)
