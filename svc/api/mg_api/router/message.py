from typing import Annotated

from dishka import FromDishka as Depends
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter, Query

import mg_api.dto as d
from mg_api.dto.message import MessageLP
from mg_api.svc.message.service import MessageList
from mg_api.utils.crud.types_ import ListSlice

router = APIRouter(route_class=DishkaRoute, prefix="/message", tags=["message"])


@router.get(
    "",
    response_model=ListSlice[d.Message],
)
async def list(
    params: Annotated[MessageLP, Query()],
    svc: Depends[MessageList],
):
    return await svc(params)
