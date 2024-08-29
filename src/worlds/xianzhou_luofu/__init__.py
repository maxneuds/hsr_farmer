from logger import logger
from .central_starskiff_haven import Central_Starskiff_Haven
from .cloudford import Cloudford
from .stargazer_navalia import Stargazer_Navalia
from .divination_commission import Divination_Commission
from .artisanship_commission import Artisanship_Commission
from .fyxestroll_garden import Fyxestroll_Garden
from .alchemy_commission import Alchemy_Commission
from .scalegorge_waterscape import Scalegorge_Waterscape
from .the_shackling_prison import The_Shackling_Prison
from worlds.extra import Extra
from ..herta_space_station import Base_Zone
from ..herta_space_station import Storage_Zone
from ..herta_space_station import Supply_Zone


class Farmer:
    def __init__(self, device, mode='credits'):
        self.mode = mode
        self.central_starskiff_haven = Central_Starskiff_Haven(device)
        self.cloudford = Cloudford(device)
        self.stargazer_navalia = Stargazer_Navalia(device)
        self.divination_commission = Divination_Commission(device)
        self.artisanship_commission = Artisanship_Commission(device)
        self.fyxestroll_garden = Fyxestroll_Garden(device)
        self.alchemy_commission = Alchemy_Commission(device)
        self.scalegorge_waterscape = Scalegorge_Waterscape(device)
        self.the_shackling_prison = The_Shackling_Prison(device)
        self.extra = Extra(device)
        self.base_zone = Base_Zone(device)
        self.storage_zone = Storage_Zone(device)
        self.supply_zone = Supply_Zone(device)
    async def stockup(self):
        if self.mode == 'credits':
            logger.info(f'Mode: {self.mode}. Nothing to buy.')
        else:
            await self.central_starskiff_haven.teleport()
            await self.central_starskiff_haven.shop_salesby()
    async def farm(self):
        '''
        Status  7/8 (new: shackling prison) /n
        TP      5 -> ???                    /n
        R2/R4   1 / 0                       /n
        XP      42596/???                   /n
        Time    ???
        '''
        await self.fyxestroll_garden.farm()         # TP:-4->1 XP:4644/4644 Time:???
        await self.base_zone.restore_tp(tp=4.1)     # TP:+4->5 Time:???
        await self.artisanship_commission.farm()    # TP:-4->1 XP:9548/9548 Time:???
        await self.base_zone.restore_tp(tp=4.2)     # TP:+4->5 Time:???
        await self.scalegorge_waterscape.farm()     # TP:-4->1 XP:4752/4752 Time:???
        await self.storage_zone.restore_tp(tp=4)    # TP:+4->5 Time:???
        await self.divination_commission.farm()     # TP:-6->1 XP:6000/6000 Time:??? R2:1
        await self.supply_zone.restore_tp(tp=4)     # TP:+4->5 Time:???
        await self.alchemy_commission.farm()        # TP:-3->2 XP:6912/6912 Time:???
        await self.cloudford.farm()                 # TP:+1->3 XP:4644/4644 Time:???
        await self.stargazer_navalia.farm()         # TP:-1->2 XP:6264/6264 Time:???
        await self.extra.restore_tp(tp=4)         # TP:+4->5 Time:???
    async def dev(self):
        await self.the_shackling_prison.farm()        # TP:???->??? Time:???
        raise SystemExit()


