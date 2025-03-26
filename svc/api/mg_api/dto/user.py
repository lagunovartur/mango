import mg_api.infra.db.models as m
import mg_api.utils.pydantic.validators as v
from mg_api.utils.pydantic.base_model import BaseModel
from mg_api.utils.pydantic.validators import UUID


class BaseUser(BaseModel):
    _model = m.User

    first_name: str
    last_name: str | None = None
    email: v.Email
    phone: v.Phone


class UserBase(BaseUser):
    id: UUID


class NewUser(BaseUser):
    password: str


class User(UserBase):
    pass
