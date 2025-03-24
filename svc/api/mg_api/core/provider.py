from dishka import AsyncContainer, Provider, Scope, from_context, provide
from fastapi import Request
from mg_api.core.config import ApiConfig


class CoreProv(Provider):

    request = from_context(provides=Request, scope=Scope.REQUEST)

    @provide(scope=Scope.APP)
    def config(self) -> ApiConfig:
        return ApiConfig()



