from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra


class Artisanship_Commission:
    def __init__(self, device):
        self.map = 'Artisanship Commission'
        self.bot = Bot(device)
        self.extra = Extra(device)
    async def farm(self):
        await self.teleport()
        await self.path_1()
        await self.path_2()
        await self.path_3()
        await self.extra.restore_tp(tp=4)
        await self.path_4()
        await self.path_5()
        await self.path_6()
        await self.extra.restore_tp(tp=4)
        await self.path_7()
        await self.path_8()
    async def teleport(self):
        logger_set_path(self.map, 'Teleport')
        logger.info('---')
        logger.info('--- Map: Artisanship Commission')
        logger.info('---')
        await self.bot.switch_map(y_list=446/1080, world='the_xianzhou_luofu', scroll_down=True, # Passage of the Finery Foundry
                                    x=933/2400, y=530/1080, corner='topright', move_x=0, move_y=4)
        await self.bot.move(0.5, 5200)
        await self.bot.move(0.0, 6200)
        await self.bot.move(0.25, 700)
        await self.bot.move(0.1, 500)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.move(0.0, 500)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.move(1.25, 700)
        await self.bot.attack_technique(3) # -1TP
        await self.bot.move(1.25, 300)
        await self.bot.attack_technique(4) # +2TP
    async def path_1(self):
        logger_set_path(self.map, 1)
        await self.bot.use_teleporter(933/2400, 530/1080, corner='topright', move_x=0, move_y=4) # Passage of the Finery Foundry
        await self.bot.move(0.5, 4100)
        await self.bot.move(0.25, 2500)
        await self.bot.attack() # items
        await self.bot.move(1.0, 1800)
        await self.bot.move(0.5, 3500)
        await self.bot.move(1.0, 1000)
        await self.bot.move(1.5, 300)
        await self.bot.attack_technique(5) # -1TP
    async def path_2(self):
        logger_set_path(self.map, 2)
        await self.bot.use_teleporter(933/2400, 530/1080, corner='topright', move_x=0, move_y=4) # Passage of the Finery Foundry
        await self.bot.move(0.5, 10900)
        await self.bot.move(0.0, 3900)
        await self.bot.move(0.55, 2300)
        await self.bot.move(0.8, 150)
        await self.bot.attack() # items
        await self.bot.move(0.25, 500)
        await self.bot.move(0.5, 2800)
        await self.bot.move(0.0, 2200)
        await self.bot.attack() # items
        await self.bot.move(1.1, 500)
        await self.bot.move(1.5, 100)
        await self.bot.attack_technique(5) # -1TP
    async def path_3(self):
        logger_set_path(self.map, 3)
        await self.bot.use_teleporter(854/2400, 418/1080, corner='botright', move_x=0, move_y=4) # Creation Furnace
        await self.bot.move(1.0, 1100)
        await self.bot.move(1.5, 900)
        await self.bot.move(0.0, 1900)
        await self.bot.move(0.5, 2800)
        await self.bot.move(0.2, 2100)
        await self.bot.attack() # +2TP
        await self.bot.move(1.5, 1600)
        await self.bot.move(0.0, 1400)
        await self.bot.move(0.25, 1000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.3, 500)
        await self.bot.move(1.5, 4600)
        await self.bot.move(0.0, 500)
        await self.bot.attack_technique(2) # -3TP, roamer
        for _ in range(8):
            await self.bot.move(0.0, 300)
            await self.bot.attack_technique(1)
        for _ in range(3):
            await self.bot.move(0.5, 300)
            await self.bot.attack_technique(1)
        for _ in range(6):
            await self.bot.move(0.9, 300)
            await self.bot.attack_technique(1)
        for _ in range(6):
            await self.bot.move(1.9, 300)
            await self.bot.attack_technique(1)
    async def path_4(self):
        logger_set_path(self.map, 4)
        await self.bot.switch_map(y_list=446/1080, world='the_xianzhou_luofu', scroll_down=True, # Passage to the Sapientia Academe
                                    x=894/2400, y=610/1080, corner='topleft', move_x=0, move_y=2)
        await self.bot.move(1.25, 3100)
        await self.bot.move(1.0, 8000)
        await self.bot.move(0.75, 200)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.move(1.5, 800)
        await self.bot.attack_technique(5) # -2TP
        await self.bot.move(1.25, 2500)
        await self.bot.posfix(1.25, 1000)
        await self.bot.move(0.25, 500)
        await self.bot.move(0.5, 600)
        await self.bot.move(1.0, 4600)
        await self.bot.move(0.5, 8350)
        await self.bot.move(1.0, 3600)
        await self.bot.attack() # +2TP
        await self.bot.move(1.0, 500)
        await self.bot.move(1.4, 2000)
        await self.bot.posfix(1.25, 1000)
        await self.bot.move(0.2, 500)
        await self.bot.move(1.5, 5200)
        await self.bot.move(0.0, 300)
        await self.bot.attack_technique(3) # -2TP
        for _ in range(3):
            await self.bot.move(1.5, 300)
            await self.bot.attack_technique(1)
        for _ in range(6):
            await self.bot.move(0.25, 300)
            await self.bot.attack_technique(1)
    async def path_5(self):
        logger_set_path(self.map, 5)
        await self.bot.use_teleporter(804/2400, 487/1080, corner='topleft', move_x=0, move_y=5) # Shape of Puppetry
        await self.bot.move(1.22, 2100)
        await self.bot.attack() # +2TP
    async def path_6(self):
        logger_set_path(self.map, 6)
        await self.bot.use_teleporter(854/2400, 418/1080, corner='botright', move_x=0, move_y=4) # Creation Furnace
        await self.bot.move(1.0, 1100)
        await self.bot.move(1.5, 900)
        await self.bot.move(0.00, 1800)
        await self.bot.move(0.5, 2500)
        await self.bot.move(0.00, 3300)
        await self.bot.move(1.5, 3000)
        await self.bot.move(1.75, 1000)
        await self.bot.move(0.25, 4500)
        await self.bot.move(0.5, 5700)
        await self.bot.move(1.05, 1000)
        await self.bot.move(1.25, 100)
        await self.bot.attack_technique(3) # -2TP
        await self.bot.move(0.25, 700)
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(6) # -1TP
    async def path_7(self):
        logger_set_path(self.map, 7)
        await self.bot.switch_map(y_list=446/1080, world='the_xianzhou_luofu', scroll_down=True, # Passage to the Sapientia Academe
                                    x=894/2400, y=610/1080, corner='topleft', move_x=0, move_y=2)
        await self.bot.move(1.25, 3100)
        await self.bot.move(1.0, 8000)
        await self.bot.move(1.4, 1400)
        await self.bot.move(1.0, 4700)
        await self.bot.move(0.57, 3800)
        await self.bot.attack() # items
        await self.bot.move(1.4, 2100)
        await self.bot.move(1.0, 300)
        await self.bot.attack_technique(12) # -1TP
        await self.bot.move(1.5, 1000)
        await self.bot.move(1.2, 2000)
        await self.bot.posfix(1.25, 1000)
        await self.bot.move(0.5, 400)
        await self.bot.move(0.8, 800)
        await self.bot.move(0.5, 200)
        await self.bot.attack() # items
        await self.bot.move(0.2, 1000)
        await self.bot.move(0.4, 1000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.2, 1500)
        await self.bot.move(1.0, 3300)
        await self.bot.move(0.5, 2500)
        await self.bot.move(0.83, 900)
        await self.bot.attack() # items
        await self.bot.move(0.5, 900)
        await self.bot.move(1.0, 1500)
        await self.bot.move(0.4, 1500)
        await self.bot.move(0.25, 1000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.2, 3500)
        await self.bot.move(1.0, 600)
        await self.bot.attack_technique(3) # items
        for _ in range(4): # -3TP, roamer
            await self.bot.move(1.0, 300)
            await self.bot.attack_technique(2)
        for _ in range(3):
            await self.bot.move(0.75, 300)
            await self.bot.attack_technique(2)
        for _ in range(3):
            await self.bot.move(1.5, 300)
            await self.bot.attack_technique(2)
        await self.bot.move(1.2, 1000)
        await self.bot.move(1.4, 1500)
        await self.bot.posfix(1.25, 1000)
        await self.bot.move(0.2, 3100)
        await self.bot.attack() # +2TP
    async def path_8(self):
        logger_set_path(self.map, 8)
        await self.bot.use_teleporter(894/2400, 610/1080, corner='topleft', move_x=0, move_y=2) # Passage to the Sapientia Academe
        await self.bot.move(0.5, 4400)
        await self.bot.move(0.75, 1700)
        await self.bot.attack() # +2TP
        await self.bot.move(0.1, 1600)
        await self.bot.move(0.5, 1600)
        await self.bot.attack_technique(2) # items
        await self.bot.move(1.7, 500)
        for _ in range(6): # -2TP
            await self.bot.move(0.0, 300)
            await self.bot.attack_technique(2)
        await self.bot.move(0.5, 1500)
        await self.bot.move(0.0, 1000)
        await self.bot.move(1.5, 2000)
        await self.bot.move(1.75, 1000)
        await self.bot.posfix(1.75, 1000)
        await self.bot.move(1.0, 1000)
        await self.bot.move(1.5, 1500)
        await self.bot.move(1.0, 4100)
        await self.bot.move(1.5, 900)
        await self.bot.move(1.65, 2200)
        for _ in range(3): # -1TP
            await self.bot.move(0.0, 300)
            await self.bot.attack_technique(1)
        await self.bot.move(1.5, 300)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(6)


