import operator

import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession

from mg_api.utils.crud.types_ import PageParams, ListSlice


class QueryUtils:
    @staticmethod
    def parse_filters(model, filters: dict):

        operators = {
            "gt": operator.gt,
            "lt": operator.lt,
            "eq": operator.eq,
            "ne": operator.ne,
            "ge": operator.ge,
            "le": operator.le,
            "in": lambda field, value: field.in_(value),
            "cn": lambda field, value: field.ilike(f"%{value}%"),
        }

        m_filters = []

        for key, value in filters.items():
            field, sep, op = key.partition("__")
            field = getattr(model, field, None)
            if field is None:
                continue
            op = operators.get(op) or operator.eq
            m_filters.append(op(field, value))

        return m_filters

    @staticmethod
    def apply_search(stmt, search: str, fields):
        search_parts = search.split()

        tsvector = sa.func.to_tsvector(
            "russian",
            sa.func.concat_ws(" ", *fields),
        )

        tsquery = sa.func.to_tsquery(
            "russian", " & ".join(map(lambda part: part + ":*", search_parts))
        )

        rank = sa.func.ts_rank(tsvector, tsquery)

        return stmt.filter(tsvector.op("@@")(tsquery)).order_by(rank.desc())

    @staticmethod
    def count_stmt(stmt):
        return sa.select(sa.func.count()).select_from(stmt.subquery())

    @classmethod
    async def list_slice(
        cls, db_sess: AsyncSession, stmt, page_params: PageParams, dto_type
    ):
        count_stmt = cls.count_stmt(stmt)
        count = (await db_sess.execute(count_stmt)).scalar()

        stmt = stmt.limit(page_params.limit).offset(page_params.offset)

        res = await db_sess.execute(stmt)

        objects = res.scalars().all()

        return ListSlice[dto_type](items=objects, total=count)
