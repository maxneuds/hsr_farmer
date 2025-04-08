from worlds.extra import Extra
from worlds.jarilo_vi import Silvermane_Guard
from worlds.xianzhou_luofu.central_starskiff_haven import Central_Starskiff_Haven
from worlds.xianzhou_luofu.cloudford import Cloudford
from worlds.xianzhou_luofu.stargazer_navalia import Stargazer_Navalia
from worlds.xianzhou_luofu.divination_commission import Divination_Commission
from worlds.xianzhou_luofu.artisanship_commission import Artisanship_Commission
from worlds.xianzhou_luofu.fyxestroll_garden import Fyxestroll_Garden
from worlds.xianzhou_luofu.alchemy_commission import Alchemy_Commission
from worlds.xianzhou_luofu.scalegorge_waterscape import Scalegorge_Waterscape
from worlds.xianzhou_luofu.the_shackling_prison import The_Shackling_Prison
from worlds.xianzhou_luofu.skysplitter import Skysplitter


class Xianzhou_Luofu:
    def __init__(self, device, mode='credits'):
        self.mode = mode
        self.extra = Extra(device)
        self.silvermane_guard = Silvermane_Guard(device)
        self.central_starskiff_haven = Central_Starskiff_Haven(device)
        self.cloudford = Cloudford(device)
        self.stargazer_navalia = Stargazer_Navalia(device)
        self.divination_commission = Divination_Commission(device)
        self.artisanship_commission = Artisanship_Commission(device)
        self.fyxestroll_garden = Fyxestroll_Garden(device)
        self.alchemy_commission = Alchemy_Commission(device)
        self.scalegorge_waterscape = Scalegorge_Waterscape(device)
        self.the_shackling_prison = The_Shackling_Prison(device)
        self.skysplitter = Skysplitter(device)
    async def stockup(self):
        await self.central_starskiff_haven.stockup()
    async def farm(self):
        '''
        Status  9/9                         /n
        TP      5 -> ???                    /n
        R2/R4   0 / 0                       /n
        XP      42596/???                   /n
        Time    ???
        '''
        await self.fyxestroll_garden.farm()                             # TP:-4->1 XP:4644/4644 Time:???
        await self.silvermane_guard.restore_tp(tp=4.1)                  # TP:+4->5 Time:85
        await self.artisanship_commission.farm()                        # TP:-4->1 XP:9548/9548 Time:???
        await self.silvermane_guard.restore_tp(tp=4.2)                  # TP:+4->5 Time:???
        await self.scalegorge_waterscape.farm()                         # TP:-4->1 XP:4752/4752 Time:???
        await self.skysplitter.restore_tp(tp=4.1)                       # TP:+4->5 Time:???
        await self.divination_commission.farm()                         # TP:-6->1 XP:6000/6000 Time:???
        await self.skysplitter.restore_tp(tp=4.2)                       # TP:+4->5 Time:???
        await self.alchemy_commission.farm()                            # TP:-3->2 XP:6912/6912 Time:???
        await self.stargazer_navalia.farm()                             # TP:-1->1 XP:6264/6264 Time:???
        await self.cloudford.farm()                                     # TP:+1->2 XP:4644/4644 Time:???
        await self.extra.restore_tp(tp=2, info='Xianzhou Luofu 1')      # TP:+2->4 Time:???
        await self.the_shackling_prison.farm()                          # TP:??->?? Time:???
        await self.extra.restore_tp(tp=4, info='End of Xianzhou Luofu') # TP:+4->5 Time:???
    async def dev(self):
        await self.fyxestroll_garden.farm()                             # TP:-4->1 XP:4644/4644 Time:???
        await self.silvermane_guard.restore_tp(tp=4.1)                  # TP:+4->5 Time:85
        await self.artisanship_commission.farm()                        # TP:-4->1 XP:9548/9548 Time:???
        await self.silvermane_guard.restore_tp(tp=4.2)                  # TP:+4->5 Time:???
        await self.scalegorge_waterscape.farm()                         # TP:-4->1 XP:4752/4752 Time:???
        await self.skysplitter.restore_tp(tp=4.1)                       # TP:+4->5 Time:???
        await self.divination_commission.farm()                         # TP:-6->1 XP:6000/6000 Time:???
        await self.skysplitter.restore_tp(tp=4.2)                       # TP:+4->5 Time:???
        await self.alchemy_commission.farm()                            # TP:-3->2 XP:6912/6912 Time:???
        await self.stargazer_navalia.farm()                             # TP:-1->1 XP:6264/6264 Time:???
        await self.cloudford.farm()                                     # TP:+1->2 XP:4644/4644 Time:???
        await self.extra.restore_tp(tp=2, info='Xianzhou Luofu 1')      # TP:+2->4 Time:???
        await self.the_shackling_prison.farm()                          # TP:??->?? Time:???
        await self.extra.restore_tp(tp=4, info='End of Xianzhou Luofu') # TP:+4->5 Time:???


