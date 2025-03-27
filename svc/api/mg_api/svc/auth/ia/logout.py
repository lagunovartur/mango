from attrs import define

from mg_api.svc.jwt.abstract import IJwtSetter


@define
class LogoutIA:
    _jwt_setter: IJwtSetter

    async def __call__(self) -> None:
        self._jwt_setter.unset()

