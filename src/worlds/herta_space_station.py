import asyncio as aio
from logger import logger
from automation.bot import Bot
from datetime import datetime as dt
from sys import exit

class World:
    def __init__(self, bot):
        self.bot = bot

    
    async def farm_seclusion_zone(self):
        x = self.Seclusion_Zone(bot=self.bot)
        # await x.teleport()
        # await x.path_1()
        # await x.path_2()
        # await x.path_3()
        # await x.path_4()
        # await x.path_5()
        # await x.path_6()
        # await x.path_7()
        # await x.path_8()
        await x.path_99()
    class Seclusion_Zone:
        def __init__(self, bot):
            self.bot = bot
        async def teleport(self):
            logger.info('---')
            logger.info("--- Map: Seclusion Zone")
            logger.info('---')
            await self.bot.switch_map(y_list=863/1080, world='herta_space_station', scroll_down=True,
                                      x=1079/2400, y=376/1080, move_x=0, move_y=1) # Incubator
            await self.bot.movepi(0.0, 2700)
            await self.bot.attack() # +2 TP
        async def path_99(self):
            logger.info('### Path 1 ###')
            await self.bot.use_teleporter(1097/2400, 285/1080, move_x=0, move_y=3, corner='botright') # Breeding Ground
            # await self.bot.attack_technique(4)
            # await self.bot.restore_tp(n=1) # +2 TP

    # async def farm_seclusion_zone(self):
        
        # logger('### group 1 ###')
        # await self.bot.use_teleporter(1098/2400, 241/1080, open_map=False) # Breeding Ground
        # await self.bot.movepi(0.06, 4000)
        # await self.bot.movepi(1.95, 6000)
        # await self.bot.movepi(1.8, 4500)
        # await self.bot.movepi(1.75, 3200)
        # await self.bot.movepi(1.6, 300)
        # await self.bot.attack()
        # await self.bot.wait_for_onmap()
        # logger('### group 2 ###')
        # await self.bot.use_teleporter(1098/2400, 174/1080) # Breeding Ground
        # await self.bot.movepi(0.06, 4000)
        # await self.bot.movepi(1.95, 6000)
        # await self.bot.movepi(1.8, 4500)
        # await self.bot.movepi(1.75, 4500)
        # await self.bot.movepi(1.6, 4500)
        # await self.bot.movepi(1.5, 500)
        # await self.bot.attack()
        # await self.bot.wait_for_onmap()
        # await self.bot.attack() # in case energy missed
        # await self.bot.sleep(0.5)
        # logger('### group 3 ###')
        # await self.bot.use_teleporter(920/2400, 632/1080) # Pharmaceutical Room
        # await self.bot.movepi(0.5, 700)
        # await self.bot.movepi(0.25, 1500)
        # await self.bot.movepi(0.00, 1500)
        # await self.bot.movepi(1.75, 3000)
        # await self.bot.movepi(0.25, 500)
        # await self.bot.movepi(1.8, 2500)
        # await self.bot.movepi(1.3, 2800)
        # await self.bot.movepi(1.75, 3800)
        # await self.bot.movepi(1.6, 2000)
        # await self.bot.movepi(1.75, 2500)
        # await self.bot.movepi(1.48, 7000)
        # await self.bot.attack()
        # await self.bot.wait_for_onmap()
        # logger('### group 3, part 2 ###')
        # await self.bot.movepi(1.45, 1800)
        # await self.bot.attack()
        # await self.bot.wait_for_onmap()

    # async def farm_supply_zone(self):
    #     logger('\nfarm: Supply Zone\n')
    #     await self.bot.switch_map(750/1080)
    #     logger('### group 1 ###')
    #     await self.bot.use_teleporter(720/2400, 375/1080, open_map=False) # Spare Parts Warehouse
    #     await self.bot.movepi(0.5, 6500)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     logger('### group 2 ###')
    #     await self.bot.use_teleporter(827/2400, 481/1080) # Bud of Preservation
    #     await self.bot.movepi(1.4, 3600)
    #     await self.bot.interact()
    #     await self.bot.wait_for_onmap(min_duration=2)
    #     await self.bot.movepi(0.5, 500)
    #     await self.bot.movepi(0.00, 5250)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     logger('### group 3 ###')
    #     await self.bot.use_teleporter(893/2400, 482/1080) # Bud of Preservation
    #     await self.bot.movepi(1.4, 3600)
    #     await self.bot.interact()
    #     await self.bot.wait_for_onmap(min_duration=2)
    #     await self.bot.movepi(0.5, 500)
    #     await self.bot.movepi(1.0, 5700)
    #     await self.bot.movepi(0.5, 4000)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     logger('### group 4 ###')
    #     await self.bot.use_teleporter(510/2400, 594/1080) # Electrical Room
    #     await self.bot.movepi(0.5, 4500)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     logger('### group 5 ###')
    #     await self.bot.use_teleporter(512/2400, 594/1080, confirm=True) # Electrical Room
    #     await self.bot.movepi(0.5, 8000)
    #     await self.bot.movepi(1.0, 3700)
    #     await self.bot.movepi(0.5, 2300)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()

    # async def farm_storage_zone(self):
    #     logger('\nfarm: Storage Zone\n')
    #     await self.bot.switch_map(630/1080)
    #     logger('### group 1 ###')
    #     await self.bot.use_teleporter(611/2400, 534/1080, open_map=False) # Bud of Destruction
    #     await self.bot.movepi(1.5, 5200)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     logger('### group 2 ###') # roamer
    #     await self.bot.use_teleporter(708/2400, 507/1080) # Bud of Destruction
    #     await self.bot.movepi(1.5, 6000)
    #     await self.bot.movepi(1.0, 3000)
    #     await self.bot.movepi(0.5, 6300)
    #     await self.bot.movepi(1.0, 2400)
    #     await self.bot.movepi(1.5, 3800)
    #     await self.bot.movepi(1.25, 500)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     logger('### group 3 ###')
    #     await self.bot.use_teleporter(774/2400, 567/1080) # Outside of Control Center
    #     await self.bot.wait_for_onmap()
    #     logger('### group 4 ###')
    #     await self.bot.movepi(0.5, 2500)
    #     await self.bot.movepi(0.75, 1300)
    #     await self.bot.movepi(0.5, 700)
    #     await self.bot.movepi(1.0, 1000)
    #     await self.bot.movepi(0.75, 1000)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     logger('### group 5 ###')
    #     await self.bot.use_teleporter(773/2400, 570/1080)
    #     await self.bot.movepi(0.5, 2500)
    #     await self.bot.movepi(0.70, 1800)
    #     await self.bot.movepi(0.9, 1000)
    #     await self.bot.movepi(0.55, 3000)
    #     await self.bot.movepi(0.75, 3000)
    #     await self.bot.movepi(0.93, 6200)
    #     await self.bot.movepi(1.47, 2500)
    #     await self.bot.movepi(0.9, 2000)
    #     await self.bot.movepi(0.45, 100)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     logger('### group 6 ###') ###
    #     await self.bot.use_teleporter(972/2400, 534/1080, confirm=True) # Courtyard
    #     await self.bot.movepi(1.4, 1000)
    #     await self.bot.movepi(1.7, 1600)
    #     await self.bot.movepi(1.8, 700)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     logger('### group 7 ###')
    #     await self.bot.use_teleporter(914/2400, 532/1080, confirm=True) # Courtyard
    #     await self.bot.movepi(1.25, 1800)
    #     await self.bot.movepi(0.75, 700)
    #     await self.bot.movepi(1.0, 1000)
    #     await self.bot.movepi(0.75, 500)
    #     await self.bot.movepi(1.0, 2000)
    #     await self.bot.movepi(1.25, 500)
    #     await self.bot.movepi(1.0, 500)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()

    # async def farm_base_zone(self):
    #     logger('\nfarm: Base Zone\n')
    #     await self.bot.switch_map(513/1080)
    #     logger('### group 1 ###')
    #     await self.bot.use_teleporter(1045/2400, 303/1080, open_map=False, move_y=0.2)
    #     await self.bot.movepi(1.5, 2500)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()