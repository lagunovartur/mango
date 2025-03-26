from dataclasses import dataclass
from typing import TypeVar, Optional, Generic, Sequence

from mg_api.infra.db.models import Base
from mg_api.infra.db.repo import Repo
from mg_api.utils.pydantic.base_model import BaseModel


class PageParams(BaseModel):
    offset: int = 0
    limit: int = 10


class BaseLP(PageParams):
    search: Optional[str] = None


C = TypeVar("C", bound=BaseModel)
R = TypeVar("R", bound=BaseModel)
U = TypeVar("U", bound=BaseModel)
M = TypeVar("M", bound=Base)
RP = TypeVar("RP", bound=Repo)
LP = TypeVar("LP", bound=BaseLP)

D = TypeVar("D", bound=BaseModel)
class ListSlice(BaseModel, Generic[D]):
    items: Sequence[D]
    total: int


