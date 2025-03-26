from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

router = APIRouter(route_class=DishkaRoute, prefix="/auth", tags=["auth"])


@router.post(path="/login")
async def login():
    pass
