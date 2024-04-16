from worlds import jarilo_vi
from sys import exit

class Jarilo_VI:
    
    def __init__(self, bot):
        self.outlying_snow_plains = jarilo_vi.Outlying_Snow_Plains(bot)
        self.backwater_pass = jarilo_vi.Backwater_Pass(bot)
        self.silvermane_guard = jarilo_vi.Silvermane_Guard(bot)
        self.corridor = jarilo_vi.Corridor(bot)
        self.everwinter_hill = jarilo_vi.Everwinter_Hill(bot)
        self.great_mine = jarilo_vi.Great_Mine(bot)
        self.rivet_town = jarilo_vi.Rivet_Town(bot)
        self.silvermane_guard = jarilo_vi.Silvermane_Guard(bot)

    async def farm_outlying_snow_plains(self):
        await self.outlying_snow_plains.teleport()
        await self.outlying_snow_plains.path_1()
        await self.outlying_snow_plains.path_2()
    
    async def farm_backwater_pass(self):
        await self.backwater_pass.teleport()
        await self.backwater_pass.path_1()
        await self.backwater_pass.path_2()
        exit() # check for kill all
        await self.backwater_pass.path_3()
        await self.backwater_pass.path_4()
    
    async def farm_silvermane_guard(self):
        await self.silvermane_guard.teleport()
    
    async def farm_corridor(self):
        await self.corridor.teleport()
        exit() # check all
        await self.corridor.path_1()
        await self.corridor.path_2()
        await self.corridor.path_3()
        await self.corridor.path_4()
        await self.corridor.path_5()
        await self.corridor.path_6()
        await self.corridor.path_7()

    async def farm_everwinter_hill(self):
        exit() # check tele
        await self.everwinter_hill.teleport()
        exit() # check kill all
        await self.everwinter_hill.path_1()
    
    async def farm_great_mine(self):
        # await self.great_mine.teleport()
        # await self.corridor.path_1()
        # await self.corridor.path_2()
        # exit() # check kill / path
        # await self.corridor.path_3()
        await self.great_mine.path_x()
    
    async def farm_rivet_town(self):
        pass
        # await self.rivet_town.teleport()
        # await self.rivet_town.path_1()
        # await self.rivet_town.path_99()

    async def farm_robot_settlement(self):
        pass


    
    