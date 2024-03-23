import asyncio
import websockets


async def connect():
    # 连接到 WebSocket 服务器
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        print("Connected to server.")

        # 接收来自服务器的消息并打印
        async for message in websocket:
            print(f"Received message: {message}")


async def send_message():
    while True:
        # 输入消息并发送给服务器
        message = input("Enter your message: ")
        async with websockets.connect("ws://localhost:8765") as websocket:
            await websocket.send(message)
            print(f"Sent message: {message}")


async def main():
    # 启动两个协程，一个用于发送消息，一个用于接收消息
    await asyncio.gather(connect(), send_message())


# 运行客户端主程序
asyncio.run(main())
