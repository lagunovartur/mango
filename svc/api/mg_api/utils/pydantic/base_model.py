import pydantic as pd

from mg_api.utils.pydantic.load import LoadOptsMixin


class BaseModel(pd.BaseModel, LoadOptsMixin):
    model_config = pd.ConfigDict(from_attributes=True)
