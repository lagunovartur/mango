from attrs import define

import mg_api.dto as d
import mg_api.repo as r
import mg_api.infra.db.models as m
from mg_api.svc.auth.errors import ExcInvalidCreds

from mg_api.svc.auth.pwd_crypt import IPwdCrypt
from mg_api.svc.jwt.abstract import IJwtSvc, IJwtSetter
from mg_api.utils.pydantic.validators.phone import is_phone


@define
class LoginIA:
    _crypt: IPwdCrypt
    _user: r.User
    _jwt: IJwtSvc
    _jwt_setter: IJwtSetter

    async def __call__(self, dto: d.Login) -> None:
        user = await self._authenticate(dto=dto)
        token_pair = self._jwt.token_pair(user.id)
        self._jwt_setter.set(token_pair)

    async def _authenticate(self, dto: d.Login) -> m.User:
        if is_phone(dto.username):
            user = await self._user.one(phone=dto.username)
        else:
            user = await self._user.one(email=dto.username)

        if not user:
            raise ExcInvalidCreds()

        if not self._crypt.verify(dto.password, user.password):
            raise ExcInvalidCreds()

        return user
