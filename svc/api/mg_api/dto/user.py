import mg_api.infra.db.models as m
import mg_api.utils.pydantic.validators as v
from mg_api.utils.pydantic.base_model import BaseModel


class BaseUser(BaseModel):
    _model = m.User

    first_name: str
    last_name: str | None = None
    email: v.Email
    phone: v.Phone


class UserBase(BaseUser):
    id: int


class NewUser(BaseUser):
    password: str


class User(UserBase):
    pass
