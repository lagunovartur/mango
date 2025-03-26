from dishka import Provider, provide_all, Scope

from .user import User
from .chat import Chat


class RepoProv(Provider):
    scope = Scope.REQUEST

    pd = provide_all(User, Chat)
