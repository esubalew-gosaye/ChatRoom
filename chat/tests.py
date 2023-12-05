import asyncio
import json
import websockets

async def on_message(websocket, message):
    data = json.loads(message)
    # Handle your data processing here
    print(data)
async def send_message(websocket, message):
    await websocket.send(json.dumps(message))

async def connect_websocket():
    uri = f"ws://localhost:8000/ws/chat/django/2/"  # Replace with your WebSocket server URI

    async with websockets.connect(uri) as websocket:
        # print(f"Connected to {uri}")
        # send_f = True
        # while True:
        #     message = await websocket.recv()
        #     await on_message(websocket, message)
        #     if send_f:
        #         await send_message(websocket, {"message": message+"sumalo"})
        #         send_f=False
        await send_message(websocket, {"message": "sumalo"})
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(connect_websocket())

