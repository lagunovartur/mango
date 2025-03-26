from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins.serial_pk import SerialPk
from .mixins.timestamp import Timestamp


class User(Base, SerialPk, Timestamp):
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str | None] = mapped_column(String(50), nullable=True)
    password: Mapped[str] = mapped_column(String(60), nullable=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)


class CurrentUser(User):
    __abstract__ = True
