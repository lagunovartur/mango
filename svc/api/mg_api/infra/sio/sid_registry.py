from collections import defaultdict
from typing import Iterator, Tuple
from uuid import UUID
from attrs import define, field


@define
class SidRegistry:
    _user_sid: dict = field(factory=lambda: defaultdict(set), init=False)

    def __setattr__(self, key: UUID, value: str) -> None:
        self._user_sid[key].add(value)

    def __getattr__(self, key: str) -> str:
        return self._user_sid[key]

    def __iter__(self) -> Iterator[Tuple[UUID, set[str]]]:
        return iter(self._user_sid.items())
