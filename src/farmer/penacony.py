from worlds import penacony
from sys import exit


class Penacony:

    def __init__(self, bot):
        self.golden_hour = penacony.Golden_Hour(bot)
        self.dreams_edge = penacony.Dreams_Edge(bot)
        self.childs_dream = penacony.Childs_Dream(bot)
        self.the_reverie_dreamscape = penacony.The_Reverie_Dreamscape(bot)
        self.dewlight_pavilion = penacony.Dewlight_Pavilion(bot)
        self.clock_studios_theme_park = penacony.Clock_Studios_Theme_Park(bot)
    
    async def farm_dreams_edge(self):
        await self.dreams_edge.teleport()
        await self.dreams_edge.path_1()
        await self.dreams_edge.path_2()
        await self.dreams_edge.path_3()
        await self.dreams_edge.path_4()
        await self.dreams_edge.path_5()
        await self.dreams_edge.path_6()
        await self.dreams_edge.path_7()
        await self.dreams_edge.path_8()
    
    async def farm_childs_dream(self):
        await self.childs_dream.teleport()
        await self.childs_dream.path_1()
        await self.childs_dream.path_2()
        await self.childs_dream.path_3()
        await self.childs_dream.path_4()
        await self.childs_dream.path_5()
    
    async def farm_the_reverie_dreamscape(self):
        # await self.the_reverie_dreamscape.teleport()
        # await self.the_reverie_dreamscape.path_1()
        # await self.the_reverie_dreamscape.path_2()
        # await self.the_reverie_dreamscape.path_3()
        # await self.the_reverie_dreamscape.path_4()
        # await self.the_reverie_dreamscape.path_5()
        # await self.the_reverie_dreamscape.path_6()
        # await self.the_reverie_dreamscape.path_7()
        # await self.the_reverie_dreamscape.path_8()
        # await self.the_reverie_dreamscape.path_9()
        # await self.the_reverie_dreamscape.path_10()
        # await self.the_reverie_dreamscape.path_11()
        # await self.the_reverie_dreamscape.path_12()
        # await self.the_reverie_dreamscape.path_13()
        # await self.the_reverie_dreamscape.path_14()
        await self.the_reverie_dreamscape.path_15()
        await self.the_reverie_dreamscape.path_16()

    async def farm_dewlight_pavilion(self):
        await self.dewlight_pavilion.teleport()
        await self.dewlight_pavilion.path_1()
        await self.dewlight_pavilion.path_2()
        await self.dewlight_pavilion.path_3()
        await self.dewlight_pavilion.path_4()
        await self.dewlight_pavilion.path_5()
        await self.dewlight_pavilion.path_6()
        await self.dewlight_pavilion.path_7()
        await self.dewlight_pavilion.path_8()
        await self.dewlight_pavilion.path_9()
        await self.dewlight_pavilion.path_10()
        await self.dewlight_pavilion.path_11()
        await self.dewlight_pavilion.path_12()

    async def farm_clock_studios_theme_park(self):
        await self.clock_studios_theme_park.teleport()
        await self.clock_studios_theme_park.path_0()
        await self.clock_studios_theme_park.path_1()
        await self.clock_studios_theme_park.path_2()
        await self.clock_studios_theme_park.path_3()
        await self.clock_studios_theme_park.path_4()
        await self.clock_studios_theme_park.path_5()
        await self.clock_studios_theme_park.path_6()
        await self.clock_studios_theme_park.path_7()
        await self.clock_studios_theme_park.path_8()

