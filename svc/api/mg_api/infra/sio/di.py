from contextvars import ContextVar
from typing import NewType

import pydantic_socketio as socketio
from dishka import AsyncContainer, Scope
from dishka.integrations.base import wrap_injection

from mg_api.svc.jwt.schemas import AccessToken

REQ_CNTR: ContextVar[AsyncContainer] = ContextVar("REQ_CNTR")


class AsyncServer(socketio.AsyncServer):
    async def _trigger_event(self, event, namespace, *args):
        sess_data = await self.get_session(args[0])
        await self._di_open_sess(event, sess_data, args)

        sess_cntr = sess_data.get("dishka_container")
        async with sess_cntr(scope=Scope.REQUEST) as req_cntr:
            REQ_CNTR.set(req_cntr)
            print(event)
            res = await super()._trigger_event(event, namespace, *args)

        await self._di_close_sess(event, sess_data)

        return res

    async def _di_open_sess(self, event, sess_data, args) -> None:
        if not event == "connect":
            return
        sess_cntr = sess_data.get("dishka_container", None)
        if sess_cntr is not None:
            return

        sid, environ = args[0], args[1]
        app_cntr = environ["asgi.scope"]["app"].state.dishka_container
        sess_data["dishka_container"] = await app_cntr(
            context={CurSid: sid}, scope=Scope.SESSION
        ).__aenter__()

    async def _di_close_sess(self, event, sess_data) -> None:
        if not event == "disconnect":
            return
        sess_cntr: AsyncContainer = sess_data["dishka_container"]
        await sess_cntr.close()


def inject(func):
    return wrap_injection(
        func=func, container_getter=lambda p, _: REQ_CNTR.get(), is_async=True
    )


CurSid = NewType("CurSid", str)
AccessTokenWS = NewType("AccessTokenWS", AccessToken)
