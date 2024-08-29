from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.universal import Init as Universal


class Stargazer_Navalia:
    def __init__(self, device):
        self.bot = Bot(device)
        self.universal = Universal(device)
    async def farm(self):
        await self.teleport()
        await self.path_1()
        await self.path_2()
        await self.path_3()
        await self.path_4()
        await self.path_5()
        await self.path_6()
        await self.universal.restore_tp(tp=4)
        await self.path_7()
    async def teleport(self):
        logger_set_path('Teleport')
        logger.info('---')
        logger.info('--- Map: Stargazer Navalia')
        logger.info('---')
        await self.bot.switch_map(y_list=630/1080, world='the_xianzhou_luofu', scroll_down=False, # Path of Conflagration
                                    x=768/2400, y=696/1080, corner='topright', move_x=0, move_y=0)
        await self.bot.move(1.7, 3300)
        await self.bot.move(1.9, 300)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.move(0.4, 1800)
        await self.bot.attack() # +2TP
    async def path_1(self):
        logger_set_path(1)
        await self.bot.use_teleporter(855/2400, 405/1080, move_x=0, move_y=2, corner='botleft') # Ship Nursery - The Budding
        await self.bot.move(0.7, 800)
        await self.bot.move(0.5, 900)
        await self.bot.move(0.00, 2500)
        for _ in range(2): # -1TP, roamer
            await self.bot.move(0.5, 300)
            await self.bot.attack_technique(2)
        for _ in range(2):
            await self.bot.move(1.0, 300)
            await self.bot.attack_technique(2)
        await self.bot.move(1.5, 300)
        await self.bot.attack_technique(2)
        for _ in range(2):
            await self.bot.move(0.0, 300)
            await self.bot.attack_technique(2)
        for _ in range(2):
            await self.bot.move(0.5, 300)
            await self.bot.attack_technique(2)
    async def path_2(self):
        logger_set_path(2)
        await self.bot.use_teleporter(855/2400, 184/1080, move_x=0, move_y=0, corner='botleft') # Ship Nursery - The Budding
        await self.bot.move(1.5, 700)
        await self.bot.move(0.0, 2300)
        await self.bot.move(0.5, 800)
        await self.bot.attack() # +2TP
        await self.bot.move(1.5, 800)
        await self.bot.move(1.9, 500)
        await self.bot.move(0.00, 8300)
        await self.bot.attack_technique(4) # -2TP
        await self.bot.move(0.25, 1000)
        await self.bot.move(1.25, 1000)
        await self.bot.move(1.5, 300)
        await self.bot.attack_technique(10) # -1TP
    async def path_3(self):
        logger_set_path(3)
        await self.bot.use_teleporter(1106/2400, 610/1080, move_x=0, move_y=0, corner='botright') # Shape of Doom
        await self.bot.move(1.5, 700)
        await self.bot.attack() # +2TP
        await self.bot.posfix(1.5, 1000)
        await self.bot.move(0.3, 500)
        await self.bot.move(0.00, 5400)
        await self.bot.move(1.7, 600)
        await self.bot.move(0.0, 2550)
        for _ in range(3): # -1TP, roamer, +2TP
            await self.bot.move(0.5, 300)
            await self.bot.attack_technique(2)
        await self.bot.move(0.75, 2000)
        await self.bot.posfix(0.75, 1000)
        await self.bot.move(1.5, 1000)
        await self.bot.move(1.3, 1100)
        await self.bot.attack() # items
        await self.bot.move(0.3, 1600)
        await self.bot.move(0.0, 3100)
        await self.bot.move(1.7, 1300)
        await self.bot.attack() # items
    async def path_4(self):
        logger_set_path(4)
        await self.bot.use_teleporter(1240/2400, 538/1080, corner='topright', move_x=0, move_y=0) # Astral Cottage
        await self.bot.move(0.25, 2500)
        await self.bot.move(0.16, 6000)
        await self.bot.move(0.27, 700)
        await self.bot.move(0.52, 400)
        await self.bot.move(1.05, 2000)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.move(0.25, 1500)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.3, 900)
        await self.bot.move(1.11, 5000)
        await self.bot.move(1.17, 2700)
        await self.bot.move(0.6, 2800)
        for _ in range(4): # -2TP, roamer
            await self.bot.move(0.2, 300)
            await self.bot.attack_technique(3)
        for _ in range(3):
            await self.bot.move(1.2, 300)
            await self.bot.attack_technique(3)
        await self.bot.attack_technique(1)
    async def path_5(self):
        logger_set_path(5)
        await self.bot.use_teleporter(1240/2400, 538/1080, move_x=0, move_y=0, corner='topright', confirm=True) # Astral Cottage
        await self.bot.move(0.25, 2500)
        await self.bot.move(0.16, 6000)
        await self.bot.move(0.27, 700)
        await self.bot.move(0.52, 400)
        await self.bot.move(1.05, 2200)
        await self.bot.move(1.07, 5000)
        await self.bot.move(1.17, 2900)
        await self.bot.move(0.62, 3000)
        await self.bot.move(0.84, 4300)
        await self.bot.move(0.9, 100)
        await self.bot.attack() # +2TP
        await self.bot.move(0.15, 3100)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.move(0.15, 1500)
        await self.bot.move(0.4, 1500)
        await self.bot.move(0.25, 2000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.15, 4900)
        await self.bot.move(1.25, 300)
        await self.bot.attack_technique(2) # -1TP
    async def path_6(self):
        logger_set_path(6)
        await self.bot.use_teleporter(855/2400, 405/1080, move_x=0, move_y=2, corner='botleft') # Ship Nursery - The Budding
        await self.bot.move(0.7, 800)
        await self.bot.move(0.5, 900)
        await self.bot.move(0.0, 2000)
        await self.bot.move(0.2, 3000)
        await self.bot.move(0.3, 500)
        await self.bot.attack() # items
        await self.bot.move(1.1, 1200)
        await self.bot.move(1.0, 700)
        await self.bot.move(0.5, 3800)
        await self.bot.move(0.3, 1000)
        await self.bot.attack() # +2TP
        await self.bot.move(0.25, 1000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.25, 1900)
        await self.bot.move(1.0, 5500)
        await self.bot.move(0.9, 1500)
        await self.bot.attack() # items
        await self.bot.move(1.5, 2000)
        await self.bot.move(1.4, 1500)
        await self.bot.attack_technique(4) # -3TP
        await self.bot.move(0.3, 300)
        await self.bot.attack_technique(4)
    async def path_7(self):
        logger_set_path(7)
        await self.bot.switch_map(y_list=630/1080, world='the_xianzhou_luofu', scroll_down=False, # Ship Nursery - The Burgeoning
                                    x=958/2400, y=364/1080, corner='botleft', move_x=0, move_y=0)
        await self.bot.move(0.95, 1700)
        await self.bot.move(0.65, 1900)
        await self.bot.move(1.0, 1900)
        await self.bot.move(0.5, 1100)
        await self.bot.attack() # items
        await self.bot.move(1.5, 3000)
        await self.bot.move(1.0, 800)
        await self.bot.move(1.5, 2000)
        await self.bot.move(1.0, 1000)
        await self.bot.move(1.5, 1500)
        await self.bot.move(1.0, 1000)
        for _ in range(9): # -2TP, roamer
            await self.bot.move(1.5, 300)
            await self.bot.attack_technique(2)
        await self.bot.move(1.0, 2000)
        await self.bot.posfix(1.25, 1000)
        await self.bot.move(0.5, 3700)
        await self.bot.move(1.0, 4200)
        await self.bot.move(1.5, 1700)
        await self.bot.move(0.0, 300)
        await self.bot.attack_technique(3) # -1TP


