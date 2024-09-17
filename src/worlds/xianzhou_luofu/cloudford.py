from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra
from datetime import datetime as dt


class Cloudford:
    def __init__(self, device):
        self.map = 'Cloudford'
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
        await self.path_6()
        await self.path_7()
        await self.path_8()
        await self.path_9()
        await self.extra.metrics(self.map, t_start)
    async def teleport(self):
        logger_set_path(self.map, 'Teleport')
        logger.info('---')
        logger.info('--- Map: Cloudford')
        logger.info('---')
        await self.bot.switch_map(y_list=500/1080, world='the_xianzhou_luofu', scroll_down=False, # Trove of Verdure
                                    x=925/2400, y=663/1080, corner='topleft', move_x=0, move_y=5)
        await self.bot.move(0.4, 8000)
        await self.bot.move(0.5, 3000)
        await self.bot.move(0.37, 2300)
        await self.bot.attack() # +2TP
    async def path_1(self):
        logger_set_path(self.map, 1)
        await self.bot.use_teleporter(925/2400, 663/1080, move_x=0, move_y=5, corner='topleft') # Trove of Verdure
        await self.bot.move(1.75, 2300)
        await self.bot.move(1.5, 4000)
        await self.bot.move(1.75, 2400)
        await self.bot.attack() # items
        await self.bot.move(1.5, 10000)
        await self.bot.move(1.7, 4000)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.move(0.62, 300)
        await self.bot.attack_technique(6) # -1TP
    async def path_2(self): # roamer
        logger_set_path(self.map, 2)
        await self.bot.use_teleporter(925/2400, 663/1080, move_x=0, move_y=5, corner='topleft') # Trove of Verdure
        await self.bot.move(1.75, 2300)
        await self.bot.move(1.5, 4000)
        await self.bot.move(1.75, 2400)
        await self.bot.move(1.5, 8900)
        await self.bot.move(1.0, 1000)
        await self.bot.attack() # items
        await self.bot.move(1.5, 900)
        await self.bot.move(1.4, 1100)
        await self.bot.attack() # +2TP
    async def path_3(self):
        logger_set_path(self.map, 3)
        await self.bot.use_teleporter(925/2400, 663/1080, move_x=0, move_y=5, corner='topleft') # Trove of Verdure
        raise SystemExit('check')
        await self.bot.move(0.75, 2100)
        await self.bot.move(1.0, 7500)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.move(1.9, 2000)
        await self.bot.move(1.7, 1000)
        await self.bot.move(1.9, 1000)
        await self.bot.posfix(1.75, 1000)
        for _ in range(8): # -1TP, roamer, +2TP
            await self.bot.move(0.75, 300)
            await self.bot.attack_technique(1)
            await self.bot.move(1.25, 300)
            await self.bot.attack_technique(1)
    async def path_4(self):
        logger_set_path(self.map, 4)
        await self.bot.use_teleporter(973/2400, 532/1080, move_x=0, move_y=0, corner='botright') # Skiff Boarding Area
        await self.bot.move(0, 9900)
        await self.bot.move(1.5, 1900)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.move(0.5, 2500)
        await self.bot.move(0.75, 1900)
        await self.bot.move(1, 1500)
        await self.bot.attack_technique(7) # -1TP
        await self.bot.move(0.75, 2000)
        await self.bot.posfix(0.75, 1000)
        await self.bot.move(1.75, 900)
        await self.bot.move(0, 3500)
        await self.bot.move(1.75, 400)
        await self.bot.move(0, 2900)
        await self.bot.attack() # +2TP
    async def path_5(self):
        logger_set_path(self.map, 5)
        await self.bot.use_teleporter(813/2400, 349/1080, move_x=0, move_y=0, corner='botright') # Bud of Memories
        await self.bot.move(1.65, 2900)
        await self.bot.move(1.8, 400)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.move(1.25, 500)
        await self.bot.attack_technique(3) # -1TP, roamer
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(2)
    async def path_6(self):
        logger_set_path(self.map, 6)
        await self.bot.use_teleporter(1129/2400, 642/1080, move_x=0, move_y=1, corner='topright') # Cargo Lane
        await self.bot.move(0.54, 5300)
        await self.bot.attack() # items
        await self.bot.move(0.3, 3500)
        await self.bot.move(0.0, 3000)
        await self.bot.move(1.88, 2900)
        await self.bot.attack() # +2TP
        await self.bot.move(0.5, 2600)
        await self.bot.attack() # items
        await self.bot.move(0.55, 2700)
        for _ in range(2): # -2TP, roamer
            await self.bot.move(0.25, 300)
            await self.bot.attack_technique(2)
        for _ in range(3):
            await self.bot.move(0.0, 300)
            await self.bot.attack_technique(2)
        await self.bot.move(1.1, 300)
        await self.bot.attack_technique(6)
    async def path_7(self):
        logger_set_path(self.map, 7)
        await self.bot.use_teleporter(1163/2400, 530/1080, move_x=0, move_y=0, corner='botright') # Shape of Icicle
        await self.bot.move(0.0, 1300)
        await self.bot.attack() # +2TP
        await self.bot.move(1.5, 1000)
        await self.bot.attack() # items
    async def path_8(self):
        logger_set_path(self.map, 8)
        await self.bot.use_teleporter(813/2400, 349/1080, move_x=0, move_y=0, corner='botright') # Bud of Memories
        await self.bot.move(1.65, 1700)
        await self.bot.move(0.14, 3100)
        await self.bot.move(1.5, 700)
        await self.bot.attack_technique(1) # items
        await self.bot.move(0.0, 400)
        await self.bot.attack_technique(3) # -1TP, roamer
        for _ in range(4): # -3TP, roamer
            await self.bot.move(0.7, 300)
            await self.bot.attack_technique(2)
        for _ in range(4):
            await self.bot.move(1.7, 300)
            await self.bot.attack_technique(3)
    async def path_9(self):
        logger_set_path(self.map, 9)
        await self.bot.use_teleporter(930/2400, 259/1080, move_x=0, move_y=0, corner='botright') # Cavern of Corrosion
        await self.bot.move(1.25, 1000)
        await self.bot.attack() # +2TP
       
 
