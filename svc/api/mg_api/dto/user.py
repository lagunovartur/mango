import mg_api.infra.db.models as m
import mg_api.utils.pydantic.validators as v
from mg_api.utils.pydantic.base_model import BaseModel
from mg_api.utils.pydantic.validators import UUID
from pydantic import Field


class BaseUser(BaseModel):
    _model = m.User

    first_name: str = Field(examples=["Иван"])
    last_name: str | None = Field(default=None, examples=["Симонов"])
    email: v.Email = Field(examples=["simonov@example.com"])
    phone: v.Phone = Field(examples=["79826234512"])


class UserBase(BaseUser):
    id: UUID


class NewUser(BaseUser):
    password: str = Field(examples=["Qwerty!1"])


class User(UserBase):
    pass
