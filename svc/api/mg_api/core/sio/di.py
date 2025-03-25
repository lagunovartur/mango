from contextvars import ContextVar

import pydantic_socketio as socketio
from dishka import AsyncContainer, Scope
from dishka.integrations.base import wrap_injection

REQ_CNTR: ContextVar[AsyncContainer] = ContextVar('REQ_CNTR')


class AsyncServer(socketio.AsyncServer):

    async def _trigger_event(self, event, namespace, *args):
        sid = args[0]
        sess_data = (await self.get_session(sid))
        sess_cntr = sess_data.get('dishka_container', None)
        if sess_cntr is None:
            return await super()._trigger_event(event, namespace, *args)

        async with sess_cntr(scope=Scope.REQUEST) as req_cntr:
            REQ_CNTR.set(req_cntr)
            return await super()._trigger_event(event, namespace, *args)


def inject(func):
    return wrap_injection(func=func, container_getter=lambda p,_: REQ_CNTR.get(), is_async=True)
