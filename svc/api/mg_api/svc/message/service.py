import mg_api.dto as d
import mg_api.repo as r
import mg_api.infra.db.models as m
from mg_api.dto.message import MessageLP
from mg_api.utils.crud.crud_svc import CrudSvc
from mg_api.utils.crud.list_svc import ListSvc


class MessageList(ListSvc[d.Message, m.Message, MessageLP]):
    pass


class MessageSvc(CrudSvc[d.NewMessage, d.Message, None, r.Message, MessageList]):
    pass
