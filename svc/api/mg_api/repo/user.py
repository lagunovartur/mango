from mg_api.infra.db.repo import Repo
from mg_api.infra.db import models as m

class User(Repo[m.User]):
    pass