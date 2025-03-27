from mg_api.infra.db.repo import Repo
from mg_api.infra.db import models as m


class Message(Repo[m.Message]):
    pass
