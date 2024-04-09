import asyncio as aio
from logger import logger
from automation.bot import Bot
from datetime import datetime as dt
from sys import exit

class World:
    def __init__(self, bot):
        self.bot = bot


    async def farm_base_zone(self):
        x = self.Base_Zone(bot=self.bot)
        await x.teleport()
        await x.path_1()
        await x.path_2()
    
    async def farm_storage_zone(self):
        x = self.Storage_Zone(bot=self.bot)
        await x.teleport()
        await x.path_1()
        await x.path_2()
        await x.path_3()
        await x.path_4()
        await x.path_5()
        await x.path_6()
        await x.path_7()
        await x.path_8()
        await x.path_9()
    
    async def farm_supply_zone(self):
        x = self.Supply_Zone(bot=self.bot)
        await x.teleport()
        await x.path_1()
        await x.path_2()
        await x.path_3()
        await x.path_4()
        await x.path_5()
        await x.path_6()
        await x.path_7()
    
    async def farm_seclusion_zone(self):
        x = self.Seclusion_Zone(bot=self.bot)
        await x.teleport()
        await x.path_1()
        await x.path_2()
        await x.path_3()


    class Base_Zone:
        def __init__(self, bot):
            self.bot = bot
        async def teleport(self):
            logger.info('---')
            logger.info("--- Map: Base Zone")
            logger.info('---')
            await self.bot.switch_map(y_list=508/1080, world='herta_space_station', scroll_down=True,
                                      x=1044/2400, y=405/1080, corner='topright', move_x=0, move_y=0) # Monitoring Room
            await self.bot.movepi(1.0, 1500)
            await self.bot.attack() # +2 TP
        async def path_1(self):
            logger.info('### Path 1 ###')
            await self.bot.use_teleporter(x=1044/2400, y=405/1080, corner='topright', move_x=0, move_y=0) # Monitoring Room
            await self.bot.movepi(1.5, 3000)
            await self.bot.attack_technique(10)
        async def path_2(self):
            logger.info('### Path 2 ###')
            await self.bot.use_teleporter(x=1044/2400, y=405/1080, corner='topright', move_x=0, move_y=0) # Monitoring Room
            await self.bot.movepi(1.51, 7700)
            await self.bot.attack_technique(4)

    class Storage_Zone:
        def __init__(self, bot):
            self.bot = bot
        async def teleport(self):
            logger.info('---')
            logger.info("--- Map: Storage Zone")
            logger.info('---')
            await self.bot.switch_map(y_list=630/1080, world='herta_space_station', scroll_down=False,
                                      x=510/2400, y=507/1080, corner='botright', move_x=0, move_y=0) # Bud of Destruction
            await self.bot.movepi(1.7, 500)
            await self.bot.attack() # +2 TP
        async def path_1(self):
            logger.info('### Path 1 ###')
            await self.bot.use_teleporter(510/2400, 507/1080, move_x=0, move_y=0, corner='botright') # Bud of Destruction
            await self.bot.movepi(1.5, 5200)
            await self.bot.attack_technique(3)
        async def path_2(self):
            logger.info('### Path 2 ###')
            await self.bot.use_teleporter(510/2400, 507/1080, move_x=0, move_y=0, corner='botright') # Bud of Destruction
            await self.bot.movepi(1.5, 6000)
            await self.bot.movepi(1.0, 3000)
            await self.bot.movepi(0.5, 6300)
            await self.bot.movepi(1.0, 2400)
            await self.bot.movepi(1.5, 3500)
            await self.bot.attack_technique(8)
        async def path_3(self):
            logger.info('### Path 3 ###')
            await self.bot.use_teleporter(576/2400, 569/1080, move_x=0, move_y=0, corner='botright') # Outside the Control Center
            await self.bot.movepi(1.5, 200)
            await self.bot.attack_technique(10)
        async def path_4(self): # TODO: can be done in the next path
            logger.info('### Path 4 ###')
            await self.bot.use_teleporter(576/2400, 569/1080, move_x=0, move_y=0, corner='botright') # Outside the Control Center
            await self.bot.movepi(0.49, 2500)
            await self.bot.attack()
        async def path_5(self):
            logger.info('### Path 5 ###')
            await self.bot.use_teleporter(576/2400, 569/1080, move_x=0, move_y=0, corner='botright') # Outside the Control Center
            await self.bot.movepi(0.55, 2700)
            await self.bot.movepi(0.6, 1500)
            await self.bot.movepi(1.0, 1800)
            await self.bot.attack_technique(4)
        async def path_6(self):
            logger.info('### Path 6 ###')
            await self.bot.use_teleporter(1068/2400, 647/1080, move_x=0, move_y=0, corner='botright') # Special Purpose Lab
            await self.bot.movepi(1.3, 1900)
            await self.bot.movepi(1.0, 4500)
            await self.bot.movepi(0.61, 6500)
            await self.bot.movepi(0.1, 200)
            await self.bot.attack_technique(8)
        async def path_7(self):
            logger.info('### Path 7 ###')
            await self.bot.use_teleporter(895/2400, 530/1080, move_x=0, move_y=0, corner='botright', confirm=True) # Courtyard
            await self.bot.movepi(0.35, 2000)
            await self.bot.attack() # +2 TP
        async def path_8(self):
            logger.info('### Path 8 ###')
            await self.bot.use_teleporter(895/2400, 530/1080, move_x=0, move_y=0, corner='botright', confirm=True) # Courtyard
            await self.bot.movepi(1.5, 1500)
            await self.bot.movepi(1.75, 500)
            await self.bot.attack_technique(10)
            await self.bot.restore_tp(n=1) # +2 TP
        async def path_9(self):
            logger.info('### Path 9 ###')
            await self.bot.use_teleporter(895/2400, 530/1080, move_x=0, move_y=0, corner='botright', confirm=True) # Courtyard
            await self.bot.movepi(1.19, 2400)
            await self.bot.movepi(0.7, 1500)
            await self.bot.attack()
            await self.bot.movepi(1.05, 3000)
            await self.bot.attack_technique(8)

    class Supply_Zone:
        def __init__(self, bot):
            self.bot = bot
        async def teleport(self):
            logger.info('---')
            logger.info("--- Map: Supply Zone")
            logger.info('---')
            await self.bot.switch_map(y_list=750/1080, world='herta_space_station', scroll_down=True,
                                      x=510/2400, y=595/1080, corner='botleft', move_x=0, move_y=0, confirm=True) # Electrical Room
            await self.bot.movepi(0.25, 2800)
            await self.bot.attack() # +2 TP
        async def path_1(self):
            logger.info('### Path 1 ###')
            await self.bot.use_teleporter(x=510/2400, y=595/1080, corner='botleft', move_x=0, move_y=0, confirm=True) # Electrical Room
            await self.bot.movepi(0.46, 3700)
            await self.bot.attack_technique(6)
        async def path_2(self):
            logger.info('### Path 2 ###')
            await self.bot.use_teleporter(x=510/2400, y=595/1080, corner='botleft', move_x=0, move_y=0, confirm=True) # Electrical Room
            await self.bot.movepi(0.5, 7800)
            await self.bot.movepi(1.0, 3700)
            await self.bot.movepi(0.5, 2400)
            await self.bot.attack_technique(5)
        async def path_3(self):
            logger.info('### Path 3 ###')
            await self.bot.use_teleporter(x=848/2400, y=376/1080, corner='botleft', move_x=0, move_y=0) # Spare Parts Warehouse
            await self.bot.movepi(1.55, 2500)
            await self.bot.attack() # +2 TP
        async def path_4(self):
            logger.info('### Path 4 ###')
            await self.bot.use_teleporter(x=848/2400, y=376/1080, corner='botleft', move_x=0, move_y=0) # Spare Parts Warehouse
            await self.bot.movepi(0.5, 6300)
            await self.bot.attack_technique(3)
        async def path_5(self):
            logger.info('### Path 5 ###')
            await self.bot.use_teleporter(x=893/2400, y=479/1080, corner='botleft', move_x=0, move_y=0) # Bud of Preservation
            await self.bot.movepi(1.2, 700)
            await self.bot.attack() # +2 TP
            await self.bot.movepi(1.45, 3000)
            await self.bot.interact()
            await self.bot.wait_for_onmap(min_duration=2)
            await self.bot.movepi(0.5, 500)
            await self.bot.movepi(0.00, 5200)
            await self.bot.attack_technique(3)
        async def path_6(self):
            logger.info('### Path 6 ###')
            await self.bot.use_teleporter(x=893/2400, y=479/1080, corner='botleft', move_x=0, move_y=0) # Bud of Preservation
            await self.bot.movepi(1.4, 3300)
            await self.bot.interact()
            await self.bot.wait_for_onmap(min_duration=2)
            await self.bot.movepi(0.5, 500)
            await self.bot.movepi(1.0, 5700)
            await self.bot.movepi(0.5, 4000)
            await self.bot.attack_technique(3)
        async def path_7(self):
            logger.info('### Path 7 ###')
            await self.bot.use_teleporter(x=1570/2400, y=433/1080, corner='botleft', move_x=0, move_y=0) # Destruction's Beginning
            await self.bot.movepi(0.1, 800)
            await self.bot.attack() # +2 TP

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
        async def path_1(self):
            logger.info('### Path 1 ###')
            await self.bot.use_teleporter(1097/2400, 285/1080, move_x=0, move_y=3, corner='botright') # Breeding Ground
            await self.bot.movepi(0.06, 4000)
            await self.bot.movepi(1.95, 6000)
            await self.bot.movepi(1.8, 4500)
            await self.bot.movepi(1.75, 3200)
            await self.bot.movepi(1.5, 200)
            await self.bot.attack_technique(6)
        async def path_2(self):
            logger.info('### Path 2 ###')
            await self.bot.use_teleporter(1097/2400, 285/1080, move_x=0, move_y=3, corner='botright') # Breeding Ground
            await self.bot.movepi(0.06, 4000)
            await self.bot.movepi(1.95, 6000)
            await self.bot.movepi(1.8, 4500)
            await self.bot.movepi(1.75, 4500)
            await self.bot.movepi(1.6, 4500)
            await self.bot.movepi(1.5, 500)
            await self.bot.attack()
            await self.bot.movepi(1.6, 800)
            await self.bot.attack_technique(6)
        async def path_3(self):
            logger.info('### Path 3 ###')
            await self.bot.use_teleporter(919/2400, 563/1080, move_x=0, move_y=0, corner='botright') # Pharmaceutical Room
            await self.bot.movepi(0.3, 2200)
            await self.bot.movepi(0.00, 1700)
            await self.bot.movepi(1.8, 1500)
            await self.bot.attack()
            await self.bot.movepi(1.75, 3500)
            await self.bot.movepi(1.35, 2900)
            await self.bot.movepi(1.8, 2400)
            await self.bot.attack()
            await self.bot.movepi(1.68, 6100)
            await self.bot.attack()
            await self.bot.movepi(1.3, 2500)
            await self.bot.attack() # +2 TP
            await self.bot.movepi(1.6, 3500)
            await self.bot.movepi(1.5, 700)
            await self.bot.attack_technique(9)

