from logger import logger, logger_set_path
from sys import exit


class Base_Zone:
    def __init__(self, bot):
        self.bot = bot
    async def teleport(self):
        logger_set_path('Teleport')
        logger.info('---')
        logger.info("--- Map: Base Zone")
        logger.info('---')
        await self.bot.switch_map(y_list=508/1080, world='herta_space_station', scroll_down=True,
                                    x=1044/2400, y=405/1080, corner='topright', move_x=0, move_y=0) # Monitoring Room
        await self.bot.movepi(1.0, 1500)
        await self.bot.attack() # +2 TP
        await self.bot.movepi(0.0, 1800)
        await self.bot.movepi(1.5, 2600)
        await self.bot.attack_technique(3)
    async def path_1(self):
        logger_set_path(1)
        await self.bot.use_teleporter(x=1044/2400, y=405/1080, corner='topright', move_x=0, move_y=0) # Monitoring Room
        await self.bot.movepi(1.48, 6300)
        await self.bot.attack() # items
        await self.bot.movepi(1.65, 1800)
        await self.bot.attack() # +2 TP
        await self.bot.movepi(1.33, 2400)
        await self.bot.attack() # items
        await self.bot.movepi(1.2, 2000)
        await self.bot.movepi(1.4, 1500)
        await self.bot.attack() # items
        await self.bot.wait_for_onmap(min_duration=3, no_fight=True)

class Storage_Zone:
    def __init__(self, bot):
        self.bot = bot
    async def teleport(self, tp_restore=False):
        logger_set_path('Teleport')
        logger.info('---')
        logger.info("--- Map: Storage Zone")
        logger.info('---')
        if tp_restore == True:
            logger.info('restore tp path')
            await self.bot.switch_map(y_list=630/1080, world='herta_space_station', scroll_down=False,
                                    x=1172/2400, y=556/1080, corner='botright', move_x=0, move_y=0) # Path of Gelid Wind
            await self.bot.movepi(1.2, 600)
            await self.bot.attack() # +2 TP
        else:
            await self.bot.switch_map(y_list=630/1080, world='herta_space_station', scroll_down=False,
                                        x=510/2400, y=507/1080, corner='botright', move_x=0, move_y=0) # Bud of Destruction
            await self.bot.movepi(1.7, 500)
            await self.bot.attack() # +2 TP
    async def path_1(self):
        logger_set_path(1)
        await self.bot.use_teleporter(510/2400, 507/1080, move_x=0, move_y=0, corner='botright') # Bud of Destruction
        await self.bot.movepi(1.5, 5200)
        await self.bot.attack_technique(3)
    async def path_2(self):
        logger_set_path(2)
        await self.bot.use_teleporter(510/2400, 507/1080, move_x=0, move_y=0, corner='botright') # Bud of Destruction
        await self.bot.movepi(1.5, 6000)
        await self.bot.movepi(1.0, 3000)
        await self.bot.movepi(0.5, 6300)
        await self.bot.movepi(1.0, 2300)
        await self.bot.movepi(1.5, 3500)
        await self.bot.attack_technique(8)
    async def path_3(self):
        logger_set_path(3)
        await self.bot.use_teleporter(576/2400, 569/1080, move_x=0, move_y=0, corner='botright') # Outside the Control Center
        await self.bot.movepi(1.3, 400)
        await self.bot.attack() # items
        await self.bot.movepi(1.6, 500)
        await self.bot.attack_technique(3)
    async def path_4(self):
        logger_set_path(4)
        await self.bot.use_teleporter(576/2400, 569/1080, move_x=0, move_y=0, corner='botright') # Outside the Control Center
        await self.bot.movepi(0.49, 2100)
        await self.bot.attack() # +2 TP
        await self.bot.movepi(0.68, 2200)
        await self.bot.movepi(1.0, 1700)
        await self.bot.attack_technique(4)
    async def path_5(self):
        logger_set_path(5)
        await self.bot.use_teleporter(1068/2400, 647/1080, move_x=0, move_y=0, corner='botright') # Special Purpose Lab
        await self.bot.movepi(1.3, 1900)
        await self.bot.movepi(1.0, 4500)
        await self.bot.movepi(0.61, 6500)
        await self.bot.movepi(0.1, 200)
        await self.bot.attack_technique(8)
    async def path_6(self):
        logger_set_path(6)
        await self.bot.use_teleporter(895/2400, 530/1080, move_x=0, move_y=0, corner='botright', confirm=True) # Courtyard
        await self.bot.movepi(0.35, 2000)
        await self.bot.attack() # +2 TP
    async def path_7(self):
        logger_set_path(7)
        await self.bot.use_teleporter(895/2400, 530/1080, move_x=0, move_y=0, corner='botright', confirm=True) # Courtyard
        await self.bot.movepi(1.5, 1500)
        await self.bot.movepi(1.75, 500)
        await self.bot.attack_technique(8)
    async def path_8(self):
        logger_set_path(8)
        await self.bot.use_teleporter(895/2400, 530/1080, move_x=0, move_y=0, corner='botright', confirm=True) # Courtyard
        await self.bot.movepi(1.19, 2400)
        await self.bot.movepi(0.7, 1500)
        await self.bot.attack()
        await self.bot.movepi(1.05, 3000)
        await self.bot.attack_technique(8)

