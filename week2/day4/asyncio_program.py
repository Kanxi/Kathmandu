import requests
import asyncio
import aiohttp
from timer import timer 
from concurrent.futures import ProcessPoolExecutor

URL = "https://httpbin.org/uuid"

async def fetch_uuid(session, url):
    async with session.get(url) as response:
        json_data= await response.json()
        print(response.json()['uuid'])

# @timer(1, 1)
async def main():
    async with aiohttp.ClientSession() as session:
        tasks=[fetch_uuid(session,URL) for _ in range(100)]
        await asyncio.gather(*tasks)
if __name__=="__main__":
    main()