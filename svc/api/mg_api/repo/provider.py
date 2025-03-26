from dishka import Provider, provide_all, Scope

from .user import User


class RepoProv(Provider):
    scope = Scope.REQUEST

    pd = provide_all(User)
