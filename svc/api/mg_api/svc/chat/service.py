from mg_api.utils.crud.crud_svc import CrudSvc
import mg_api.dto as d
import mg_api.repo as r
import mg_api.infra.db.models as m
from mg_api.utils.crud.list_svc import ListSvc
from mg_api.utils.crud.types_ import BaseLP


class ChatList(ListSvc[d.Chat, m.Chat, BaseLP]):
    pass

class ChatSvc(CrudSvc[d.NewChat, d.Chat, d.EditChat, r.Chat, ChatList]):
    pass