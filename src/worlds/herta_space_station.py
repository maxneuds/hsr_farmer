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
        await self.bot.movepi(1.0, 1600)
        await self.bot.attack() # +2TP
        await self.bot.movepi(1.25, 2000)
        await self.bot.posfix(1.25, 1500)
        await self.bot.movepi(0.25, 1000)
        await self.bot.movepi(0.0, 1100)
        await self.bot.movepi(1.5, 2500)
        await self.bot.attack_technique(6)
    async def path_1(self):
        logger_set_path(1)
        await self.bot.use_teleporter(x=1044/2400, y=405/1080, corner='topright', move_x=0, move_y=0) # Monitoring Room
        await self.bot.movepi(1.48, 6300)
        await self.bot.attack() # items
        await self.bot.movepi(1.65, 1800)
        await self.bot.attack() # +2TP
        await self.bot.movepi(1.33, 2400)
        await self.bot.attack() # items
        await self.bot.movepi(1.2, 2000)
        await self.bot.movepi(1.4, 1500)
        await self.bot.attack() # items

class Storage_Zone:
    def __init__(self, bot):
        self.bot = bot
    async def teleport(self):
        logger_set_path('Teleport')
        logger.info('---')
        logger.info("--- Map: Storage Zone")
        logger.info('---')
        logger.info('path: restore TP')
        await self.bot.switch_map(y_list=630/1080, world='herta_space_station', scroll_down=False,
                                x=1068/2400, y=647/1080, corner='botright', move_x=0, move_y=0) # Special Purpose Lab
        await self.bot.movepi(1.3, 1900)
        await self.bot.movepi(1.0, 4500)
        await self.bot.movepi(0.61, 6500)
        await self.bot.movepi(0.1, 200)
        await self.bot.attack_technique(6) # -1TP
    async def path_1(self):
        logger_set_path(1)
        await self.bot.use_teleporter(576/2400, 569/1080, move_x=0, move_y=0, corner='botright') # Outside the Control Center
        await self.bot.movepi(1.3, 400)
        await self.bot.attack() # items
        await self.bot.movepi(1.6, 300)
        await self.bot.attack_technique(3) # -1TP
        await self.bot.posfix(1.75, 1000)
        await self.bot.movepi(1.0, 600)
        await self.bot.movepi(1.4, 1500)
        await self.bot.movepi(1.6, 500)
        await self.bot.attack() # +2TP
        await self.bot.movepi(0.6, 800)
        await self.bot.movepi(0.4, 1500)
        await self.bot.movepi(0.5, 4000)
        await self.bot.movepi(0.2, 500)
        await self.bot.attack() # +2TP
        await self.bot.movepi(0.25, 500)
        await self.bot.posfix(0.25, 1000)
        await self.bot.movepi(1.0, 600)
        await self.bot.movepi(0.7, 2200)
        await self.bot.movepi(1.1, 800)
        await self.bot.attack_technique(4) # -1TP
    async def path_2(self):
        logger_set_path(2)
        await self.bot.use_teleporter(895/2400, 530/1080, move_x=0, move_y=0, corner='botright', confirm=True) # Courtyard
        await self.bot.movepi(1.5, 1500)
        await self.bot.movepi(1.75, 500)
        await self.bot.attack_technique(8) # -1TP, roamer
    async def path_3(self):
        logger_set_path(3)
        await self.bot.use_teleporter(510/2400, 507/1080, move_x=0, move_y=0, corner='botright') # Bud of Destruction
        await self.bot.movepi(1.6, 700)
        await self.bot.attack() # +2TP
        await self.bot.movepi(1.4, 1200)
        await self.bot.movepi(1.5, 3800)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.movepi(1.75, 2000)
        await self.bot.posfix(1.75, 1000)
        await self.bot.movepi(0.8, 1000)
        await self.bot.movepi(1.0, 2800)
        await self.bot.movepi(0.5, 6400)
        await self.bot.movepi(1.0, 2200)
        await self.bot.movepi(1.5, 1500)
        for _ in range(2): # -1TP
            await self.bot.movepi(1.5, 300)
            await self.bot.attack_technique(2)
        for _ in range(2):
            await self.bot.movepi(1.25, 300)
            await self.bot.attack_technique(2)
    async def path_4(self):
        logger_set_path(4)
        await self.bot.use_teleporter(895/2400, 530/1080, move_x=0, move_y=0, corner='botright') # Courtyard
        await self.bot.movepi(0.35, 2000)
        await self.bot.attack() # +2TP
        await self.bot.movepi(1.35, 3100)
        await self.bot.movepi(1.0, 1500)
        await self.bot.movepi(0.88, 1200)
        await self.bot.attack() # items
        await self.bot.movepi(1.05, 3000)
        await self.bot.attack_technique(5) # -2TP
    async def path_5(self):
        logger_set_path(5)
        await self.bot.use_teleporter(1172/2400, 556/1080, move_x=0, move_y=0, corner='botright') # Path of Gelid Wind
        await self.bot.movepi(1.2, 600)
        await self.bot.attack() # +2TP
        

