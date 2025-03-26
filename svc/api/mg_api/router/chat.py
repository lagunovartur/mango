from dishka import FromDishka as Depends
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

import mg_api.dto as d
from mg_api.svc.chat.service import ChatSvc
from mg_api.utils.crud.types_ import ListSlice
from uuid import UUID

router = APIRouter(route_class=DishkaRoute, prefix="/chat", tags=["chat"])


@router.post(
    "/",
    response_model=d.Chat
)
async def create(
    dto: d.NewChat,
    svc: Depends[ChatSvc],
):
    return await svc.create(dto)


@router.put(
    "/",
    response_model=d.Chat,
)
async def update(
    dto: d.EditChat,
    svc: Depends[ChatSvc],
):
    pass
    # return await ia(dto)


@router.get(
    "/{chat_id}",
    response_model=d.Chat,
)
async def get(
    chat_id: UUID,
    svc: Depends[ChatSvc],
):
    pass

@router.get(
    "/",
    response_model=ListSlice[d.Chat],
)
async def list(
    svc: Depends[ChatSvc],
):
    pass

@router.delete(
    "/{chat_id}",
)
async def delete(
    svc: Depends[ChatSvc],
):
    pass


