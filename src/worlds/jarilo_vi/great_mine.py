from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra
from datetime import datetime as dt


class Great_Mine:
    def __init__(self, device):
        self.map = 'Great Mine'
        self.bot = Bot(device)
        self.extra = Extra(device)
    async def farm(self):
        t_start = dt.now()
        # await self.teleport()
        # await self.path_1()
        # await self.path_2() # TODO: path1+2 might be combined
        await self.path_3()
        await self.path_4()
        await self.path_5()
        await self.path_6()
        # await self.extra.metrics(self.map, t_start)
    async def teleport(self):
        logger_set_path(self.map, 'Teleport')
        logger.info('---')
        logger.info("--- Map: Great Mine")
        logger.info('---')
        await self.bot.switch_map(y_list=687/1080, world='jarilo_vi', scroll_down=True, # Vagrant Shelter
                                    x=1220/2400, y=328/1080, corner='topright', move_x=0, move_y=3)
        await self.bot.move(0.9, 2000)
        await self.bot.move(1.2, 900)
        await self.bot.attack() # items
        await self.bot.move(1.1, 500)
        await self.bot.move(0.9, 1000)
        await self.bot.move(1.0, 1000)
        await self.bot.move(1.2, 1700)
        await self.bot.move(1.07, 4000)
        await self.bot.attack() # items
        await self.bot.move(0.5, 900)
        await self.bot.move(1.0, 2700)
        await self.bot.move(1.45, 2500)
        await self.bot.move(1.8, 1000)
        await self.bot.attack_technique(6) # -1TP
        await self.bot.move(0.25, 4000) # stability move
    async def path_1(self):
        logger_set_path(self.map, 1)
        await self.bot.use_teleporter(x=956/2400, y=610/1080, corner='botright', move_x=0, move_y=0, confirm=True) # Overlook
        await self.bot.move(1.8, 2000)
        await self.bot.move(0.1, 4600)
        await self.bot.move(0.2, 900)
        await self.bot.attack_technique(3) # -1TP
    async def path_2(self): # roamer
        logger_set_path(self.map, 2)
        await self.bot.use_teleporter(x=912/2400, y=755/1080, corner='botright', move_x=0, move_y=0) # Main Mine Shaft
        await self.bot.move(1.02, 2700)
        await self.bot.attack() # +2TP
        await self.bot.move(1.1, 4000)
        await self.bot.move(0.9, 700)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.move(1.5, 500)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.posfix(1.25, 4000)
        await self.bot.move(0.49, 800)
        await self.bot.move(0.85, 2300)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.move(1.1, 700)
        await self.bot.attack_technique(2) # items
        await self.bot.move(1.8, 2000)
        await self.bot.posfix(1.75, 1500)
        await self.bot.move(0.5, 2000)
        await self.bot.move(0.1, 2000)
        await self.bot.move(1.85, 3000)
        await self.bot.move(1.9, 1000)
        await self.bot.move(0.0, 600)
        await self.bot.move(0.25, 600)
        await self.bot.move(0.3, 1900)
        await self.bot.attack_technique(1) # items
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(3) # -1TP
    async def path_3(self):
        logger_set_path(self.map, 3)
        await self.bot.use_teleporter(x=665/2400, y=435/1080, corner='topleft', move_x=0, move_y=0, confirm=True) # Entrance
        raise SystemExit('check')
        await self.bot.move(0.2, 1500)
        await self.bot.attack_technique(1) # +2TP
        await self.bot.move(0.9, 300)
        await self.bot.attack_technique(5) # move
        await self.bot.move(0.6, 300)
        await self.bot.attack_technique(4) # move
        await self.bot.move(0.3, 300)
        await self.bot.attack_technique(5) # items
        await self.bot.move(0.4, 1500)
        await self.bot.posfix(0.5, 500)
        await self.bot.move(1.7, 700)
        await self.bot.move(0.0, 300)
        await self.bot.attack_technique(4) # move
        await self.bot.move(0.2, 300)
        await self.bot.attack_technique(3) # move
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(10) # items
        await self.bot.move(1.0, 900)
        await self.bot.move(0.75, 300)
        await self.bot.attack_technique(16) # items
    async def path_4(self): # roamer
        logger_set_path(self.map, 4)
        await self.bot.use_teleporter(x=1296/2400, y=600/1080, corner='botright', move_x=0, move_y=0) # Shape of Scorch
        await self.bot.move(1.23, 1700)
        await self.bot.attack() # items
        await self.bot.move(1.23, 2000)
        await self.bot.attack() # +2TP
        await self.bot.move(1.15, 1200)
        await self.bot.move(0.75, 1800)
        await self.bot.move(0.33, 3800)
        await self.bot.attack() # items
        await self.bot.move(1.33, 4700)
        await self.bot.move(1.1, 1500)
        await self.bot.move(1.2, 700)
        await self.bot.move(1.0, 400)
        await self.bot.attack_technique(2) # -2TP
        await self.bot.move(1.1, 500)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.move(1.3, 500)
        await self.bot.attack_technique(2)
        await self.bot.move(1.0, 500)
        await self.bot.attack_technique(5)
    async def path_5(self): # roamer
        logger_set_path(self.map, 5)
        await self.bot.use_teleporter(x=951/2400, y=480/1080, corner='botright', move_x=0, move_y=0) # Shape of Spike
        await self.bot.move(1.8, 1500)
        await self.bot.attack() # +2TP
        await self.bot.move(0.8, 3000)
        await self.bot.move(0.9, 1000)
        await self.bot.move(1.05, 3000)
        await self.bot.move(1.2, 1000)
        await self.bot.attack_technique(3) # -2TP
        for _ in range(2): # -1TP
            await self.bot.move(0.49, 500)
            await self.bot.attack_technique(2)
    async def path_6(self):
        logger_set_path(self.map, 6)
        await self.bot.use_teleporter(x=951/2400, y=480/1080, corner='botright', move_x=0, move_y=0) # Shape of Spike
        await self.bot.move(0.8, 1500)
        await self.bot.move(0.9, 1000)
        await self.bot.move(1.0, 5500)
        await self.bot.move(1.05, 1000)
        await self.bot.move(0.9, 1000)
        await self.bot.move(0.5, 200)
        await self.bot.attack() # +2TP
        await self.bot.move(0.5, 1000)
        await self.bot.move(0.0, 1500)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.5, 1000)
        await self.bot.move(0.0, 1800)
        await self.bot.move(0.55, 2200)
        await self.bot.move(0.2, 1900)
        await self.bot.attack_technique(2) # -2TP


