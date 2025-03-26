from attrs import define
from sqlalchemy.ext.asyncio import AsyncSession
import mg_api.repo as r
import mg_api.infra.db.models as m
import mg_api.dto as d
from mg_api.svc.auth.pwd_crypt import IPwdCrypt


@define
class RegisterIA:
    _user: r.User
    _db_sess: AsyncSession
    _crypt: IPwdCrypt

    async def __call__(self, dto: d.NewUser) -> m.User:
        user = await self._user.add(**dto.model_dump())
        user.password = self._crypt.hash(user.password)
        await self._db_sess.commit()
        return user
