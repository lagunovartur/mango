from mg_api.utils.pydantic.base_model import BaseModel


class Login(BaseModel):
    username: str
    password: str
