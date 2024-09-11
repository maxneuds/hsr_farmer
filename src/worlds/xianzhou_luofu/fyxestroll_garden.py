from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra
from datetime import datetime as dt


class Fyxestroll_Garden:
    def __init__(self, device):
        self.map = 'Fyxestroll Garden'
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
        logger.info('---')
        logger.info('--- Map: Fyxestroll Garden')
        logger.info('---')
        await self.bot.switch_map(y_list=568/1080, world='the_xianzhou_luofu', scroll_down=True, # Locufox Forest Backdoor
                                    x=578/2400, y=284/1080, move_x=0, move_y=1, corner='botleft', confirm=False)
        await self.bot.move(1.5, 4400)
        await self.bot.move(1.95, 600)
        await self.bot.attack_technique(3) # -2TP
        await self.bot.move(1.0, 1000)
        await self.bot.move(1.2, 500)
        await self.bot.attack_technique(4) # -1TP
    async def path_1(self): # roamer
        logger_set_path(self.map, 1)
        await self.bot.use_teleporter(697/2400, 153/1080, move_x=0, move_y=0) # Path of Darkness
        await self.bot.move(1.8, 1800)
        await self.bot.attack() # +2TP
        await self.bot.move(1.8, 800)
        await self.bot.move(0.1, 2100)
        await self.bot.move(1.75, 2600)
        await self.bot.move(0.25, 300)
        await self.bot.attack_technique(8) # -1TP
    async def path_2(self):
        logger_set_path(self.map, 2)
        await self.bot.use_teleporter(697/2400, 153/1080, move_x=0, move_y=0) # Path of Darkness
        await self.bot.move(1.8, 2300)
        await self.bot.move(1.9, 800)
        await self.bot.move(0.1, 1800)
        await self.bot.move(1.75, 2600)
        await self.bot.move(0.25, 3000)
        await self.bot.move(0.1, 2100)
        await self.bot.attack() # items
        await self.bot.move(0.7, 1900)
        await self.bot.attack_technique(3) # -2TP
    async def path_3(self):
        logger_set_path(self.map, 3)
        await self.bot.use_teleporter(510/2400, 423/1080, corner='botleft', move_x=0, move_y=0) # Shape of Perdition
        await self.bot.move(0.95, 2500)
        await self.bot.attack() # +2TP
    async def path_4(self):
        logger_set_path(self.map, 4)
        await self.bot.use_teleporter(412/2400, 603/1080, move_x=0, move_y=0) # Bud of Abundance
        await self.bot.move(1.49, 3900)
        await self.bot.attack_technique(2) # -1TP
    async def path_5(self):
        logger_set_path(self.map, 5) # roamer
        await self.bot.use_teleporter(412/2400, 603/1080, move_x=0, move_y=0) # Bud of Abundance
        await self.bot.move(0.9, 4000)
        await self.bot.move(1.2, 3000)
        await self.bot.attack_technique(8) # -1TP
    async def path_6(self):
        logger_set_path(self.map, 6)
        await self.bot.use_teleporter(931/2400, 383/1080, corner='botright', move_x=0, move_y=0) # Verdant Terrace Entrance
        await self.bot.move(0.75, 3400)
        await self.bot.move(1.0, 1500)
        await self.bot.move(0.75, 3100)
        await self.bot.move(1.25, 5900)
        await self.bot.attack() # +2TP
    async def path_7(self):
        logger_set_path(self.map, 7)
        await self.bot.use_teleporter(577/2400, 285/1080, corner='botleft', move_x=0, move_y=1) # Locufox Forest Backdoor
        await self.bot.move(0.5, 2500)
        await self.bot.move(0.25, 2000)
        await self.bot.move(0.75, 2000)
        await self.bot.move(0.5, 2000)
        await self.bot.move(0.4, 1500)
        await self.bot.attack_technique(3) # -2TP
    async def path_8(self):
        logger_set_path(self.map, 8)
        await self.bot.use_teleporter(412/2400, 603/1080, move_x=0, move_y=0)  # Bud of Abundance
        await self.bot.move(1.47, 5000)
        await self.bot.move(1.2, 2000)
        await self.bot.move(0.9, 1500)
        await self.bot.move(1.12, 2300)
        await self.bot.attack() # +2TP
        await self.bot.sleep(0.5)
        await self.bot.move(1.2, 1500)
        await self.bot.move(0.7, 1000)
        await self.bot.attack_technique(4) # -2TP


