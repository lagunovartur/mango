from dishka import Provider, Scope, provide_all

from mg_api.svc.user.service import UserList


class UserProv(Provider):
    scope = Scope.REQUEST
    pd = provide_all(UserList)
