from dishka import Provider, Scope, provide_all

from mg_api.svc.message.ia.send_message import SendMessageIA
from mg_api.svc.message.service import MessageList, MessageSvc


class MessageProv(Provider):
    scope = Scope.REQUEST
    pd = provide_all(MessageList, MessageSvc, SendMessageIA)