class Supply_Zone:
    def __init__(self, bot):
        self.bot = bot
    async def teleport(self, tp_restore=False):
        logger_set_path('Teleport')
        logger.info('---')
        logger.info("--- Map: Supply Zone")
        logger.info('---')
        if tp_restore == True:
            logger.info('restore tp path')
            await self.bot.switch_map(y_list=745/1080, world='herta_space_station', scroll_down=False,
                                    x=1315/2400, y=434/1080, corner='botright', move_x=0, move_y=0) # Destruction's Beginning
            await self.bot.movepi(0.1, 800)
            await self.bot.attack() # +2 TP
        else:
            await self.bot.switch_map(y_list=750/1080, world='herta_space_station', scroll_down=True,
                                        x=510/2400, y=595/1080, corner='botleft', move_x=0, move_y=0, confirm=True) # Electrical Room
            await self.bot.movepi(0.25, 2800)
            await self.bot.attack() # +2 TP
    async def path_1(self):
        logger_set_path(1)
        await self.bot.use_teleporter(x=510/2400, y=595/1080, corner='botleft', move_x=0, move_y=0, confirm=True) # Electrical Room
        await self.bot.movepi(0.46, 3700)
        await self.bot.attack_technique(4)
    async def path_2(self):
        logger_set_path(2)
        await self.bot.use_teleporter(x=510/2400, y=595/1080, corner='botleft', move_x=0, move_y=0, confirm=True) # Electrical Room
        await self.bot.movepi(0.5, 7800)
        await self.bot.movepi(1.0, 3700)
        await self.bot.movepi(0.5, 2000)
        await self.bot.attack_technique(5)
    async def path_3(self):
        logger_set_path(3)
        await self.bot.use_teleporter(x=848/2400, y=376/1080, corner='botleft', move_x=0, move_y=0) # Spare Parts Warehouse
        await self.bot.movepi(1.55, 2500)
        await self.bot.attack() # +2 TP
    async def path_4(self):
        logger_set_path(4)
        await self.bot.use_teleporter(x=848/2400, y=376/1080, corner='botleft', move_x=0, move_y=0) # Spare Parts Warehouse
        await self.bot.movepi(0.5, 6300)
        await self.bot.attack_technique(3)
    async def path_5(self):
        logger_set_path(5)
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
        logger_set_path(6)
        await self.bot.use_teleporter(x=893/2400, y=479/1080, corner='botleft', move_x=0, move_y=0) # Bud of Preservation
        await self.bot.movepi(1.65, 800)
        await self.bot.attack() # items
        await self.bot.movepi(1.1, 1000)
        await self.bot.movepi(1.43, 2100)
        await self.bot.interact()
        await self.bot.wait_for_onmap(min_duration=2)
        await self.bot.movepi(0.5, 500)
        await self.bot.movepi(1.0, 5700)
        await self.bot.movepi(0.5, 3900)
        await self.bot.attack_technique(1, wait=False)
        await self.bot.movepi(1.95, 1800)
        await self.bot.attack_technique(2)
    async def path_7(self):
        logger_set_path(7)
        await self.bot.use_teleporter(x=1036/2400, y=583/1080, corner='botright', move_x=0, move_y=0) # Railway Platform
        await self.bot.movepi(0.4, 1500)
        await self.bot.attack() # items
        await self.bot.movepi(1.4, 4900)
        await self.bot.movepi(1.0, 5600)
        await self.bot.movepi(1.3, 500)
        await self.bot.attack() # +2 TP
        await self.bot.movepi(0.59, 2200)
        await self.bot.attack() # items

