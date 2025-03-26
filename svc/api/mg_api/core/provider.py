from dishka import Provider, Scope, from_context, provide
from fastapi import Request, Response

from mg_api.core.config import ApiConfig


class CoreProv(Provider):
    request = from_context(provides=Request, scope=Scope.REQUEST)

    @provide(scope=Scope.APP)
    def config(self) -> ApiConfig:
        return ApiConfig()

    @provide(scope=Scope.REQUEST)
    def response(self, request: Request) -> Response:
        return getattr(request.state, "response")
