import aiohttp
import asyncio
from .utils import log_as_client
class HttpClient():
    def __init__(self, *args, **kwargs):
        self.__session = aiohttp.ClientSession(*args, **kwargs)


    async def request(self, path : str):
        async with self.__session.get(path) as response:
            payload = await response.json()
            return payload




    async def _close(self, msg = None):
        await self.__session.close()
        if msg is not None:
           log_as_client(msg, "Closed HTTP Session")
            