import mg_api.infra.db.models as m
from mg_api.utils.pydantic.base_model import BaseModel
from mg_api.utils.pydantic.validators import UUID
from .user import UserBase
from .chat import ChatBase

class BaseMessage(BaseModel):
    _model = m.Message
    text: str


class MessageBase(BaseMessage):
    id: UUID


class Message(MessageBase):
    sender: UserBase
    chat: ChatBase

