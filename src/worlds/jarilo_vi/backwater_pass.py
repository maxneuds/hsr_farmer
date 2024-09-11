from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra
from datetime import datetime as dt


class Backwater_Pass:
    def __init__(self, device):
        self.map = 'Backwater Pass'
        self.bot = Bot(device)
        self.extra = Extra(device)
    async def farm(self):
        t_start = dt.now()
        await self.teleport()
        await self.path_1()
        await self.path_2()
        await self.path_3()
        await self.path_4()
        await self.extra.metrics(self.map, t_start)
    async def teleport(self):
        logger_set_path(self.map, 'Teleport')
        logger.info('Teleport')
        logger.info('---')
        logger.info("--- Map: Backwater Pass")
        logger.info('---')
        await self.bot.switch_map(y_list=629/1080, world='jarilo_vi', scroll_down=False,
                                    x=829/2400, y=273/1080, corner='botright', move_x=0, move_y=0) # Transport Hub
        await self.bot.move(1.5, 4900)
        await self.bot.move(1.0, 300)
        await self.bot.attack() # items
        await self.bot.move(1.5, 700)
        await self.bot.move(1.03, 2300)
        await self.bot.attack() # items
        await self.bot.move(0.97, 2500)
        await self.bot.move(1.0, 300)
        await self.bot.attack_technique(3) # -1TP
        await self.bot.posfix(1.3, 2000)
        await self.bot.move(0.05, 2600)
        await self.bot.move(1.5, 5500)
        await self.bot.move(1.3, 200)
        await self.bot.attack() # items
        await self.bot.move(1.0, 900)
        await self.bot.move(1.5, 2500)
        await self.bot.move(0.0, 2000)
        await self.bot.move(0.22, 2100)
        await self.bot.attack() # +2TP
    async def path_1(self):
        logger_set_path(self.map, 1)
        await self.bot.use_teleporter(x=829/2400, y=273/1080, corner='botright', move_x=0, move_y=0) # Transport Hub
        await self.bot.move(1.5, 6000)
        await self.bot.move(1.75, 3200)
        await self.bot.move(0.3, 300)
        await self.bot.attack_technique(4) # -2TP
        await self.bot.move(0.1, 500)
        await self.bot.attack_technique(8) # -1TP
        await self.bot.move(0.6, 1200)
        await self.bot.attack_technique(2) # items
    async def path_2(self):
        logger_set_path(self.map, 2)
        await self.bot.use_teleporter(x=945/2400, y=715/1080, corner='topright', move_x=0, move_y=1, confirm=True) # Leisure Plaza
        await self.bot.move(1.15, 600)
        await self.bot.attack() # +2TP
        await self.bot.move(0.5, 1000)
        await self.bot.move(1.0, 3700)
        await self.bot.move(0.5, 3500)
        await self.bot.move(0.35, 900)
        await self.bot.attack() # items
        await self.bot.move(1.0, 3100)
        await self.bot.attack() # items
        await self.bot.move(0.05, 2800)
        await self.bot.move(0.55, 2300)
        await self.bot.attack() # items
        await self.bot.posfix(0.7, 1500)
        await self.bot.move(1.7, 600)
        await self.bot.move(0.0, 5900)
        await self.bot.attack_technique(2) # -1TP
    async def path_3(self):
        logger_set_path(self.map, 3)
        await self.bot.use_teleporter(x=830/2400, y=360/1080, corner='topright', move_x=0, move_y=1) # Bud of Aether
        await self.bot.move(0.68, 900)
        await self.bot.attack() # items
        await self.bot.move(1.5, 2700)
        await self.bot.move(0.0, 1300)
        await self.bot.attack() # +2TP
        await self.bot.move(1.78, 1600)
        await self.bot.attack() # items
        await self.bot.move(0.8, 700)
        await self.bot.move(0.85, 3200)
        await self.bot.move(1.0, 3100)
        await self.bot.move(1.29, 2400)
        await self.bot.attack_technique(3) # -2TP
        await self.bot.move(1.3, 700)
        await self.bot.attack_technique(1)
        for _ in range(4): # -1TP, roamer
            await self.bot.move(1.0, 300)
            await self.bot.attack_technique(3)
    async def path_4(self):
        logger_set_path(self.map, 4)
        await self.bot.use_teleporter(x=829/2400, y=273/1080, corner='botright', move_x=0, move_y=0) # Transport Hub
        await self.bot.move(0.8, 700)
        await self.bot.attack() # +2TP


