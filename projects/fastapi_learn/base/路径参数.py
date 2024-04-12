from fastapi import FastAPI
import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


# 顺序很重要¶
# 有时，路径操作中的路径是写死的。
# 比如要使用 /users/me 获取当前用户的数据。
# 然后还要使用 /users/{user_id}，通过用户 ID 获取指定用户的数据。
# 由于路径操作是按顺序依次运行的，
# 因此，一定要在 /users/{user_id} 之前声明 /users/me ：


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


if __name__ == "__main__":
    # system(f"hypercorn {__file__.rstrip('.py')}:app --reload")
    asyncio.run(serve(app, Config()))
