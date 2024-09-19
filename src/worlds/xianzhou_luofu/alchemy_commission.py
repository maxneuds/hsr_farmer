from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra
from datetime import datetime as dt


class Alchemy_Commission:
    def __init__(self, device):
        self.map = 'Alchemy Comission'
        self.bot = Bot(device)
        self.extra = Extra(device)
    async def farm(self):
        await self.teleport()
        await self.path_1()
        await self.path_2()
        await self.path_3()
        await self.path_4()
        await self.path_5()
        await self.extra.restore_tp(tp=4, info='Alchemy Comission')
        await self.path_6()
        await self.path_7()
        await self.path_8()
        await self.path_9()
        await self.path_10()
        await self.path_11()
    async def teleport(self):
        logger_set_path(self.map, 'Teleport')
        logger.info('---')
        logger.info('--- Map: Alchemy Comission')
        logger.info('---')
        await self.bot.switch_map(y_list=568/1080, world='the_xianzhou_luofu', scroll_down=True, # Healer's Market
                                    x=854/2400, y=689/1080, corner='topright', move_x=0, move_y=6, confirm=True)
        await self.bot.move(0.5, 1500)
        await self.bot.move(0.75, 6700)
        await self.bot.move(0.98, 6000)
        await self.bot.attack() # items
        await self.bot.move(1.2, 4000)
        await self.bot.move(1.1, 4500)
        await self.bot.attack_technique(5) # -2TP
        await self.bot.move(1.6, 300)
        await self.bot.attack_technique(8) # -1TP
    async def path_1(self):
        logger_set_path(self.map, 1)
        await self.bot.use_teleporter(854/2400, 689/1080, corner='topright', move_x=0, move_y=6, confirm=True) # Healer's Market
        await self.bot.move(1.4, 4600)
        await self.bot.move(1.9, 2100)
        await self.bot.attack() # +2TP
        await self.bot.move(0.25, 1000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.2, 1000)
        await self.bot.move(0.9, 2800)
        await self.bot.move(1.4, 7400)
        await self.bot.move(0.0, 1400)
        await self.bot.attack() # items
        await self.bot.move(1.65, 1000)
        await self.bot.posfix(1.65, 1000)
        await self.bot.move(1.0, 1000)
        await self.bot.move(1.5, 1500)
        await self.bot.move(1.8, 600)
        await self.bot.attack_technique(6) # -1TP
        await self.bot.move(1.7, 300)
        await self.bot.attack_technique(4) # -1TP
    async def path_2(self):
        logger_set_path(self.map, 2)
        await self.bot.use_teleporter(659/2400, 363/1080, corner='botright', move_x=0, move_y=0) # Cavern of Corrosion
        await self.bot.move(1.5, 2800)
        await self.bot.move(1.2, 1600)
        await self.bot.attack() # +2TP
        await self.bot.move(1.75, 2000)
        for _ in range(3): # -1TP, roamer
            await self.bot.move(1.25, 300)
            await self.bot.attack_technique(2)
        await self.bot.move(0.25, 1000)
        await self.bot.move(1.5, 1000)
        await self.bot.move(1.25, 1000)
        await self.bot.posfix(1.25, 1000)
        await self.bot.move(0.4, 2000)
        await self.bot.move(0.65, 1300)
        await self.bot.attack() # items
        await self.bot.move(1.6, 2300)
        await self.bot.move(1.25, 300)
        await self.bot.attack_technique(12) # -1TP
    async def path_3(self):
        logger_set_path(self.map, 3)
        await self.bot.use_teleporter(867/2400, 646/1080, corner='topleft', move_x=0, move_y=4) # Elixir Research Terrace
        await self.bot.move(0.5, 10300)
        await self.bot.move(0.75, 2000)
        await self.bot.move(1.1, 2200)
        await self.bot.attack() # +2TP
        await self.bot.move(0.0, 600)
        await self.bot.move(1.5, 4400)
        await self.bot.move(1.0, 1300)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(3)
        await self.bot.move(0.25, 300)
        await self.bot.attack_technique(4) # -1TP
    async def path_4(self):
        logger_set_path(self.map, 4)
        await self.bot.use_teleporter(867/2400, 646/1080, corner='topleft', move_x=0, move_y=4) # Elixir Research Terrace
        await self.bot.move(0.5, 6900)
        await self.bot.move(0.0, 3600)
        await self.bot.move(1.5, 3700)
        await self.bot.move(0.0, 4200)
        await self.bot.attack_technique(2) # -1TP
    async def path_5(self):
        logger_set_path(self.map, 5)
        await self.bot.use_teleporter(1003/2400, 595/1080, corner='topleft', move_x=0, move_y=3) # Aureate Elixir Furnace
        await self.bot.move(0.8, 700)
        await self.bot.attack() # +2TP
        await self.bot.move(0.1, 500)
        await self.bot.move(0.55, 2200)
        await self.bot.move(0.34, 2300)
        await self.bot.move(0.2, 1300)
        await self.bot.move(0.5, 1200)
        await self.bot.move(0.35, 2000)
        await self.bot.move(0.14, 2700)
        await self.bot.attack_technique(1) # -2TP
        for _ in range(2):
            await self.bot.move(1.64, 300)
            await self.bot.attack_technique(1)
        for _ in range(3):
            await self.bot.move(0.14, 300)
            await self.bot.attack_technique(1)
        for _ in range(3):
            await self.bot.move(0.64, 300)
            await self.bot.attack_technique(1)
        for _ in range(3):
            await self.bot.move(1.14, 300)
            await self.bot.attack_technique(1)
        for _ in range(2):
            await self.bot.move(1.64, 300)
            await self.bot.attack_technique(1)
    async def path_6(self):
        logger_set_path(self.map, 6)
        await self.bot.switch_map(y_list=568/1080, world='the_xianzhou_luofu', scroll_down=True, # Aureate Elixir Furnace
                                    x=1003/2400, y=595/1080, corner='topleft', move_x=0, move_y=3)
        await self.bot.move(0.54, 3200)
        await self.bot.move(0.33, 2500)
        await self.bot.move(0.1, 1000)
        await self.bot.move(0.6, 1000)
        await self.bot.move(0.33, 2600)
        await self.bot.move(0.13, 3000)
        await self.bot.move(1.85, 1000)
        await self.bot.move(0.15, 1000)
        await self.bot.move(0.13, 3100)
        await self.bot.move(1.82, 1500)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.move(1.32, 300)
        await self.bot.attack_technique(2) # -1TP
        for _ in range(3):
            await self.bot.move(1.82, 300)
            await self.bot.attack_technique(1)
        for _ in range(3):
            await self.bot.move(0.32, 300)
            await self.bot.attack_technique(1)
        for _ in range(3):
            await self.bot.move(0.82, 300)
            await self.bot.attack_technique(1)
        for _ in range(3):
            await self.bot.move(1.32, 300)
            await self.bot.attack_technique(1)
        for _ in range(2):
            await self.bot.move(1.82, 300)
            await self.bot.attack_technique(1)
    async def path_7(self):
        logger_set_path(self.map, 7)
        await self.bot.use_teleporter(583/2400, 241/1080, corner='botright', move_x=0, move_y=3) # Bud of Nihility
        await self.bot.move(1.0, 1500)
        await self.bot.move(0.5, 4200)
        await self.bot.move(0.7, 1800)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.move(0.8, 1500)
        await self.bot.posfix(0.75, 1000)
        await self.bot.move(0.0, 1000)
        await self.bot.move(0.28, 1300)
        await self.bot.attack() # items
        await self.bot.move(1.55, 1200)
        await self.bot.move(1.7, 1500)
        await self.bot.move(1.4, 1000)
        await self.bot.move(1.5, 6000)
        await self.bot.move(0.0, 4800)
        await self.bot.move(1.8, 600)
        await self.bot.attack() # +2TP
    async def path_8(self):
        logger_set_path(self.map, 8)
        await self.bot.use_teleporter(583/2400, 241/1080, corner='botright', move_x=0, move_y=3) # Bud of Nihility
        await self.bot.move(1.0, 2600)
        await self.bot.move(0.5, 3100)
        await self.bot.move(1.0, 3400)
        await self.bot.move(1.4, 1900)
        await self.bot.move(1.1, 300)
        await self.bot.attack() # items
        for _ in range(8): # -3TP
            await self.bot.move(1.15, 300)
            await self.bot.attack_technique(1)
        for _ in range(6):
            await self.bot.move(0.35, 300)
            await self.bot.attack_technique(1)
        await self.bot.move(1.7, 800)
        await self.bot.move(1.5, 300)
        await self.bot.attack_technique(16)
    async def path_9(self):
        logger_set_path(self.map, 9)
        await self.bot.use_teleporter(1355/2400, 351/1080, corner='botright', move_x=0, move_y=5) # Shape of Celestial
        await self.bot.move(1.66, 2500)
        await self.bot.attack() # +2TP
    async def path_10(self):
        logger_set_path(self.map, 10)
        await self.bot.use_teleporter(583/2400, 241/1080, corner='botright', move_x=0, move_y=3) # Bud of Nihility
        await self.bot.move(1.0, 2600)
        await self.bot.move(0.5, 3100)
        await self.bot.move(1.0, 3500)
        await self.bot.move(1.1, 4000)
        await self.bot.move(1.5, 3600)
        await self.bot.move(1.0, 3000)
        await self.bot.move(0.5, 500)
        await self.bot.attack_technique(13) # move
        await self.bot.move(1.0, 500)
        await self.bot.attack_technique(3) # +2TP
    async def path_11(self):
        logger_set_path(self.map, 11)
        await self.bot.use_teleporter(1003/2400, 595/1080, corner='topleft', move_x=0, move_y=3) # Aureate Elixir Furnace
        await self.bot.move(0.54, 3200)
        await self.bot.move(0.33, 2500)
        await self.bot.move(0.1, 1000)
        await self.bot.move(0.6, 1000)
        await self.bot.move(0.33, 2600)
        await self.bot.move(0.13, 3000)
        await self.bot.move(1.85, 1000)
        await self.bot.move(0.15, 1000)
        await self.bot.move(0.13, 3100)
        await self.bot.move(1.82, 2500)
        await self.bot.move(1.55, 2000)
        await self.bot.move(1.35, 3000)
        await self.bot.move(1.55, 5000)
        await self.bot.move(1.25, 3000)
        await self.bot.move(1.1, 2200)
        await self.bot.attack_technique(3) # -3TP
        await self.bot.move(1.7, 300)
        await self.bot.attack_technique(1)
        await self.bot.move(0.6, 300)
        await self.bot.attack_technique(5)


