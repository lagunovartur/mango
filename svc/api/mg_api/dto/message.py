import mg_api.infra.db.models as m
from mg_api.utils.pydantic.base_model import BaseModel
from mg_api.utils.pydantic.validators import UUID
from pydantic import Field
from .user import UserBase
from .chat import ChatBase
from ..svc.crud.types_ import BaseLP


class BaseMessage(BaseModel):
    _model = m.Message
    text: str


class MessageBase(BaseMessage):
    id: UUID
    chat_id: UUID


class NewMessage(BaseMessage):
    chat_id: UUID


class Message(BaseMessage):
    id: UUID
    sender: UserBase
    chat: ChatBase


class ReadFilter(BaseModel):
    chat_id: UUID
    id__in: list[UUID] = []


class MessageLP(BaseLP):
    chat_id__in: list[UUID] = Field(min_length=1)
