from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra
from datetime import datetime as dt


class Rivet_Town:
    def __init__(self, device):
        self.map = 'Rivet Town'
        self.bot = Bot(device)
        self.extra = Extra(device)
    async def farm(self):
        t_start = dt.now()
        await self.teleport()
        await self.path_1()
        await self.path_2()
        await self.path_3()
        await self.path_4()
        await self.path_5()
        await self.extra.metrics(self.map, t_start)
    async def teleport(self):
        logger_set_path(self.map, 'Teleport')
        logger.info('---')
        logger.info("--- Map: Rivet Town")
        logger.info('---')
        await self.bot.switch_map(y_list=808/1080, world='jarilo_vi', scroll_down=True,
                                    x=832/2400, y=597/1080, corner='topleft', move_x=0, move_y=0) # Abandoned Market
        await self.bot.move(0.9, 700)
        await self.bot.attack() # +2TP
    async def path_1(self):
        logger_set_path(self.map, 1)
        await self.bot.use_teleporter(x=998/2400, y=393/1080, corner='topright', move_x=0, move_y=0) # Orphanage
        # TODO: improve posfix timings
        await self.bot.move(1.6, 1500)
        await self.bot.move(1.25, 1000)
        await self.bot.move(1.1, 1000)
        await self.bot.move(1.0, 2800)
        await self.bot.move(0.88, 1000)
        await self.bot.attack_technique(2) # -2TP
        await self.bot.move(0.9, 2000)
        await self.bot.move(1.25, 2000)
        await self.bot.posfix(1.25, 500)
        await self.bot.move(0.25, 2500)
        await self.bot.move(0.5, 2900)
        await self.bot.move(1.9, 600)
        await self.bot.move(1.6, 200)
        await self.bot.attack() # items
        await self.bot.move(0.5, 1000)
        await self.bot.move(0.25, 2300)
        await self.bot.move(0.5, 100)
        await self.bot.attack() # +2TP
        await self.bot.move(1.75, 3000)
        await self.bot.posfix(1.75, 1500)
        await self.bot.move(0.75, 1000)
        await self.bot.move(1.1, 3000)
        await self.bot.move(1.0, 400)
        await self.bot.move(0.5, 4400)
        await self.bot.move(0.98, 1900)
        await self.bot.attack() # items
        await self.bot.move(0.75, 1000)
        await self.bot.posfix(0.75, 1500)
        await self.bot.move(0.0, 2000)
        await self.bot.move(0.5, 1900)
        await self.bot.move(0.3, 2500)
        await self.bot.move(0.5, 500)
        await self.bot.attack() # items
        await self.bot.posfix(0.5, 1500)
        await self.bot.move(1.5, 700)
        await self.bot.move(1.3, 2500)
        await self.bot.move(0.9, 1300)
        await self.bot.move(0.5, 300)
        for _ in range(6): # -2TP
            await self.bot.move(0.5, 300)
            await self.bot.attack_technique(2)
        await self.bot.move(0.1, 2500)
        await self.bot.move(0.0, 2900)
        await self.bot.attack() # +2TP
    async def path_2(self):
        logger_set_path(self.map, 2)
        await self.bot.use_teleporter(x=1017/2400, y=744/1080, corner='botright', move_x=0, move_y=0, confirm=True) # Entrance
        await self.bot.move(0.69, 1800)
        await self.bot.attack() # items
        await self.bot.move(0.4, 200)
        await self.bot.move(0.5, 1100)
        await self.bot.attack() # +2TP
    async def path_3(self):
        logger_set_path(self.map, 3)
        await self.bot.use_teleporter(x=1017/2400, y=744/1080, corner='botright', move_x=0, move_y=0, confirm=True) # Entrance
        await self.bot.move(0.5, 2500)
        await self.bot.move(0.0, 2400)
        await self.bot.move(0.25, 500)
        await self.bot.move(0.75, 700)
        await self.bot.move(1.0, 7800)
        await self.bot.move(0.5, 1700)
        await self.bot.move(0.65, 300)
        await self.bot.attack_technique(4) # -2TP
        await self.bot.move(0.5, 1200)
        for _ in range(5): # -1TP
            await self.bot.move(0.75, 300)
            await self.bot.attack_technique(2)
    async def path_4(self):
        logger_set_path(self.map, 4)
        await self.bot.use_teleporter(x=975/2400, y=599/1080, corner='topleft', move_x=0, move_y=0) # Shape of Gust
        await self.bot.move(1.65, 4000)
        await self.bot.attack() # +2TP
    async def path_5(self):
        logger_set_path(self.map, 5)
        await self.bot.use_teleporter(x=975/2400, y=599/1080, corner='topleft', move_x=0, move_y=0) # Shape of Gust
        await self.bot.move(1.0, 2500)
        await self.bot.move(0.8, 500)
        await self.bot.attack() # items
        await self.bot.move(1.5, 1000)
        await self.bot.move(1.2, 1300)
        await self.bot.move(1.5, 1000)
        await self.bot.move(1.4, 2000)
        await self.bot.attack_technique(2) # +2TP


