import pydantic_socketio as socketio

from mg_api.infra.sio.di import AsyncServer

sio = AsyncServer(
    async_mode="asgi",
    cors_allowed_origins=[],
)

sio_app = socketio.ASGIApp(
    socketio_server=sio,
    socketio_path="ws",
)
