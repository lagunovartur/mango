from mg_api.utils.pydantic.base_model import BaseModel
from mg_api.utils.pydantic.validators import UUID


class IdIn(BaseModel):
    id__in: list[UUID] = []