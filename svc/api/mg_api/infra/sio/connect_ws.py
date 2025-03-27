from attrs import define
from abc import ABC, abstractmethod
from mg_api.infra.sio.di import AsyncServer
from mg_api.infra.sio.sid_registry import SidRegistry
from mg_api.svc.jwt.abstract import IJwtSvc
from mg_api.svc.jwt.schemas import AccessToken


class IConnectWS:

    @abstractmethod
    async def __call__(self, cookie: str, sid: str) -> bool:
        pass


@define
class ConnectWS(IConnectWS):

    _sid_registry: SidRegistry
    _sio: AsyncServer
    _jwt_svc: IJwtSvc

    async def __call__(self, cookie: str, sid: str) -> bool:
        cookie = self._parse_cookie(cookie)

        access_token: str = cookie.get(AccessToken.COOKIE_KEY, None)
        if not access_token:
            return False

        try:
            access_token: AccessToken = self._jwt_svc.decode(access_token)
        except Exception as e:
            return False

        sess_data = await self._sio.get_session(sid)
        sess_data['access_token'] = access_token
        self._sid_registry[access_token.payload.sub] = sid

        return True

    @staticmethod
    def _parse_cookie(cookie: str) -> dict[str, str]:
        return dict(map(lambda item: item.split('='), cookie.split(';')))





