from . import http
from .classes.anime import Anime
from .classes.manga import Manga
import asyncio
httpClient = http.HttpClient()



    
        
class KitsuClient:
    BASE = "https://kitsu.io/api/edge"
    def __init__(self):
        return None

    
    async def search_anime(self, query : str):
        endpoint = self.BASE + "/anime?filter[text]={}".format(query)
        payload = await httpClient.request(endpoint)
        data = payload.get("data")
        for x in data:
            obj = Anime(x)
            yield obj

    async def search_manga(self, query : str):
        endpoint = self.BASE + "/manga?filter[text]={}".format(query)
        payload = await httpClient.request(endpoint)
        data = payload.get("data")
        for x in data:
            obj = Manga(x)
            yield obj
            

    
    async def close(self, msg : str = None):
        await httpClient._close(msg = msg)
        


        

