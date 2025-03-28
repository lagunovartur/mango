from mg_api.core.provider import CoreProv
from mg_api.infra.db.provider import DbProv
from mg_api.infra.sio.provider import SioProv
from mg_api.repo.provider import RepoProv
from mg_api.svc.auth.provider import AuthProv
from mg_api.svc.chat.provider import ChatProv
from mg_api.svc.jwt.provider import JwtProv
from mg_api.svc.message.provider import MessageProv
from mg_api.svc.user.provider import UserProv
from mg_api.utils.ioc_builder import IocBuilder


def ioc_builder() -> IocBuilder:
    providers = [
        DbProv(),
        CoreProv(),
        SioProv(),
        RepoProv(),
        AuthProv(),
        JwtProv(),
        ChatProv(),
        MessageProv(),
        UserProv(),
    ]

    builder = IocBuilder(*providers)

    return builder
