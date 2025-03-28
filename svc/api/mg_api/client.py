import asyncio
from asyncio import sleep
import socketio

sio_client = socketio.AsyncClient(ssl_verify=False)


@sio_client.event
async def connect():
    print("I'm connected")


@sio_client.event
async def disconnect():
    print("I'm disconnected")


async def main():
    await sio_client.connect(url="https://localhost:8000", socketio_path="ws")
    await sleep(1)
    await sio_client.emit(event="msg", data={"text": "hello"})
    await sleep(3)
    await sio_client.disconnect()


asyncio.run(main())
