from collections import defaultdict
from typing import Iterator, Tuple

from attrs import define, field


@define
class SidRegistry:
    _user_sid: dict = field(factory=lambda: defaultdict(list), init=False)

    def __setattr__(self, key: str, value: str) -> None:
        self._user_sid[key].append(value)

    def __getattr__(self, key: str) -> str:
        return self._user_sid[key]

    def __iter__(self) -> Iterator[Tuple[str, list[str]]]:
        return iter(self._user_sid.items())
