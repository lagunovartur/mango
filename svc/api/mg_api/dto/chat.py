import mg_api.infra.db.models as m
from mg_api.utils.pydantic.base_model import BaseModel
from mg_api.utils.pydantic.validators import UUID
from pydantic import Field

class BaseChat(BaseModel):
    _model = m.Chat
    name: str = Field(examples=['чат 1'])


class ChatBase(BaseChat):
    id: UUID


class NewChat(BaseChat):
    id: UUID | None = Field(examples=['27a1f785-dab0-4a9d-828b-9e0762224119'])


class Chat(ChatBase):
    pass


class EditChat(BaseChat):
    id: UUID
    name: str | None = None
