from mg_api.core.provider import CoreProv
from mg_api.infra.db.provider import DbProv
from mg_api.utils.ioc_builder import IocBuilder


def ioc_builder() -> IocBuilder:
    providers = [
        DbProv(),
        CoreProv(),
    ]

    builder = IocBuilder(*providers)

    return builder
