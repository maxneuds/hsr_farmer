from logger import logger, logger_set_path
from worlds import the_xianzhou_luofu
from sys import exit

class The_Xianzhou_Luofu:
    
    def __init__(self, bot):
        self.central_starskiff_haven = the_xianzhou_luofu.Central_Starskiff_Haven(bot)
        self.cloudford = the_xianzhou_luofu.Cloudford(bot)
        self.fyxestroll_garden = the_xianzhou_luofu.Fyxestroll_Garden(bot)

    async def farm_starskiff_haven(self):
        await self.central_starskiff_haven.teleport()
        await self.central_starskiff_haven.shop_salesby()

    async def farm_cloudford(self):
        # await self.cloudford.teleport()
        # await self.cloudford.path_1()
        # await self.cloudford.path_2()
        await self.cloudford.path_x()

    async def farm_fyxestroll_garden(self):
        await self.fyxestroll_garden.teleport()
        await self.fyxestroll_garden.path_1()
        await self.fyxestroll_garden.path_2()
        await self.fyxestroll_garden.path_3()
        await self.fyxestroll_garden.path_4()
        await self.fyxestroll_garden.path_5()
        await self.fyxestroll_garden.path_6()
        await self.fyxestroll_garden.path_7()
