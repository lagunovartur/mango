import pydantic as pd

from mg_api.utils.pydantic.load import LoadOptsMixin


class BaseModel(pd.BaseModel, LoadOptsMixin):
    pass
