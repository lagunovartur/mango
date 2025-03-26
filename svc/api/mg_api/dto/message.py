import mg_api.infra.db.models as m
from mg_api.utils.pydantic.base_model import BaseModel
from mg_api.utils.pydantic.validators import UUID
from pydantic import Field
from .user import UserBase
from .chat import ChatBase
from ..utils.crud.types_ import BaseLP


class BaseMessage(BaseModel):
    _model = m.Message
    text: str


class MessageBase(BaseMessage):
    id: UUID


class Message(MessageBase):
    sender: UserBase
    chat: ChatBase

class MessageLP(BaseLP):
    chat_id__in: list[UUID] = Field(min_length=1)