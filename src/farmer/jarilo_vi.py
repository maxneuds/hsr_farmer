from worlds import jarilo_vi
from sys import exit

class Jarilo_VI:
    
    def __init__(self, bot):
        self.outlying_snow_plains = jarilo_vi.Outlying_Snow_Plains(bot)
        self.backwater_pass = jarilo_vi.Backwater_Pass(bot)
        self.silvermane_guard = jarilo_vi.Silvermane_Guard(bot)

    async def farm_outlying_snow_plains(self):
        await self.outlying_snow_plains.teleport()
        await self.outlying_snow_plains.path_1()
        await self.outlying_snow_plains.path_2()
    
    async def farm_backwater_pass(self):
        # await self.backwater_pass.teleport()
        # await self.backwater_pass.path_1()
        # await self.backwater_pass.path_2()
        await self.backwater_pass.path_99()
    
    async def farm_silvermane_guard(self):
        # await self.backwater_pass.teleport()
        # await self.backwater_pass.path_1()
        await self.backwater_pass.path_99()
    
    async def farm_rivet_town(self):
        pass
        # await x.teleport()
        # await x.path_1()
        # await x.path_99()

    # async def farm_robot_settlement(self):

    # async def farm_great_mine(self):

    # async def farm_everwinter_hill(self):

    # async def farm_corridor(self): 
    
    