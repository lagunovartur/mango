from abc import ABC, abstractmethod
from typing import TypeVar
from uuid import UUID
from fr_lib.interfaces.jwt.schemas import JwtPair, AccessToken, RefreshToken, JwtToken

T = TypeVar('T', bound=JwtToken)


class IJwtSvc(ABC):

    @abstractmethod
    def token_pair(self, sub: UUID, cid: int, **kwargs) -> JwtPair:
        pass

    @abstractmethod
    def refresh_pair(self, refresh_token: RefreshToken) -> JwtPair:
        pass

    @abstractmethod
    def decode(self, token: str, **options) -> AccessToken | RefreshToken:
        pass


class IJwtSetter:

    @abstractmethod
    def set(self, token_pair: JwtPair) -> None:
        pass

    @abstractmethod
    def unset(self) -> None:
        pass


