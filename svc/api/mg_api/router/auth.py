from dishka import FromDishka as Depends
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

import mg_api.dto as d
from mg_api.svc.auth.ia.login import LoginIA
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



@router.post(
    "/login",
)
async def login(
    dto: d.Login,
    ia: Depends[LoginIA],
):
    return await ia(dto)