from fastapi import Request
from dishka import Provider, from_context, Scope, provide_all

from mg_api.svc.auth.ia.register import RegisterIA


class AuthProv(Provider):
    scope = Scope.REQUEST

    request = from_context(provides=Request, scope=Scope.REQUEST)

    pd = provide_all(
        RegisterIA
    )

