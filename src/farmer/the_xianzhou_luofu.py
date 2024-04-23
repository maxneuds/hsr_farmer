from logger import logger, logger_set_path
from worlds import the_xianzhou_luofu
from sys import exit

class The_Xianzhou_Luofu:
    
    def __init__(self, bot):
        self.central_starskiff_haven = the_xianzhou_luofu.Central_Starskiff_Haven(bot)
        self.cloudford = the_xianzhou_luofu.Cloudford(bot)
        self.stargazer_navalia = the_xianzhou_luofu.Stargazer_Navalia(bot)
        self.divination_commission = the_xianzhou_luofu.Divination_Commission(bot)
        self.artisanship_commission = the_xianzhou_luofu.Artisanship_Commission(bot)
        self.fyxestroll_garden = the_xianzhou_luofu.Fyxestroll_Garden(bot)

    async def farm_starskiff_haven(self):
        await self.central_starskiff_haven.teleport()
        await self.central_starskiff_haven.shop_salesby()

    async def farm_cloudford(self):
        await self.cloudford.teleport()
        await self.cloudford.path_1()
        await self.cloudford.path_2()
        await self.cloudford.path_3()
        await self.cloudford.path_4()
        await self.cloudford.path_5()
        await self.cloudford.path_6()
        await self.cloudford.path_7()
    
    async def farm_stargazer_navalia(self):
        await self.stargazer_navalia.teleport()
        await self.stargazer_navalia.path_1()
        await self.stargazer_navalia.path_2()
        await self.stargazer_navalia.path_3()
        await self.stargazer_navalia.path_4()
        await self.stargazer_navalia.path_5()
        await self.stargazer_navalia.path_6()
    
    async def farm_divination_commission(self):
        await self.divination_commission.teleport()
        await self.divination_commission.path_1()
        await self.divination_commission.path_2()
        await self.divination_commission.path_3()
        await self.divination_commission.path_4()
        await self.divination_commission.path_5()
        await self.divination_commission.path_6()
        await self.divination_commission.path_7()
    
    async def farm_artisanship_commission(self):
        # await self.artisanship_commission.teleport()
        await self.artisanship_commission.path_x()

    async def farm_fyxestroll_garden(self):
        await self.fyxestroll_garden.teleport()
        await self.fyxestroll_garden.path_1()
        await self.fyxestroll_garden.path_2()
        await self.fyxestroll_garden.path_3()
        await self.fyxestroll_garden.path_4()
        await self.fyxestroll_garden.path_5()
        await self.fyxestroll_garden.path_6()
        await self.fyxestroll_garden.path_7()
