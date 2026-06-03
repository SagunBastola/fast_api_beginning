import asyncio
from asyncio import taskgroups
from pdb import run
from unittest import result
async def fetch_data(delay,id):
    print(f"fetching....: {id}")
    await asyncio.sleep(delay)
    print("data fetched")
    return {"xyz":"abc"}
async def main():
    print("start:")
    task1=fetch_data(2,1)
    task2=fetch_data(2,2)
    result1=await task1
    print(f"the data obtained task1 {result1}")
    result2=await task2
    print(f"the data obtained task2 {result2}")

asyncio.run(main())