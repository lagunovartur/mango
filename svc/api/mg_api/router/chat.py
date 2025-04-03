from mg_api.svc.chat.ia.link_user import LinkUserIA
from mg_api.svc.chat.service import ChatSvc, ChatList
from mg_api.svc.crud.router import crud_router, add_list_route
from dishka import FromDishka as Depends
from uuid import UUID

router = crud_router(ChatSvc)
add_list_route(router, ChatList)

@router.post(
    path="/{chat_id}/user/{user_id}",
    response_model=None
)
async def link_user(
    chat_id: UUID,
    user_id: UUID,
    ia: Depends[LinkUserIA],
):
    return await ia(chat_id=chat_id, user_id=user_id)
