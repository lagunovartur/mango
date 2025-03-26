from fastapi import Request
from dishka import Provider, from_context, Scope, provide_all, provide
from passlib.context import CryptContext

from mg_api.svc.auth.ia.register import RegisterIA
from mg_api.svc.auth.pwd_crypt import PwdCrypt, IPwdCrypt


class AuthProv(Provider):
    scope = Scope.REQUEST

    @provide(scope=Scope.APP)
    def crypt_context(self) -> CryptContext:
        return CryptContext(schemes=["bcrypt"], deprecated="auto")

    pwd_crypt = provide(PwdCrypt, scope=Scope.APP, provides=IPwdCrypt)

    request = from_context(provides=Request, scope=Scope.REQUEST)

    pd = provide_all(
        RegisterIA
    )

