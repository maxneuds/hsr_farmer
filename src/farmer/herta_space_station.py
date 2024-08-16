from worlds import herta_space_station
from sys import exit


class Herta_Space_Station:
    
    def __init__(self, device):
        self.base_zone = herta_space_station.Base_Zone(device)
        self.storage_zone = herta_space_station.Storage_Zone(device)
        self.supply_zone = herta_space_station.Supply_Zone(device)
        self.seclusion_zone = herta_space_station.Seclusion_Zone(device)

    async def farm_base_zone(self):
        await self.base_zone.teleport()
        await self.base_zone.path_1()
    
    async def farm_storage_zone(self):
        await self.storage_zone.teleport()
        await self.storage_zone.path_1()
        await self.storage_zone.path_2()
        await self.storage_zone.path_3()
        await self.storage_zone.path_4()
        await self.storage_zone.path_5()
    
    async def farm_supply_zone(self):
        await self.supply_zone.teleport()
        await self.supply_zone.path_1()
        await self.supply_zone.path_2()
        await self.supply_zone.path_3()
    
    async def farm_seclusion_zone(self):
        await self.seclusion_zone.teleport()
        await self.seclusion_zone.path_1()
        await self.seclusion_zone.path_2()

