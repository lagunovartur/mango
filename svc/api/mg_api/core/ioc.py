from mg_api.core.provider import CoreProv
from mg_api.infra.db.provider import DbProv
from mg_api.infra.sio.provider import SioProv
from mg_api.repo.provider import RepoProv
from mg_api.utils.ioc_builder import IocBuilder


def ioc_builder() -> IocBuilder:
    providers = [
        DbProv(),
        CoreProv(),
        SioProv(),
        RepoProv(),
    ]

    builder = IocBuilder(*providers)

    return builder
