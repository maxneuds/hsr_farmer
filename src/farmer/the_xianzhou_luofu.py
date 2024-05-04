from logger import log_runtime
from worlds import the_xianzhou_luofu
from sys import exit
from datetime import datetime as dt

class The_Xianzhou_Luofu:
    
    def __init__(self, bot):
        self.central_starskiff_haven = the_xianzhou_luofu.Central_Starskiff_Haven(bot)
        self.cloudford = the_xianzhou_luofu.Cloudford(bot)
        self.stargazer_navalia = the_xianzhou_luofu.Stargazer_Navalia(bot)
        self.divination_commission = the_xianzhou_luofu.Divination_Commission(bot)
        self.artisanship_commission = the_xianzhou_luofu.Artisanship_Commission(bot)
        self.fyxestroll_garden = the_xianzhou_luofu.Fyxestroll_Garden(bot)
        self.alchemy_commission = the_xianzhou_luofu.Alchemy_Commission(bot)
        self.scalegorge_waterscape = the_xianzhou_luofu.Scalegorge_Waterscape(bot)

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
        await self.cloudford.path_8()
        await self.cloudford.path_9()
    
    async def farm_stargazer_navalia(self):
        await self.stargazer_navalia.teleport()
        await self.stargazer_navalia.path_1()
        await self.stargazer_navalia.path_2()
        await self.stargazer_navalia.path_3()
        await self.stargazer_navalia.path_4()
        await self.stargazer_navalia.path_5()
        await self.stargazer_navalia.path_6()
        await self.stargazer_navalia.path_7()
    
    async def farm_divination_commission(self):
        await self.divination_commission.teleport()
        await self.divination_commission.path_1()
        await self.divination_commission.path_2()
        await self.divination_commission.path_3()
        await self.divination_commission.path_4()
        await self.divination_commission.path_5()
        await self.divination_commission.path_6()
        await self.divination_commission.path_7()
        await self.divination_commission.path_8()
        await self.divination_commission.path_9()
    
    async def farm_artisanship_commission(self):
        await self.artisanship_commission.teleport()
        await self.artisanship_commission.path_1()
        await self.artisanship_commission.path_2()
        await self.artisanship_commission.path_3()
        await self.artisanship_commission.path_4()
        await self.artisanship_commission.path_5()
        await self.artisanship_commission.path_6()
        await self.artisanship_commission.path_7()
        await self.artisanship_commission.path_8()

    async def farm_fyxestroll_garden(self):
        await self.fyxestroll_garden.teleport()
        await self.fyxestroll_garden.path_1()
        await self.fyxestroll_garden.path_2()
        await self.fyxestroll_garden.path_3()
        await self.fyxestroll_garden.path_4()
        await self.fyxestroll_garden.path_5()
        await self.fyxestroll_garden.path_6()
        await self.fyxestroll_garden.path_7()
        await self.fyxestroll_garden.path_8()
    
    async def farm_alchemy_commission(self):
        await self.alchemy_commission.teleport()
        await self.alchemy_commission.path_1()
        await self.alchemy_commission.path_2()
        await self.alchemy_commission.path_3()
        await self.alchemy_commission.path_4()
        await self.alchemy_commission.path_5()
        await self.alchemy_commission.path_6()
        await self.alchemy_commission.path_7()
        await self.alchemy_commission.path_8()
        await self.alchemy_commission.path_9()
        await self.alchemy_commission.path_10()
    
    async def farm_scalegorge_waterscape(self):
        await self.scalegorge_waterscape.teleport()
        await self.scalegorge_waterscape.path_1()
        await self.scalegorge_waterscape.path_2()
        await self.scalegorge_waterscape.path_3()
        await self.scalegorge_waterscape.path_4()
        await self.scalegorge_waterscape.path_5()
        await self.scalegorge_waterscape.path_6()
        await self.scalegorge_waterscape.path_7()
        await self.scalegorge_waterscape.path_8()


