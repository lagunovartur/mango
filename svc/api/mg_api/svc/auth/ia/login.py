from attrs import define

import mg_api.dto as d
import mg_api.repo as r
from mg_api.svc.auth.pwd_crypt import IPwdCrypt


@define
class LoginIA:

    _crypt: IPwdCrypt
    _user: r.User

    async def __call__(self, dto: d.Login) -> None:
        pass
