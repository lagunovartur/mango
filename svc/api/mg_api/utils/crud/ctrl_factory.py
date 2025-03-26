from typing import Type

from dishka import FromDishka as Depends
from dishka.integrations.litestar import inject
from litestar import Controller, get, post
from litestar.di import Provide

from app.utils.kts_resp import ListSlice

# mypy: ignore-errors


def ctrl_factory(
    SVC: Type[CrudSvc],
):
    C, R, U, RP, LS = SVC.__orig_bases__[0].__args__
    LP = LS.__orig_bases__[0].__args__[2]

    class CrudController(Controller):
        @post("create")
        @inject
        async def create(
            self,
            data: C,
            svc: Depends[SVC],
        ) -> R:
            return await svc.create(data)

        @post("edit")
        @inject
        async def update(
            self,
            data: U,
            svc: Depends[SVC],
        ) -> R:
            return await svc.update(data)

        @get(path="{id:int}")
        @inject
        async def get_by_id(
            self,
            id: int,
            svc: Depends[SVC],
        ) -> R:
            return await svc.get_by_id(id)

        @get(
            "list",
            dependencies={"params": Provide(LP, sync_to_thread=False)},
        )
        @inject
        async def get_list(
            self,
            params: LP,
            svc: Depends[SVC],
        ) -> ListSlice[R]:
            return await svc.get_list(params)

    return CrudController
