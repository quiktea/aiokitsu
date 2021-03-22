from aiokitsu import KitsuClient
from aiokitsu.utils import log_as_client
import asyncio
kitsu = KitsuClient()



async def main():

    async for manga in kitsu.search_manga("dr stone"):
        print(manga.synopsis)
        print("\n\n\n\n")
    
    await asyncio.sleep(3)



    await kitsu.close()
        


asyncio.get_event_loop().run_until_complete(main())


