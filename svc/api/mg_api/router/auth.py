from dishka import FromDishka as Depends
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

import mg_api.dto as d
from mg_api.svc.auth.ia.register import RegisterIA

router = APIRouter(route_class=DishkaRoute, prefix='/auth', tags=["auth"])


@router.post(
    "/register",
    response_model=d.UserBase
)
async def register(
    dto: d.NewUser,
    ia: Depends[RegisterIA],
):
    return await ia(dto)
