from attrs import define
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from mg_api.infra.db.models import user_chat


@define
class LinkUserIA:
    _db_sess: AsyncSession

    async def __call__(
        self, chat_id: UUID, user_id: UUID, with_commit=True
    ) -> None:

        stmt = (
            insert(user_chat)
            .values(user_id=user_id, chat_id=chat_id)
            .on_conflict_do_nothing()
        )
        await self._db_sess.execute(stmt)
        if with_commit:
            await self._db_sess.commit()