import asyncio
import websockets

# Store connected clients
connected = set()


async def handler(websocket, path):
    # When a new client connects, add it to the connected set
    connected.add(websocket)
    print(f"New connection established: {websocket}")

    try:
        # Loop to receive client messages and broadcast to all connected clients
        async for message in websocket:
            print(f"Received message: {message}")
            await asyncio.gather(*[client.send(message) for client in connected])
    finally:
        # When a client disconnects, remove it from the connected set
        connected.remove(websocket)
        print(f"Connection closed: {websocket}")


# Start WebSocket server
start_server = websockets.serve(handler, "localhost", 8765)

print("WebSocket server started.")

# Run event loop
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
