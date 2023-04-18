import asyncio
import time

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    tasks = []
    start = time.time()
    for i in range(2):
        tasks.append(asyncio.create_task(func1()))
        tasks.append(asyncio.create_task(func2()))
    response = await asyncio.gather(*tasks)
    end = time.time()
    return {"response": response, "time_taken": (end - start)}


async def func1():
    await asyncio.sleep(2)
    return "Func1() Completed"


async def func2():
    await asyncio.sleep(1)
    return "Func2() Completed"
