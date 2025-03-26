import sqlalchemy as sa
from .base import Base


user_chat = sa.Table(
    "user_chat",
    Base.metadata,
    sa.Column(
        "user_id", sa.ForeignKey("user.id"), primary_key=True
    ),
    sa.Column("chat_id", sa.ForeignKey("chat.id"), primary_key=True),
)