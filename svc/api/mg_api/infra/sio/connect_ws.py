from attrs import define, field
from abc import ABC, abstractmethod
from mg_api.infra.sio.di import AsyncServer
from mg_api.infra.sio.sid_registry import SidRegistry
from mg_api.svc.jwt.abstract import IJwtSvc
from mg_api.svc.jwt.schemas import AccessToken
from typing import NewType, Any


class IConnectWS:

    @abstractmethod
    async def __call__(self, cookie: str, sid: str) -> bool:
        pass

WSConnectManager = NewType("WSConnectManager", Any)

@define
class ConnectWS(IConnectWS):

    _sid_registry: SidRegistry
    _sio: AsyncServer
    _jwt_svc: IJwtSvc
    _sid: str | None = field(init=False, default=None)

    async def __call__(self, cookie: str, sid: str) -> bool:
        if self._sid:
            raise RuntimeError("ConnectWS can only be used once.")

        cookie = self._parse_cookie(cookie)

        access_token: str = cookie.get(AccessToken.COOKIE_KEY, None)
        if not access_token:
            return False

        try:
            access_token: AccessToken = self._jwt_svc.decode(access_token)
        except Exception as e:
            return False

        self._sid = sid

        sess_data = await self._sio.get_session(sid)
        sess_data['access_token'] = access_token
        self._sid_registry[access_token.payload.sub] = sid

        return True

    @staticmethod
    def _parse_cookie(cookie: str) -> dict[str, str]:
        return dict(map(lambda item: item.split('='), cookie.split(';')))

    async def __aenter__(self) -> WSConnectManager:
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if self._sid:
            self._sid_registry.remove(self._sid)


