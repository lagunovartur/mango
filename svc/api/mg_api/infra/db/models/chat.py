from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship, Mapped

from .base import Base
from .mixins import UuidPk
from .mixins.timestamp import Timestamp
from .user_chat import user_chat

if TYPE_CHECKING:
    from .user import User
    from .message import Message


class Chat(Base, UuidPk, Timestamp):
    users: Mapped["User"] = relationship("User", secondary=user_chat, back_populates="chats")
    messages: Mapped["Message"] = relationship(
        back_populates="chat", lazy="noload"
    )
