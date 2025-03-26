from typing import List

import mg_api.infra.db.models as m
from mg_api.utils.pydantic.base_model import BaseModel
from mg_api.utils.pydantic.validators import UUID

from .user import UserBase

class BaseChat(BaseModel):
    _model = m.Chat
    name: str

class ChatBase(BaseChat):
    id: UUID


class NewChat(BaseChat):
    pass


class Chat(ChatBase):
    users: List[UserBase] = []

class EditChat(BaseChat):
    id: UUID
    name: str | None = None