class Supply_Zone:
    def __init__(self, bot):
        self.bot = bot
    async def teleport(self, tp_restore=-1):
        logger_set_path('Teleport')
        logger.info('---')
        logger.info("--- Map: Supply Zone")
        logger.info('---')
        if tp_restore == 4:
            logger.info('path: restore TP')
            await self.bot.switch_map(y_list=745/1080, world='herta_space_station', scroll_down=False,
                                    x=1315/2400, y=434/1080, corner='botright', move_x=0, move_y=0) # Destruction's Beginning
            await self.bot.movepi(0.1, 800)
            await self.bot.attack() # +2TP
            await self.bot.use_teleporter(x=1036/2400, y=583/1080, corner='botright', move_x=0, move_y=0) # Railway Platform
            await self.bot.movepi(0.4, 1500)
            await self.bot.attack() # items
            await self.bot.movepi(1.4, 4900)
            await self.bot.movepi(1.0, 5600)
            await self.bot.movepi(1.3, 500)
            await self.bot.attack() # +2TP
            await self.bot.movepi(0.59, 2200)
            await self.bot.attack() # items
        else:
            await self.bot.switch_map(y_list=750/1080, world='herta_space_station', scroll_down=True, # Electrical Room
                                        x=510/2400, y=595/1080, corner='botleft', move_x=0, move_y=0, confirm=True)
            await self.bot.movepi(0.5, 3000)
            await self.bot.movepi(0.25, 500)
            await self.bot.attack_technique(5) # -2TP
            await self.bot.movepi(1.0, 1000)
            await self.bot.movepi(0.75, 1000)
            await self.bot.posfix(0.75, 1000)
            await self.bot.movepi(0.1, 1600)
            await self.bot.movepi(0.5, 1200)
            await self.bot.movepi(1.0, 3600)
            await self.bot.movepi(0.5, 300)
            await self.bot.attack_technique(10) # -1TP
    async def path_1(self):
        logger_set_path(1)
        await self.bot.use_teleporter(x=848/2400, y=376/1080, corner='botleft', move_x=0, move_y=0) # Spare Parts Warehouse
        await self.bot.movepi(1.5, 2100)
        await self.bot.movepi(1.7, 500)
        await self.bot.attack() # +2TP
        await self.bot.movepi(0.7, 700)
        await self.bot.movepi(0.5, 300)
        await self.bot.attack_technique(16) # -1TP
    async def path_2(self):
        logger_set_path(2)
        await self.bot.use_teleporter(x=893/2400, y=479/1080, corner='botleft', move_x=0, move_y=0) # Bud of Preservation
        await self.bot.movepi(1.2, 700)
        await self.bot.attack() # +2TP
        await self.bot.movepi(1.9, 900)
        await self.bot.attack() # items
        await self.bot.movepi(1.0, 1200)
        await self.bot.movepi(1.45, 2300)
        await self.bot.interact()
        await self.bot.wait_for_onmap(min_duration=2)
        await self.bot.movepi(0.5, 500)
        await self.bot.movepi(0.0, 5000)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.movepi(1.5, 1000)
        await self.bot.movepi(1.75, 1000)
        await self.bot.posfix(1.5, 1000)
        await self.bot.movepi(0.7, 1000)
        await self.bot.movepi(1.0, 300)
        await self.bot.attack_technique(20)
        await self.bot.movepi(0.4, 2500)
        await self.bot.movepi(0.5, 1200)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.movepi(0.0, 300)
        await self.bot.attack_technique(3) # items
    async def path_3(self):
        logger_set_path(3)
        await self.bot.use_teleporter(x=510/2400, y=595/1080, corner='botleft', move_x=0, move_y=0) # Electrical Room
        await self.bot.movepi(0.7, 2600)
        await self.bot.attack() # items
        await self.bot.movepi(0.0, 300)
        await self.bot.attack_technique(7) # +2TP
    

class Seclusion_Zone:
    def __init__(self, bot):
        self.bot = bot
    async def teleport(self):
        logger_set_path('Teleport')
        logger.info('---')
        logger.info("--- Map: Seclusion Zone")
        logger.info('---')
        await self.bot.switch_map(y_list=863/1080, world='herta_space_station', scroll_down=True, # Breeding Ground
                                    x=1097/2400, y=285/1080, corner='botright', move_x=0, move_y=3, confirm=False)
        await self.bot.movepi(0.06, 4000)
        await self.bot.movepi(1.95, 6000)
        await self.bot.movepi(1.8, 4500)
        await self.bot.movepi(1.75, 3200)
        await self.bot.movepi(1.5, 200)
        await self.bot.attack_technique(4) # -2TP
        await self.bot.movepi(1.1, 1500)
        await self.bot.movepi(1.4, 3000)
        await self.bot.posfix(1.4, 1000)
        await self.bot.movepi(0.25, 500)
        await self.bot.movepi(1.65, 5000)
        await self.bot.movepi(1.5, 1800)
        await self.bot.attack_technique(5) # -1TP
    async def path_1(self):
        logger_set_path(1)
        await self.bot.use_teleporter(919/2400, 563/1080, move_x=0, move_y=0, corner='botright') # Pharmaceutical Room
        await self.bot.movepi(0.3, 2200)
        await self.bot.movepi(0.00, 1700)
        await self.bot.movepi(1.8, 1400)
        await self.bot.attack() # items
        await self.bot.movepi(1.8, 2000)
        await self.bot.movepi(1.9, 1500)
        await self.bot.posfix(0.0, 1000)
        await self.bot.movepi(1.5, 1500)
        await self.bot.movepi(1.3, 2200)
        await self.bot.movepi(1.8, 2400)
        await self.bot.attack() # items
        await self.bot.movepi(1.68, 6100)
        await self.bot.attack() # items
        await self.bot.movepi(1.33, 2400)
        await self.bot.attack() # +2TP
        await self.bot.movepi(1.6, 3500)
        await self.bot.movepi(1.5, 700)
        await self.bot.attack_technique(8) # -3TP
    async def path_2(self):
        logger_set_path(2)
        await self.bot.use_teleporter(1079/2400, 376/1080, move_x=0, move_y=1, corner='botright') # Incubator
        await self.bot.movepi(0.0, 2700)
        await self.bot.attack() # +2TP


