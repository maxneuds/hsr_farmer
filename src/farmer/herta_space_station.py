from worlds import herta_space_station
from sys import exit


class Herta_Space_Station:
    
    def __init__(self, bot):
        self.base_zone = herta_space_station.Base_Zone(bot)
        self.storage_zone = herta_space_station.Storage_Zone(bot)
        self.supply_zone = herta_space_station.Supply_Zone(bot)
        self.seclusion_zone = herta_space_station.Seclusion_Zone(bot)

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
        await self.storage_zone.path_6()
        await self.storage_zone.path_7()
        await self.storage_zone.path_8()
    
    async def farm_supply_zone(self):
        await self.supply_zone.teleport()
        await self.supply_zone.path_1()
        await self.supply_zone.path_2()
        await self.supply_zone.path_3()
        await self.supply_zone.path_4()
        await self.supply_zone.path_5()
        await self.supply_zone.path_6()
        await self.supply_zone.path_7()
    
    async def farm_seclusion_zone(self):
        await self.seclusion_zone.teleport()
        await self.seclusion_zone.path_1()
        await self.seclusion_zone.path_2()
        await self.seclusion_zone.path_3()
        await self.seclusion_zone.path_4()

