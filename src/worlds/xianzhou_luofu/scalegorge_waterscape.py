from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra


class Scalegorge_Waterscape:
    def __init__(self, device):
        self.map = 'Scalegorge Waterscape'
        self.bot = Bot(device)
    async def farm(self):
        await self.teleport()
        await self.path_1()
        await self.path_2()
        await self.path_3()
        await self.path_4()
        await self.path_5()
        await self.path_6()
        await self.path_7()
        await self.path_8()
    async def teleport(self):
        logger_set_path(self.map, 'Teleport')
        logger.info('---')
        logger.info('--- Map: Scalegorge Waterscape')
        logger.info('---')
        await self.bot.switch_map(y_list=807/1080, world='the_xianzhou_luofu', scroll_down=True, # Dragonvista Rain Hall
                                    x=966/2400, y=379/1080, corner='botright', move_x=0, move_y=0)
        await self.bot.move(1.5, 4000)
        await self.bot.move(1.7, 2900)
        await self.bot.attack() # items
        await self.bot.move(0.4, 4500)
        await self.bot.move(0.1, 2900)
        await self.bot.attack_technique(4) # -3TP
        await self.bot.move(1.3, 300)
        await self.bot.attack_technique(4)
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(4)
    async def path_1(self):
        logger_set_path(self.map, 1)
        await self.bot.use_teleporter(357/2400, 354/1080, move_x=0, move_y=0) # Ancient Sea Palace Ruins
        await self.bot.move(0.75, 900)
        await self.bot.attack() # items
        await self.bot.move(1.75, 1200)
        await self.bot.move(1.5, 8000)
        await self.bot.move(0.0, 1000)
        await self.bot.attack() # +2TP
        await self.bot.posfix(1.70, 1300)
        await self.bot.attack() # items
    async def path_2(self):
        logger_set_path(self.map, 2)
        await self.bot.use_teleporter(357/2400, 354/1080, move_x=0, move_y=0) # Ancient Sea Palace Ruins
        await self.bot.move(1.0, 4900)
        await self.bot.move(1.3, 2100)
        await self.bot.attack() # items
        await self.bot.move(1.0, 1000)
        await self.bot.move(0.9, 2000)
        for _ in range(9): # -3TP, roamer
            await self.bot.move(1.0, 300)
            await self.bot.attack_technique(1)
        for _ in range(4):
            await self.bot.move(0.5, 300)
            await self.bot.attack_technique(1)
        await self.bot.move(1.7, 300)
    async def path_3(self):
        logger_set_path(self.map, 3)
        await self.bot.use_teleporter(1433/2400, 659/1080, corner='topleft', move_x=0, move_y=0) # Palace Ruin Depthsck
        await self.bot.move(1.3, 1200)
        await self.bot.attack() # items
        await self.bot.move(1.5, 2000)
        await self.bot.move(1.0, 2500)
        await self.bot.move(1.5, 2900)
        await self.bot.move(1.13, 2000)
        await self.bot.attack() # +2TP
        await self.bot.move(0.75, 2000)
        await self.bot.posfix(0.75, 1000)
        await self.bot.move(1.75, 600)
        await self.bot.move(0.0, 2100)
        await self.bot.move(0.5, 2400)
        await self.bot.move(1.0, 6500)
        await self.bot.move(0.7, 1300)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.move(0.75, 1000)
        await self.bot.move(1.0, 2000)
        await self.bot.posfix(0.75, 1000)
        await self.bot.move(1.6, 1000)
        await self.bot.move(1.5, 1000)
        await self.bot.move(1.0, 1900)
        await self.bot.move(0.5, 1200)
        await self.bot.attack() # items
        await self.bot.move(0.25, 500)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.2, 1000)
        await self.bot.move(1.5, 300)
        await self.bot.attack_technique(21) # -1TP, roamer
    async def path_4(self):
        logger_set_path(self.map, 4)
        await self.bot.use_teleporter(1465/2400, 341/1080, corner='topleft', move_x=0, move_y=0) # Shape of Abomination
        await self.bot.move(1.5, 4000)
        await self.bot.move(1.0, 1000)
        await self.bot.attack() # +2TP
        await self.bot.move(0.7, 1000)
        await self.bot.move(0.5, 1000)
        await self.bot.move(0.7, 5000)
        await self.bot.move(0.5, 500)
        await self.bot.move(0.75, 1000)
        await self.bot.posfix(0.75, 1000)
        await self.bot.move(1.5, 1900)
        await self.bot.move(1.0, 4500)
        await self.bot.move(1.1, 900)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.move(1.6, 300)
        await self.bot.attack_technique(1)
        await self.bot.move(1.5, 300)
        await self.bot.attack_technique(4) # -1TP
    async def path_5(self):
        logger_set_path(self.map, 5)
        await self.bot.use_teleporter(909/2400, 690/1080, corner='topleft', move_x=0, move_y=0) # Divine Seed
        await self.bot.move(1.0, 2000)
        await self.bot.move(1.1, 2500)
        await self.bot.move(1.5, 1500)
        await self.bot.move(1.0, 2000)
        await self.bot.attack() # +2TP
        await self.bot.move(0.0, 2100)
        await self.bot.move(0.5, 1500)
        await self.bot.move(1.0, 8500)
        await self.bot.move(1.25, 2300)
        await self.bot.move(1.0, 1600)
        await self.bot.move(0.75, 3000)
        await self.bot.posfix(0.75, 1000)
        await self.bot.move(1.75, 1000)
        await self.bot.move(0.5, 3000)
        await self.bot.move(0.6, 2000)
        await self.bot.move(0.5, 3900)
        for _ in range(2): # -2TP, roamer
            await self.bot.move(0.5, 300)
            await self.bot.attack_technique(1)
        for _ in range(6):
            await self.bot.move(0.8, 300)
            await self.bot.attack_technique(1)
        for _ in range(4):
            await self.bot.move(0.0, 300)
            await self.bot.attack_technique(1)
        await self.bot.attack_technique(7)
    async def path_6(self):
        logger_set_path(self.map, 6)
        await self.bot.use_teleporter(1433/2400, 659/1080, corner='topleft', move_x=0, move_y=0) # Palace Ruin Depths
        await self.bot.move(1.5, 6000)
        await self.bot.move(1.6, 300)
        await self.bot.attack() # +2TP
        await self.bot.sleep(0.5)
        await self.bot.move(0.5, 3600)
        await self.bot.move(0.0, 300)
        await self.bot.attack_technique(12) # -1TP
        await self.bot.move(1.5, 300)
        await self.bot.attack_technique(4) # -1TP
    async def path_7(self):
        logger_set_path(self.map, 7)
        await self.bot.use_teleporter(1465/2400, 341/1080, corner='topleft', move_x=0, move_y=0) # Shape of Abomination
        await self.bot.move(1.0, 1600)
        await self.bot.move(0.75, 1600)
        await self.bot.move(1.0, 5000)
        await self.bot.move(1.1, 1000)
        await self.bot.move(1.0, 2000)
        await self.bot.move(1.5, 4000)
        await self.bot.move(1.4, 1700)
        await self.bot.move(1.6, 1200)
        await self.bot.move(1.8, 800)
        await self.bot.attack() # +2TP
    async def path_8(self):
        logger_set_path(self.map, 8)
        await self.bot.use_teleporter(1433/2400, 659/1080, corner='topleft', move_x=0, move_y=0) # Palace Ruin Depths
        await self.bot.move(1.5, 3000)
        await self.bot.move(0.0, 3600)
        await self.bot.move(1.5, 6000)
        await self.bot.move(1.25, 500)
        for _ in range(3): # -2TP, roamer
            await self.bot.move(1.5, 300)
            await self.bot.attack_technique(2)
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(3)
        await self.bot.move(0.25, 300)
        await self.bot.attack_technique(6) # items
    

