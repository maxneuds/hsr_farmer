from worlds.extra import Extra
from worlds.herta_space_station.base_zone import Base_Zone
from worlds.herta_space_station.storage_zone import Storage_Zone
from worlds.herta_space_station.supply_zone import Supply_Zone
from worlds.herta_space_station.seclusion_zone import Seclusion_Zone


class Herta_Space_Station:
    def __init__(self, device):
        self.extra = Extra(device)
        self.base_zone = Base_Zone(device)
        self.storage_zone = Storage_Zone(device)
        self.supply_zone = Supply_Zone(device)
        self.seclusion_zone = Seclusion_Zone(device)
    async def farm(self):
        '''
        Status  4/4         \n
        TP      0 -> 5      \n
        R2/R4   0 / 0       \n
        XP      7128/7128   \n
        Time    ???
        '''
        await self.extra.restore_tp(tp=4)   # TP:+4->5
        await self.base_zone.farm()         # TP:-1->3 XP:432/432 Time:90
        await self.seclusion_zone.farm()    # TP:+2->5 XP:1620/1620 Time:220
        await self.storage_zone.farm()      # TP:+0->5 XP:2592/2592 Time:250
        await self.supply_zone.farm()       # TP:+0->5 XP:2484/2484 Time:281


