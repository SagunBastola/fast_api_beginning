import asyncio
from asyncio import taskgroups
from pdb import run
from unittest import result
async def fetch_data(delay):
    print("fetching....")
    await asyncio.sleep(delay)
    print("data fetched")
    return {"xyz":"abc"}
async def main():
    print("start:")
    task=fetch_data(2)
    print("after the task")
    result=await task
    print(f"the data obtained {result}")

asyncio.run(main())