class Seclusion_Zone:
    def __init__(self, bot):
        self.bot = bot
    async def teleport(self):
        logger_set_path('Teleport')
        logger.info('---')
        logger.info("--- Map: Seclusion Zone")
        logger.info('---')
        await self.bot.switch_map(y_list=863/1080, world='herta_space_station', scroll_down=True,
                                    x=1079/2400, y=376/1080, move_x=0, move_y=1) # Incubator
        await self.bot.movepi(0.0, 2700)
        await self.bot.attack() # +2 TP
    async def path_1(self):
        logger_set_path(1)
        await self.bot.use_teleporter(1097/2400, 285/1080, move_x=0, move_y=3, corner='botright') # Breeding Ground
        await self.bot.movepi(0.06, 4000)
        await self.bot.movepi(1.95, 6000)
        await self.bot.movepi(1.8, 4500)
        await self.bot.movepi(1.75, 3200)
        await self.bot.movepi(1.5, 200)
        await self.bot.attack_technique(6)
    async def path_2(self):
        logger_set_path(2)
        await self.bot.use_teleporter(1097/2400, 285/1080, move_x=0, move_y=3, corner='botright') # Breeding Ground
        await self.bot.movepi(0.06, 4000)
        await self.bot.movepi(1.95, 6000)
        await self.bot.movepi(1.8, 4500)
        await self.bot.movepi(1.75, 4500)
        await self.bot.movepi(1.6, 4500)
        await self.bot.movepi(1.5, 500)
        await self.bot.attack() # +2 TP
        await self.bot.movepi(1.6, 800)
        await self.bot.attack_technique(6)
    async def path_3(self):
        logger_set_path(3)
        await self.bot.use_teleporter(919/2400, 563/1080, move_x=0, move_y=0, corner='botright') # Pharmaceutical Room
        await self.bot.movepi(0.3, 2200)
        await self.bot.movepi(0.00, 1700)
        await self.bot.movepi(1.8, 1400)
        await self.bot.attack()
        # TODO: integrate path 4 using positing fixing
    async def path_4(self):
        logger_set_path(4)
        await self.bot.use_teleporter(919/2400, 563/1080, move_x=0, move_y=0, corner='botright') # Pharmaceutical Room
        await self.bot.movepi(0.3, 2200)
        await self.bot.movepi(0.00, 1700)
        await self.bot.movepi(1.78, 5500)
        await self.bot.movepi(1.35, 3200)
        await self.bot.movepi(1.8, 2300)
        await self.bot.attack()
        await self.bot.movepi(1.68, 6100)
        await self.bot.attack()
        await self.bot.movepi(1.3, 2500)
        await self.bot.attack() # +2 TP
        await self.bot.movepi(1.6, 3500)
        await self.bot.movepi(1.5, 700)
        await self.bot.attack_technique(9)

