from fastapi import Request
from dishka import Provider, from_context, Scope, provide_all, provide
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from typing import cast
from mg_api.svc.auth.guard import AuthGuard
from mg_api.svc.auth.ia.login import LoginIA
from mg_api.svc.auth.ia.logout import LogoutIA
from mg_api.svc.auth.ia.register import RegisterIA
from mg_api.svc.auth.pwd_crypt import PwdCrypt, IPwdCrypt
from mg_api.svc.jwt.schemas import AccessToken
import mg_api.infra.db.models as m


class AuthProv(Provider):
    scope = Scope.REQUEST

    @provide(scope=Scope.APP)
    def crypt_context(self) -> CryptContext:
        return CryptContext(schemes=["bcrypt"], deprecated="auto")

    pwd_crypt = provide(PwdCrypt, scope=Scope.APP, provides=IPwdCrypt)

    request = from_context(provides=Request, scope=Scope.REQUEST)

    @provide(scope=Scope.REQUEST)
    def access_token(self, request: Request) -> AccessToken | None:
        return getattr(request.state, "access_token", None)

    @provide(scope=Scope.REQUEST)
    def access_token(self, request: Request) -> AccessToken:
        return getattr(request.state, "access_token")

    auth_guard = provide(AuthGuard, scope=Scope.APP)

    pd = provide_all(RegisterIA, LoginIA, LogoutIA)


    @provide(scope=Scope.REQUEST)
    async def cur_user(
        self, db_sess: AsyncSession, token: AccessToken
    ) -> m.CurrentUser:
        user_id = token.payload.sub
        with db_sess.no_autoflush:
            user = await db_sess.get(m.User, user_id)
        return cast(m.CurrentUser, user)



