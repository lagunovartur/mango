from mg_api.svc.chat.service import ChatSvc, ChatList
from mg_api.svc.crud.router import crud_router, add_list_route

router = crud_router(ChatSvc)
add_list_route(router, ChatList)

