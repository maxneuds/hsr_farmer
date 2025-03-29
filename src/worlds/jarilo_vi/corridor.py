from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra
from datetime import datetime as dt


class Corridor:
    def __init__(self, device):
        self.map = 'Corridor of Fading Echoes'
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
        await self.extra.metrics(self.map, t_start)
    async def teleport(self):
        logger_set_path(self.map, 'Teleport')
        logger.info('Teleport')
        logger.info('---')
        logger.info("--- Map: Corridor of Fading Echoes")
        logger.info('---')
        await self.bot.switch_map(y_list=869/1080, world='jarilo_vi', scroll_down=False,
                                        x=869/2400, y=351/1080, corner='botright', move_x=0, move_y=3) # Command Center
        await self.bot.move(0.3, 4700)
        await self.bot.attack() # items
        await self.bot.move(1.0, 700)
        await self.bot.move(0.6, 300)
        await self.bot.attack_technique(3) # -2TP
        await self.bot.move(0.6, 500)
        await self.bot.attack_technique(3) # -1TP
        await self.bot.move(1.6, 500)
        await self.bot.attack_technique(3)
        await self.bot.move(0.7, 500)
        await self.bot.attack_technique(3)
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(3)
    async def path_1(self): # roamer
        logger_set_path(self.map, 1)
        await self.bot.use_teleporter(x=962/2400, y=502/1080, corner='botright', move_x=0, move_y=0) # Ancient Battlefield: Frontline
        await self.bot.move(0.7, 1000)
        await self.bot.attack() # +2TP
        await self.bot.move(1.6, 1500)
        await self.bot.move(1.5, 4100)
        await self.bot.move(1.0, 1000)
        await self.bot.attack_technique(10) # -1TP
    async def path_2(self): # roamer
        logger_set_path(self.map, 2)
        await self.bot.use_teleporter(x=962/2400, y=502/1080, corner='botright', move_x=0, move_y=0) # Ancient Battlefield: Frontline
        await self.bot.move(1.5, 5000)
        await self.bot.move(1.6, 2400)
        await self.bot.attack() # items
        await self.bot.posfix(0.9, 2500)
        await self.bot.move(1.8, 4000)
        await self.bot.move(1.7, 2000)
        await self.bot.move(1.8, 700)
        await self.bot.move(1.4, 300)
        await self.bot.move(1.5, 1000)
        await self.bot.attack_technique(2) # +2TP
        await self.bot.move(1.3, 700)
        for _ in range(4): # -1TP
            await self.bot.move(1.5, 500)
            await self.bot.attack_technique(2)
        await self.bot.move(0.7, 700)
        for _ in range(2):
            await self.bot.move(0.95, 500)
            await self.bot.attack_technique(2)
    async def path_3(self):
        logger_set_path(self.map, 3)
        await self.bot.use_teleporter(x=962/2400, y=502/1080, corner='botright', move_x=0, move_y=0) # Ancient Battlefield: Frontline
        raise SystemExit()
        await self.bot.move(1.5, 5000)
        await self.bot.move(1, 3500)
        await self.bot.move(1.51, 5000)
        await self.bot.attack_technique(7) # -3TP # just changed
        await self.bot.move(0.35, 4000)
        await self.bot.attack() # items
        await self.bot.posfix(0.3, 1000)
        await self.bot.move(1.5, 1000)
        await self.bot.move(1.3, 1200)
        await self.bot.move(1.5, 500)
        await self.bot.move(1.4, 1000)
        await self.bot.move(1.5, 500)
        await self.bot.move(1.6, 1500)
        await self.bot.move(1.47, 3600)
        await self.bot.attack() # +2TP
        await self.bot.move(1.6, 700)
        await self.bot.move(1.4, 1000)
        await self.bot.attack() # items
    async def path_4(self): #
        logger_set_path(self.map, 4)
        await self.bot.teleport(x=910/2400, y=719/1080, start=0.75, deg=1.75, n=1) # Stagnant Shadow
        await self.bot.move(1.2, 1800)
        await self.bot.move(1.0, 6000)
        await self.bot.move(1.1, 1500)
        await self.bot.attack() # items
        await self.bot.move(0.2, 800)
        await self.bot.move(1.0, 1500)
        await self.bot.attack_technique(2) # -1TP, roamer
        for _ in range(3):
            await self.bot.move(0.7, 500)
            await self.bot.attack_technique(2)
        await self.bot.attack_technique(1)
    async def path_5(self):
        logger_set_path(self.map, 5)
        await self.bot.teleport(x=910/2400, y=719/1080, start=0.75, deg=1.75, n=1) # Stagnant Shadow
        await self.bot.move(1, 1000)
        await self.bot.move(0.72, 2000)
        await self.bot.attack() # +2TP
        await self.bot.move(0.21, 2400)
        await self.bot.attack() # items
        await self.bot.move(1.1, 700)
        await self.bot.move(1.0, 5000)
        await self.bot.move(0.5, 4500)
        await self.bot.attack_technique(2) # -1TP, roamer
        for _ in range(4):
            await self.bot.move(0.25, 500)
            await self.bot.attack_technique(2)
        await self.bot.attack_technique(2)
    async def path_6(self):
        logger_set_path(self.map, 6)
        await self.bot.teleport(x=910/2400, y=719/1080, start=0.75, deg=1.75, n=1) # Stagnant Shadow
        await self.bot.move(1, 1000)
        await self.bot.move(0.75, 1550)
        await self.bot.move(0.5, 1500)
        await self.bot.move(1, 3800)
        await self.bot.move(0.5, 5500)
        await self.bot.move(0.25, 6500)
        await self.bot.move(1.75, 500)
        for _ in range(2): # -1TP, roamer
            await self.bot.move(1.75, 500)
            await self.bot.attack_technique(2)
        await self.bot.move(1.0, 500)
        await self.bot.attack_technique(2)
        for _ in range(2):
            await self.bot.move(1.6, 500)
            await self.bot.attack_technique(2)
        for _ in range(3):
            await self.bot.move(1.1, 500)
            await self.bot.attack_technique(2)
        await self.bot.attack_technique(1)
    async def path_7(self):
        logger_set_path(self.map, 7)
        await self.bot.teleport(x=1071/2400, y=530/1080, start=0.25, deg=0.0, n=0) # Cavern of Corrosion
        await self.bot.move(1.45, 1900)
        await self.bot.attack() # items
        await self.bot.move(0.35, 1700)
        await self.bot.move(1.77, 6000)
        await self.bot.move(1.39, 800)
        await self.bot.attack_technique(2) # +2TP
        await self.bot.move(0.3, 500)
        await self.bot.attack_technique(4) # -1TP, roamer
        await self.bot.move(1.7, 300)
        await self.bot.attack_technique(3)
        await self.bot.move(1.2, 500)
        await self.bot.attack_technique(4)
    async def path_8(self):
        logger_set_path(self.map, 8)
        await self.bot.teleport(x=1214/2400, y=784/1080, start=0.25, deg=0.0, n=0) # Fortified Zone
        await self.bot.move(0.15, 700)
        await self.bot.attack() # items
        await self.bot.move(0.6, 500)
        await self.bot.move(0.5, 500)
        await self.bot.move(0.2, 1200)
        await self.bot.move(0.5, 3000)
        await self.bot.move(0.39, 1700)
        await self.bot.attack() # items


