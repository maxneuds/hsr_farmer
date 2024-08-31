from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra


class Seclusion_Zone:
    def __init__(self, device):
        self.map = 'Seclusion Zone'
        self.bot = Bot(device)
    async def farm(self):
        await self.teleport()
        await self.path_1()
        await self.path_2()
        await self.path_3()
    async def teleport(self):
        logger_set_path(self.map, 'Teleport')
        logger.info('---')
        logger.info("--- Map: Seclusion Zone")
        logger.info('---')
        await self.bot.switch_map(y_list=863/1080, world='herta_space_station', scroll_down=True, # Breeding Ground
                                    x=1097/2400, y=285/1080, corner='botright', move_x=0, move_y=3)
        await self.bot.move(0.06, 4000)
        await self.bot.move(1.95, 6000)
        await self.bot.move(1.8, 6000)
        await self.bot.move(1.7, 1500)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.move(0.0, 300)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.move(1.0, 2000)
        await self.bot.move(1.4, 2500)
        await self.bot.posfix(1.4, 1000)
        await self.bot.move(0.2, 600)
        await self.bot.move(1.6, 3900)
        await self.bot.move(1.5, 700)
        await self.bot.attack_technique(1) # +2TP
        await self.bot.move(1.6, 300)
        await self.bot.attack_technique(5) # -1TP
    async def path_1(self):
        logger_set_path(self.map, 1)
        await self.bot.use_teleporter(919/2400, 563/1080, move_x=0, move_y=0, corner='botright') # Pharmaceutical Room
        await self.bot.move(0.3, 2200)
        await self.bot.move(0.00, 1700)
        await self.bot.move(1.8, 1400)
        await self.bot.attack() # items
        await self.bot.move(1.8, 2000)
        await self.bot.move(1.9, 1500)
        await self.bot.posfix(0.0, 1000)
        await self.bot.move(1.5, 1500)
        await self.bot.move(1.3, 2200)
        await self.bot.move(1.8, 2400)
        await self.bot.attack() # items
        await self.bot.move(1.68, 6100)
        await self.bot.attack() # items
        await self.bot.move(1.33, 2400)
        await self.bot.attack() # +2TP
        await self.bot.move(1.6, 3500)
        await self.bot.move(1.5, 700)
        await self.bot.attack_technique(8) # -3TP
    async def path_2(self):
        logger_set_path(self.map, 2)
        await self.bot.use_teleporter(1097/2400, 285/1080, move_x=0, move_y=3, corner='botright') # Breeding Ground
        await self.bot.move(0.1, 3000)
        await self.bot.move(0.5, 3000)
        await self.bot.move(0.9, 4000)
        await self.bot.move(1.0, 500)
        await self.bot.attack_technique(3) # +2TP
    async def path_3(self):
        logger_set_path(self.map, 3)
        await self.bot.use_teleporter(1079/2400, 376/1080, move_x=0, move_y=1, corner='botright') # Incubator
        await self.bot.move(0.0, 2700)
        await self.bot.attack() # +2TP


