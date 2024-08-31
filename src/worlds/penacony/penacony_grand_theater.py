from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra


class Penacony_Grand_Theater:
    def __init__(self, device):
        self.map = 'Penacony Grand Theater'
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
        await self.path_9()
        await self.path_10()
        await self.path_x()
    async def teleport(self): # 1->3
        logger_set_path(self.map, 'Teleport')
        logger.info('---')
        logger.info('--- Map: Penacony Grand Theater')
        logger.info('---')
        await self.bot.switch_map(y_list=807/1080, world='penacony', scroll_down=True, # Echo of War
                                    x=787/2400, y=717/1080, corner='topleft', move_x=3, move_y=7)
        await self.bot.move(0.12, 1800)
        await self.bot.attack() # +2TP
    async def path_1(self):
        logger_set_path(self.map, 1)
        await self.bot.use_teleporter(966/2400, 763/1080, move_x=1, move_y=6, swipe=2, corner='topleft') # Hall of Chords
        await self.bot.move(0.31, 2200)
        await self.bot.attack() # +2TP
        await self.bot.move(1.6, 1000)
        await self.bot.move(0.1, 2500)
        await self.bot.attack() # items
        await self.bot.move(1.6, 500)
        await self.bot.move(0.1, 4000)
        await self.bot.move(0.25, 2500)
        await self.bot.move(0.4, 500)
        await self.bot.attack() # items
        await self.bot.move(0.25, 300)
        await self.bot.attack_technique(4) # -2TP
        await self.bot.move(0.6, 1500)
        await self.bot.posfix(0.6, 1000)
        await self.bot.move(1.7, 1000)
        await self.bot.move(0.35, 5000)
        await self.bot.move(0.5, 1500)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.move(0.8, 300)
        await self.bot.attack_technique(4) # -1TP
    async def path_2(self): # 1->3
        logger_set_path(self.map, 2)
        await self.bot.use_teleporter(1251/2400, 469/1080, move_x=0, move_y=8, swipe=2, corner='botright') # Communing Hall
        await self.bot.move(1.4, 3000)
        await self.bot.move(1.5, 1000)
        await self.bot.attack() # items
        await self.bot.move(1.6, 4500)
        await self.bot.move(0.1, 1600)
        await self.bot.attack() # +2TP
    async def path_3(self):
        logger_set_path(self.map, 3)
        await self.bot.use_teleporter(1251/2400, 469/1080, move_x=0, move_y=8, swipe=2, corner='botright') # Communing Hall
        await self.bot.move(0.62, 2400)
        await self.bot.attack(2) # items
        await self.bot.move(0.0, 2100)
        await self.bot.attack() # items
        await self.bot.move(0.7, 5000)
        await self.bot.move(0.5, 700)
        await self.bot.attack(2) # items
    async def path_4(self): # 3->3
        logger_set_path(self.map, 4)
        await self.bot.use_teleporter(1251/2400, 469/1080, move_x=0, move_y=8, swipe=2, corner='botright') # Communing Hall
        await self.bot.move(0.5, 6000)
        await self.bot.move(0.4, 8000)
        for _ in range(3): # -1TP
            await self.bot.move(0.3, 300)
            await self.bot.attack_technique(2)
        for _ in range(2): # +2TP
            await self.bot.move(1.9, 300)
            await self.bot.attack_technique(2)
        for _ in range(2): # -1TP
            await self.bot.move(0.9, 300)
            await self.bot.attack_technique(4)
    async def path_5(self): # 3 -> 
        logger_set_path(self.map, 5)
        await self.bot.use_teleporter(635/2400, 388/1080, move_x=0, move_y=9, swipe=1, corner='botright') # Ascension Hallway
        await self.bot.move(0.3, 900)
        await self.bot.move(0.0, 4200)
        await self.bot.move(1.9, 900)
        await self.bot.move(0.0, 500)
        await self.bot.attack() # +2TP
        await self.bot.move(0.3, 500)
        for _ in range(2):
            await self.bot.move(0.1, 300)
            await self.bot.attack_technique(2)
        await self.bot.move(1.5, 300)
        await self.bot.attack_technique(4) # -1TP
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(6)
        await self.bot.move(1.7, 300)
        await self.bot.attack_technique(6) # -1TP
    async def path_6(self):
        logger_set_path(self.map, 6)
        await self.bot.use_teleporter(635/2400, 388/1080, move_x=0, move_y=9, swipe=1, corner='botright') # Ascension Hallway
        await self.bot.move(0.62, 300)
        await self.bot.attack_technique(5) # items
        await self.bot.move(0.3, 500)
        await self.bot.move(0.5, 2000)
        await self.bot.move(0.6, 300)
        await self.bot.attack_technique(2) # +2TP
        await self.bot.move(0.25, 300)
        await self.bot.attack_technique(5) # items
        await self.bot.move(1.0, 1000)
        await self.bot.move(0.6, 300)
        await self.bot.attack_technique(7) # items
        await self.bot.move(0.25, 300)
        await self.bot.attack_technique(5) # items
        await self.bot.move(0.69, 300)
        await self.bot.attack_technique(6) # items
        await self.bot.move(0.33, 300)
        await self.bot.attack_technique(6) # items
    async def path_7(self):
        logger_set_path(self.map, 7)
        await self.bot.use_teleporter(900/2400, 184/1080, move_x=0, move_y=9, swipe=2, corner='botright') # Bud of Erdutition
        await self.bot.move(1.5, 1200)
        await self.bot.attack_technique(1) # items
        await self.bot.move(1, 1500)
        await self.bot.move(0.83, 2500)
        await self.bot.attack_technique(1) # items
        await self.bot.move(1.3, 300)
        await self.bot.attack_technique(9) # -1TP
    async def path_8(self):
        logger_set_path(self.map, 8)
        await self.bot.use_teleporter(900/2400, 184/1080, move_x=0, move_y=9, swipe=2, corner='botright') # Bud of Erdutition
        await self.bot.move(1.37, 500)
        await self.bot.attack_technique(19) # -1TP
    async def path_9(self):
        logger_set_path(self.map, 9)
        await self.bot.use_teleporter(1000/2400, 274/1080, move_x=1, move_y=7, swipe=2, corner='botright') # Hall of Chords
        await self.bot.move(0.9, 3500)
        await self.bot.move(0.7, 1000)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.move(1.0, 2000)
        await self.bot.move(0.9, 1000)
        await self.bot.move(0.7, 1600)
        await self.bot.attack_technique(2) # +2TP
        await self.bot.move(0.75, 2000)
        await self.bot.posfix(0.75, 1000)
        await self.bot.move(1.4, 2000)
        await self.bot.move(0.9, 2000)
        await self.bot.move(0.7, 1000)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.move(0.6, 300)
        await self.bot.attack_technique(3) # items
    async def path_10(self):
        logger_set_path(self.map, 10)
        await self.bot.use_teleporter(599/2400, 322/1080, move_x=0, move_y=8, swipe=2, corner='botleft') # Cavern of Corrosion
        await self.bot.move(1.3, 1400)
        await self.bot.attack_technique(1) # +2TP
        await self.bot.move(0.1, 500)
        await self.bot.attack_technique(6) # items
        await self.bot.move(0.25, 1000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.5, 1000)
        await self.bot.move(1.8, 7000)
        await self.bot.posfix(1.8, 1000)
        await self.bot.move(1.5, 1000)
        await self.bot.move(1.85, 1500)
        await self.bot.attack_technique(2) # items
        # END: 5TP
    async def path_x(self):
        logger_set_path(self.map, 11)
        await self.bot.use_teleporter(787/2400, 717/1080, corner='topleft', move_x=3, move_y=7) # Echo of War
        # TODO: 4 to the left
    async def path_z(self):
        logger_set_path(self.map, 11)
        await self.bot.use_teleporter(671/2400, 526/1080, move_x=0, move_y=8, swipe=2, corner='botleft') # Saloon of Gospels
        # TODO: +2TP bot, teleport back, go into dream (1), -2TP


