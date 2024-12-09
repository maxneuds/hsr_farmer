from worlds.jarilo_vi.outlying_snow_plains import Outlying_Snow_Plains
from worlds.jarilo_vi.backwater_pass import Backwater_Pass
from worlds.jarilo_vi.silvermane_guard import Silvermane_Guard
from worlds.jarilo_vi.corridor import Corridor
from worlds.jarilo_vi.everwinter_hill import Everwinter_Hill
from worlds.jarilo_vi.great_mine import Great_Mine
from worlds.jarilo_vi.rivet_town import Rivet_Town
from worlds.jarilo_vi.robot_settlement import Robot_Settlement


class Jarilo_VI:
    def __init__(self, device):
        self.outlying_snow_plains = Outlying_Snow_Plains(device)
        self.backwater_pass = Backwater_Pass(device)
        self.silvermane_guard = Silvermane_Guard(device)
        self.corridor = Corridor(device)
        self.everwinter_hill = Everwinter_Hill(device)
        self.great_mine = Great_Mine(device)
        self.rivet_town = Rivet_Town(device)
        self.robot_settlement = Robot_Settlement(device)
    async def farm(self):
        '''
        Status  7/7             /n
        TP      5 -> 5          /n
        R2/R4   0 / 0           /n
        XP      19440/19440     /n
        Time    ???
        '''
        await self.outlying_snow_plains.farm()          # TP:-1->4 XP:2052/2052 Time:188
        await self.backwater_pass.farm()                # TP:+0->4 XP:3024/3024 Time:240
        await self.robot_settlement.farm()              # TP:+1->5 XP:2592/2592 Time:237
        await self.corridor.farm()                      # TP:-2->3 XP:3672/3672 Time:432
        await self.everwinter_hill.farm()               # TP:+0->3 XP:1404/1404 Time:119
        await self.robot_settlement.restore_tp(tp=2)    # TP:+2->5 Time:???
        await self.great_mine.farm()                    # TP:-4->1 XP:4536/4536 Time:326
        await self.rivet_town.farm()                    # TP:+5->5 XP:2160/2160 Time:262
    async def dev(self):
        await self.outlying_snow_plains.farm()          # TP:-1->4 XP:2052/2052 Time:188
        await self.backwater_pass.farm()                # TP:+0->4 XP:3024/3024 Time:240
        await self.robot_settlement.farm()              # TP:+1->5 XP:2592/2592 Time:237
        await self.corridor.farm()                      # TP:-2->3 XP:3672/3672 Time:432
        await self.everwinter_hill.farm()               # TP:+0->3 XP:1404/1404 Time:119
        await self.robot_settlement.restore_tp(tp=2)    # TP:+2->5 Time:???
        await self.great_mine.farm()                    # TP:-4->1 XP:4536/4536 Time:326
        await self.rivet_town.farm()                    # TP:+5->5 XP:2160/2160 Time:262
        raise SystemExit('dev')
        

