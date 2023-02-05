import asyncio
import websockets

async def subscribe_to_data(uri):
    async with websockets.connect(uri) as websocket:
        # receive data from the stream
        while True:
            data = await websocket.recv()
            print(f"Received data: {data}")

asyncio.get_event_loop().run_until_complete(
    subscribe_to_data("wss://stream.binance.com:9443/ws/BTCUSDT@kline_3m")
)
