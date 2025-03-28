from mg_api.infra.db import models as m
from mg_api.infra.db.repo import Repo


class Message(Repo[m.Message]):
    pass
