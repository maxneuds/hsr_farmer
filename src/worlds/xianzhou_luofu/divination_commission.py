from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra
from datetime import datetime as dt


class Divination_Commission:
    def __init__(self, device):
        self.map = 'Divination Commission'
        self.bot = Bot(device)
        self.extra = Extra(device)
    async def farm(self):
        t_start = dt.now()
        await self.teleport()
        await self.path_1()
        await self.extra.restore_tp(tp=2, info="Divination Commission")
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
        logger.info('--- Map: Divination Commission')
        logger.info('---')
        await self.bot.switch_map(y_list=989/1080, world='the_xianzhou_luofu', scroll_down=False,
                                    x=848/2400, y=524/1080, corner='botright', move_x=0, move_y=0) # Bud of Aether
        await self.bot.move(1.25, 2600)
        await self.bot.attack_technique(6) # -1TP
    async def path_1(self):
        logger_set_path(self.map, 1)
        await self.bot.use_teleporter(445/2400, 720/1080, corner='botright', move_x=0, move_y=0, confirm=True) # Fortuna Augurstead
        await self.bot.move(0.5, 4000)
        await self.bot.move(0.7, 1500)
        await self.bot.attack() # items
        await self.bot.move(1.1, 1600)
        await self.bot.move(0.75, 500)
        await self.bot.attack_technique(5) # -1TP
        await self.bot.move(1.5, 500)
        await self.bot.attack_technique(4) # -1TP
    async def path_2(self):
        logger_set_path(self.map, 2)
        await self.bot.switch_map(y_list=989/1080, world='the_xianzhou_luofu', scroll_down=False, # Fortuna Augurstead
                                    x=445/2400, y=720/1080, corner='botright', move_x=0, move_y=0, confirm=True)
        await self.bot.move(0.5, 4000)
        await self.bot.move(0.7, 1000)
        await self.bot.move(1.0, 2000)
        await self.bot.move(0.7, 1200)
        await self.bot.move(1.0, 10700)
        await self.bot.move(0.5, 800)
        await self.bot.move(0.4, 500)
        await self.bot.attack_technique(1) # -3TP, roamer
        await self.bot.move(0.7, 200)
        await self.bot.attack_technique(1)
        for _ in range(5):
            await self.bot.move(1.0, 300)
            await self.bot.attack_technique(1)
        for _ in range(4):
            await self.bot.move(1.5, 300)
            await self.bot.attack_technique(1)
        await self.bot.attack_technique(1)
    async def path_3(self):
        logger_set_path(self.map, 3)
        await self.bot.use_teleporter(445/2400, 720/1080, move_x=0, move_y=0, corner='botright', confirm=True) # Fortuna Augurstead
        await self.bot.move(0.5, 4000)
        await self.bot.move(0.7, 1000)
        await self.bot.move(1.0, 2000)
        await self.bot.move(0.7, 1200)
        await self.bot.move(1.0, 10700)
        await self.bot.move(1.5, 1500)
        await self.bot.move(1.6, 500)
        await self.bot.attack() # +2TP
        await self.bot.posfix(1.75, 1000)
        await self.bot.move(0.75, 1000)
        await self.bot.move(1.0, 1500)
        await self.bot.move(1.5, 500)
        await self.bot.attack_technique(5)
        await self.bot.move(1.2, 1000)
        await self.bot.move(1.5, 300)
        await self.bot.attack_technique(14) # -1TP
    async def path_4(self):
        logger_set_path(self.map, 4)
        await self.bot.use_teleporter(627/2400, 308/1080, corner='botright', move_x=0, move_y=3) # Matrix of Prescience Ultima
        await self.bot.move(0.75, 800)
        await self.bot.attack() # +2TP
    async def path_5(self): # roamer
        logger_set_path(self.map, 5)
        await self.bot.use_teleporter(1089/2400, 284/1080, corner='botright', move_x=0, move_y=0) # Conclave Hall
        await self.bot.move(1.5, 22900)
        await self.bot.move(1.25, 2200)
        await self.bot.move(1.5, 300)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.move(0.0, 300)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.move(1.5, 3000)
        await self.bot.posfix(1.25, 1000)
        await self.bot.move(0.1, 3000)
        await self.bot.attack() # +2TP
        await self.bot.move(1.75, 1000)
        await self.bot.posfix(1.75, 1000)
        await self.bot.move(0.75, 5000)
        await self.bot.move(1.0, 3500)
        for _ in range(4): # -3TP
            await self.bot.move(1.3, 300)
            await self.bot.attack_technique(1)
        for _ in range(2):
            await self.bot.move(1.3, 300)
            await self.bot.attack_technique(2)
        for _ in range(9):
            await self.bot.move(0.4, 300)
            await self.bot.attack_technique(1)
        for _ in range(6):
            await self.bot.move(1.5, 300)
            await self.bot.attack_technique(1)
    async def path_6(self):
        logger_set_path(self.map, 6)
        await self.bot.use_teleporter(1089/2400, 284/1080, corner='botright', move_x=0, move_y=0) # Conclave Hall
        await self.bot.move(1.0, 1100)
        await self.bot.move(0.7, 2100)
        await self.bot.attack() # items
        await self.bot.move(1.7, 3500)
        await self.bot.move(1.5, 10000)
        await self.bot.move(0.78, 1500)
        await self.bot.attack() # items
        await self.bot.move(0.75, 1000)
        await self.bot.posfix(0.75, 1000)
        await self.bot.move(1.75, 2600)
        await self.bot.move(1.5, 8500)
        await self.bot.move(0.0, 1500)
        await self.bot.attack() # items
        await self.bot.move(0.25, 1000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.2, 2500)
        await self.bot.move(1.5, 1000)
        await self.bot.move(0.0, 3000)
        await self.bot.move(1.75, 1700)
        await self.bot.move(0.0, 3500)
        await self.bot.move(0.5, 1900)
        await self.bot.move(0.0, 3700)
        await self.bot.move(1.75, 1000)
        await self.bot.move(0.0, 2500)
        await self.bot.move(1.42, 1100)
        await self.bot.attack() # +2TP
        await self.bot.move(0.4, 2500)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.35, 3800)
        await self.bot.move(1.1, 1500)
        await self.bot.move(1.0, 4300)
        await self.bot.move(1.5, 3500)
        await self.bot.move(1.75, 2000)
        await self.bot.move(1.75, 300)
        await self.bot.attack_technique(2) # -1TP
    async def path_7(self): # roamer
        logger_set_path(self.map, 7)
        await self.bot.use_teleporter(743/2400, 586/1080, corner='topleft', move_x=0, move_y=0) # Spatial Terminal
        await self.bot.move(0.4, 1500)
        await self.bot.move(0.5, 1500)
        await self.bot.move(0.7, 1200)
        await self.bot.move(0.9, 300)
        await self.bot.attack() # +2TP
        await self.bot.move(0.12, 1900)
        await self.bot.attack() # items
        await self.bot.move(0.25, 2000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.3, 1500)
        await self.bot.move(1.5, 4000)
        await self.bot.move(1.3, 800)
        await self.bot.move(1.5, 2900)
        await self.bot.move(1.75, 4500)
        await self.bot.attack_technique(4) # -2TP
        await self.bot.move(0.6, 500)
        await self.bot.attack_technique(6)    
    async def path_8(self): # roamer
        logger_set_path(self.map, 8)
        await self.bot.use_teleporter(743/2400, 586/1080, corner='topleft', move_x=0, move_y=0) # Spatial Terminal
        await self.bot.move(1.5, 3700)
        await self.bot.move(1.75, 5800)
        await self.bot.move(0.0, 1500)
        await self.bot.attack() # +2TP
        await self.bot.move(1.0, 1900)
        await self.bot.move(1.25, 2800)
        await self.bot.move(0.75, 300)
        await self.bot.attack_technique(1) # -2TP
        for _ in range(4):
            await self.bot.move(1.2, 300)
            await self.bot.attack_technique(1)
        for _ in range(4):
            await self.bot.move(1.75, 300)
            await self.bot.attack_technique(1)
    async def path_9(self):
        logger_set_path(self.map, 9)
        await self.bot.use_teleporter(743/2400, 586/1080, corner='topleft', move_x=0, move_y=0) # Spatial Terminal
        await self.bot.move(1.5, 3700)
        await self.bot.move(1.75, 11300)
        await self.bot.move(0.0, 2900)
        await self.bot.move(0.3, 1200)
        await self.bot.attack() # items
        await self.bot.move(0.0, 2500)
        await self.bot.move(0.5, 1500)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.5, 2500)
        await self.bot.move(0.0, 4500)
        await self.bot.move(0.25, 3200)
        await self.bot.move(0.0, 1400)
        await self.bot.move(0.2, 300)
        await self.bot.attack_technique(3) # -1TP


