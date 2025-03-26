from dishka import Provider, Scope, provide_all

from mg_api.svc.chat.service import ChatSvc, ChatList


class ChatProv(Provider):

    scope = Scope.REQUEST
    pd = provide_all(ChatSvc, ChatList)

