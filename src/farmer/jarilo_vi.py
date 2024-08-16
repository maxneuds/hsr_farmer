from worlds import jarilo_vi
from sys import exit

class Jarilo_VI:
    
    def __init__(self, device):
        self.outlying_snow_plains = jarilo_vi.Outlying_Snow_Plains(device)
        self.backwater_pass = jarilo_vi.Backwater_Pass(device)
        self.silvermane_guard = jarilo_vi.Silvermane_Guard(device)
        self.corridor = jarilo_vi.Corridor(device)
        self.everwinter_hill = jarilo_vi.Everwinter_Hill(device)
        self.great_mine = jarilo_vi.Great_Mine(device)
        self.rivet_town = jarilo_vi.Rivet_Town(device)
        self.robot_settlement = jarilo_vi.Robot_Settlement(device)

    async def farm_outlying_snow_plains(self):
        await self.outlying_snow_plains.teleport()
        await self.outlying_snow_plains.path_1()
        await self.outlying_snow_plains.path_2()
        await self.outlying_snow_plains.path_3()
    
    async def farm_backwater_pass(self):
        await self.backwater_pass.teleport()
        await self.backwater_pass.path_1()
        await self.backwater_pass.path_2()
        await self.backwater_pass.path_3()
        await self.backwater_pass.path_4()
    
    async def farm_silvermane_guard(self):
        await self.silvermane_guard.teleport()
    
    async def farm_corridor(self):
        await self.corridor.teleport()
        await self.corridor.path_1()
        await self.corridor.path_2()
        await self.corridor.path_3()
        await self.corridor.path_4()
        await self.corridor.path_5()
        await self.corridor.path_6()
        await self.corridor.path_7()
        await self.corridor.path_8()

    async def farm_everwinter_hill(self):
        await self.everwinter_hill.teleport()
        await self.everwinter_hill.path_1()
        await self.everwinter_hill.path_2()
    
    async def farm_great_mine(self):
        await self.great_mine.teleport()
        await self.great_mine.path_1()
        await self.great_mine.path_2() # TODO: path1+2 might be combined
        await self.great_mine.path_3()
        await self.great_mine.path_4()
        await self.great_mine.path_5()
        await self.great_mine.path_6()
        # TODO: get items along the bridge path
    
    async def farm_rivet_town(self):
        await self.rivet_town.teleport()
        await self.rivet_town.path_1()
        await self.rivet_town.path_2()
        await self.rivet_town.path_3()
        await self.rivet_town.path_4()

    async def farm_robot_settlement(self):
        await self.robot_settlement.teleport()
        await self.robot_settlement.path_1()
        await self.robot_settlement.path_2()
        await self.robot_settlement.path_3()
        await self.robot_settlement.path_4()


    
    