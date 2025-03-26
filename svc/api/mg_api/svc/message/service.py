import mg_api.dto as d
import mg_api.infra.db.models as m
from mg_api.utils.crud.list_svc import ListSvc
from mg_api.utils.crud.types_ import BaseLP


class MessageList(ListSvc[d.Message, m.Message, BaseLP]):
    pass
