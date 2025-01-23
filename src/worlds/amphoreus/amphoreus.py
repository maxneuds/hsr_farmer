from worlds.extra import Extra
from worlds.amphoreus.okhema import Okhema



class Amphoreus:
    '''
    Status: 0/4
    '''
    def __init__(self, device):
        self.extra = Extra(device)
        self.okhema = Okhema(device)
    async def farm(self):
        # await self.dreams_edge.farm()
        raise SystemExit('farm')
    async def dev(self):
        # await self.dreams_edge.farm()                           # TP:-4->1 XP
        raise SystemExit('dev')


