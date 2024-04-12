from fastapi import FastAPI

# from os import system
import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    # system(f"hypercorn {__file__.rstrip('.py')}:app --reload")
    asyncio.run(serve(app, Config()))
