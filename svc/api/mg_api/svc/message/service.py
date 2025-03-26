import mg_api.dto as d
import mg_api.infra.db.models as m
from mg_api.dto.message import MessageLP
from mg_api.utils.crud.list_svc import ListSvc


class MessageList(ListSvc[d.Message, m.Message, MessageLP]):
    pass
