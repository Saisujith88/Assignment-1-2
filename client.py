import asyncio
import websockets

async def communicate():
    uri = "ws://64.227.128.4:8325"
    async with websockets.connect(uri) as websocket:
        while True:
            message = input("Enter a message to send: ")
            await websocket.send(message)
            response = await websocket.recv()
            print("Received:", response)

asyncio.get_event_loop().run_until_complete(communicate())