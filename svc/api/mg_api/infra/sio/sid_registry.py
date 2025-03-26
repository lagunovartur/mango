from collections import defaultdict
from typing import Iterator, Tuple, overload
from uuid import UUID
from attrs import define, field


@define
class SidRegistry:

    _user_sid: dict[UUID, set[str]] = field(factory=lambda: defaultdict(set), init=False)
    _sid_user: dict[str, UUID] = field(factory=dict, init=False)

    def __setattr__(self, user_id: UUID, sid: str) -> None:
        self._user_sid[user_id].add(sid)
        self._sid_user[sid] = user_id

    def __getattr__(self, user_id: UUID) -> set[str]:
        return self._user_sid[user_id]

    def __iter__(self) -> Iterator[Tuple[UUID, set[str]]]:
        return iter(self._user_sid.items())

    @overload
    def remove(self, sid: str) -> None: ...

    @overload
    def remove(self, user_id: UUID) -> None: ...

    def remove(self, value: str | UUID) -> None:
        if isinstance(value, str):
            user_id = self._sid_user.pop(value, None)
            if user_id is not None:
                self._user_sid[user_id].discard(value)
                if not self._user_sid[user_id]:
                    self._user_sid.pop(user_id, None)
        else:
            sids = self._user_sid.pop(value, set())
            for sid in sids:
                self._sid_user.pop(sid, None)

    def get(self, sid: str) -> UUID | None:
        return self._sid_user.get(sid, None)