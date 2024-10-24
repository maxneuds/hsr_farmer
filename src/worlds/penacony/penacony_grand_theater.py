from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra
from datetime import datetime as dt


class Penacony_Grand_Theater:
    def __init__(self, device):
        self.map = 'Penacony Grand Theater'
        self.bot = Bot(device)
        self.extra = Extra(device)
    async def farm(self):
        t_start = dt.now()
        raise SystemExit('2.6 map change')
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
        await self.path_11()
        await self.path_12()
        await self.path_13()
        await self.path_14()
        await self.path_15()
        await self.path_16()
        # await self.extra.metrics(self.map, t_start)
    async def dev(self):
        pass
    async def teleport(self):
        logger_set_path(self.map, 'Teleport')
        logger.info('---')
        logger.info('--- Map: Penacony Grand Theater')
        logger.info('---')
        await self.bot.switch_map_new(world='penacony', y_list=807/1080, scroll_down=True, # Communing Hall
                                      x=1251/2400, y=383/1080, start=1.75, deg=0.5, n=4, confirm=False)
        await self.bot.move(0.62, 2400)
        await self.bot.attack(2) # items
        await self.bot.move(0.0, 2100)
        await self.bot.attack() # items
        await self.bot.move(0.7, 5000)
        await self.bot.move(0.5, 700)
        await self.bot.attack(2) # items
    async def path_1(self):
        logger_set_path(self.map, 1)
        await self.bot.teleport(x=636/2400, y=610/1080, start=1.75, deg=0.5, n=3) # Ascension Hallway
        await self.bot.move(1.5, 300)
        await self.bot.attack_technique(20) # -2TP
        await self.bot.move(0.0, 300)
        await self.bot.attack_technique(3) # -1TP
    async def path_2(self):
        logger_set_path(self.map, 2)
        await self.bot.teleport(x=1251/2400, y=383/1080, start=1.75, deg=0.5, n=4) # Communing Hall
        await self.bot.move(0.35, 3200)
        await self.bot.move(0.0, 3900)
        await self.bot.move(0.5, 1300)
        await self.bot.interact() # Enter Dreamscape
        await self.bot.move(0.5, 500)
        await self.bot.attack_technique(5) # +2TP
        await self.bot.move(0.0, 300)
        await self.bot.attack_technique(4) # items
        await self.bot.move(0.0, 300)
        await self.bot.attack_technique(10) # -1TP, items
        # TODO: more enemies, very hard to reach
    async def path_3(self):
        logger_set_path(self.map, 3)
        await self.bot.teleport(x=1312/2400, y=656/1080, start=0.75, deg=1.5, n=2) # Echo of War
        await self.bot.move(0.12, 1800)
        await self.bot.attack() # +2TP
    async def path_4(self):
        logger_set_path(self.map, 4)
        await self.bot.teleport(x=1312/2400, y=656/1080, start=0.75, deg=1.5, n=2) # Echo of War
        await self.bot.move(1.1, 500)
        await self.bot.attack_technique(13) # move
        await self.bot.move(1.3, 300)
        await self.bot.attack_technique(10) # move
        await self.bot.move(1.4, 300)
        await self.bot.attack_technique(5) # -1TP
        await self.bot.move(1.0, 300)
        await self.bot.attack_technique(6) # move
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(10) # -1TP, roamer
        await self.bot.move(0.25, 300)
        await self.bot.attack_technique(2) # move
        await self.bot.move(0.25, 300)
        await self.bot.attack_technique(20) # move
        await self.bot.posfix(0.25, 500)
        await self.bot.move(1.05, 300)
        await self.bot.attack_technique(8) # move
        await self.bot.move(1.25, 300)
        await self.bot.attack_technique(10) # -2TP
    async def path_5(self):
        logger_set_path(self.map, 5)
        await self.bot.teleport(x=1251/2400, y=383/1080, start=1.75, deg=0.5, n=4) # Communing Hall
        await self.bot.move(1.4, 3000)
        await self.bot.move(1.5, 1000)
        await self.bot.attack() # items
        await self.bot.move(1.6, 4500)
        await self.bot.move(0.1, 1600)
        await self.bot.attack() # +2TP
    async def path_6(self):
        logger_set_path(self.map, 6)
        await self.bot.teleport(x=613/2400, y=335/1080, start=1.75, deg=0.5, n=4) # Hall of Chords
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
    async def path_7(self):
        logger_set_path(self.map, 7)
        await self.bot.teleport(x=636/2400, y=610/1080, start=1.75, deg=0.5, n=3) # Ascension Hallway
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
    async def path_8(self):
        logger_set_path(self.map, 8)
        await self.bot.teleport(x=1251/2400, y=383/1080, start=1.75, deg=0.5, n=4) # Communing Hall
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
    async def path_9(self):
        logger_set_path(self.map, 9)
        await self.bot.teleport(x=613/2400, y=335/1080, start=1.75, deg=0.5, n=4) # Hall of Chords
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
        await self.bot.teleport(x=897/2400, y=775/1080, start=0.25, deg=1.5, n=2) # Bud of Erdutition
        await self.bot.move(1.5, 1200)
        await self.bot.attack_technique(1) # items
        await self.bot.move(1, 1500)
        await self.bot.move(0.83, 2500)
        await self.bot.attack_technique(1) # items
        await self.bot.move(1.3, 300)
        await self.bot.attack_technique(9) # -1TP
    async def path_11(self):
        logger_set_path(self.map, 11)
        await self.bot.teleport(x=897/2400, y=775/1080, start=0.25, deg=1.5, n=2) # Bud of Erdutition
        await self.bot.move(1.37, 500)
        await self.bot.attack_technique(19) # -1TP
    async def path_12(self):
        logger_set_path(self.map, 12)
        await self.bot.teleport(x=600/2400, y=682/1080, start=0.75, deg=1.5, n=3) # Cavern of Corrosion
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
    async def path_13(self):
        logger_set_path(self.map, 13)
        await self.bot.teleport(x=834/2400, y=592/1080, start=1.75, deg=0.5, n=3) # Stagnant Shadow
        await self.bot.move(1.5, 300)
        await self.bot.attack_technique(4) # +2TP
    async def path_14(self):
        logger_set_path(self.map, 14)
        await self.bot.teleport(x=670/2400, y=412/1080, start=1.25, deg=0.5, n=4) # Saloon of Gospels
        await self.bot.move(0.7, 2500)
        await self.bot.move(1.0, 1600)
        await self.bot.move(0.75, 300)
        await self.bot.attack_technique(3) # items
        await self.bot.move(0.75, 1500)
        await self.bot.posfix(0.75, 500)
        await self.bot.move(1.5, 1500)
        await self.bot.move(1.6, 1200)
        await self.bot.interact() # Enter Dreamscape
        await self.bot.move(0.75, 2000)
        await self.bot.posfix(0.75, 500)
        await self.bot.move(1.9, 1300)
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(12) # move
        await self.bot.move(0.75, 300)
        await self.bot.attack_technique(3) # items
        await self.bot.move(1.7, 1200)
        await self.bot.move(0.0, 300)
        await self.bot.attack_technique(10) # -2TP
        await self.bot.move(0.25, 1500)
        await self.bot.posfix(0.25, 500)
        await self.bot.move(1.25, 700)
        await self.bot.move(1.0, 500)
        await self.bot.attack_technique(26) # move
        await self.bot.attack_technique(1) # items
        await self.bot.move(0.5, 400)
        await self.bot.attack_technique(14) # items
        await self.bot.move(0.0, 300)
        await self.bot.attack_technique(12) # +2TP
        await self.bot.move(1.25, 600)
        await self.bot.move(1.0, 300)
        await self.bot.attack_technique(14) # move
        await self.bot.move(0.75, 1500)
        await self.bot.posfix(0.75, 500)
        await self.bot.move(1.75, 700)
        await self.bot.move(1.5, 300)
        await self.bot.attack_technique(17) # move
        await self.bot.move(1.6, 900)
        await self.bot.attack_technique(1) # -1TP
        for _ in range(2): # -1TP, roamer
            await self.bot.move(1.5, 300)
            await self.bot.attack_technique(1)
        for _ in range(2):
            await self.bot.move(0.5, 300)
            await self.bot.attack_technique(1)
        for _ in range(2):
            await self.bot.move(1.0, 300)
            await self.bot.attack_technique(1)
        for _ in range(2):
            await self.bot.move(0.0, 300)
            await self.bot.attack_technique(1)
        # this part doesn't always work
        await self.bot.move(1.8, 300)
        await self.bot.attack_technique(5)
        await self.bot.move(1.75, 500)
        await self.bot.posfix(1.75, 500)
        await self.bot.move(0.4, 900)
        await self.bot.move(0.0, 300)
        await self.bot.attack_technique(18) # items
    async def path_15(self):
        logger_set_path(self.map, 15)
        await self.bot.teleport(x=613/2400, y=335/1080, start=1.75, deg=0.5, n=4) # Hall of Chords
        await self.bot.move(0.1, 500)
        await self.bot.attack_technique(12) # move
        await self.bot.move(0.45, 1500)
        await self.bot.move(0.6, 900)
        await self.bot.interact() # Enter Dreamscape
        await self.bot.move(0.7, 700)
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(15) # +2TP
        await self.bot.move(0.41, 1900)
        await self.bot.interact() # Obtain Bubble Charge
        await self.bot.move(1.75, 500)
        await self.bot.move(0.0, 300)
        await self.bot.attack_technique(6) # move
        await self.bot.move(1.7, 300)
        await self.bot.attack_technique(3) # items
        await self.bot.move(1.75, 1500)
        await self.bot.posfix(1.75, 500)
        await self.bot.move(0.5, 1500)
        await self.bot.move(0.0, 1700)
        await self.bot.action_button()
        await self.bot.move(0.0, 2000)
        await self.bot.move(0.5, 1000)
        await self.bot.move(0.25, 300)
        await self.bot.attack_technique(2) # stability
        await self.bot.move(1.5, 300)
        await self.bot.attack_technique(2) # -1 TP
        await self.bot.move(0.25, 300)
        await self.bot.attack_technique(2) # items
        await self.bot.move(0.25, 1500)
        await self.bot.posfix(0.25, 500)
        await self.bot.move(1.0, 1500)
        await self.bot.move(0.4, 300)
        await self.bot.attack_technique(2) # items
        await self.bot.move(0.25, 1500)
        await self.bot.posfix(0.25, 500)
        await self.bot.move(1.25, 900)
        await self.bot.move(1.5, 3500)
        await self.bot.move(1.0, 2700)
        await self.bot.attack_technique(4) # move
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(4) # move
        await self.bot.move(0.38, 300)
        await self.bot.attack_technique(4) # items
        await self.bot.move(0.25, 1500)
        await self.bot.posfix(0.25, 500)
        await self.bot.move(1.35, 300)
        await self.bot.attack_technique(4) # move
        await self.bot.move(1.5, 300)
        await self.bot.attack_technique(5) # move
        await self.bot.move(1.0, 600)
        await self.bot.attack_technique(12) # move
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(3) # -1TP
        await self.bot.move(0.25, 1500)
        await self.bot.posfix(0.25, 500)
        await self.bot.move(1.25, 300)
        await self.bot.attack_technique(4) # items
        # TODO: more enemies, very hard to reach
    async def path_16(self):
        logger_set_path(self.map, 16)
        await self.bot.teleport(x=613/2400, y=335/1080, start=1.75, deg=0.5, n=4) # Hall of Chords
        await self.bot.move(0.9, 500)
        await self.bot.attack_technique(20) # move
        await self.bot.move(0.6, 500)
        await self.bot.attack_technique(11) # move
        await self.bot.move(0.25, 1800)
        await self.bot.move(0.1, 500)
        await self.bot.interact() # Enter Dreamscape
        await self.bot.move(1.25, 1500)
        await self.bot.posfix(1.25, 500)
        await self.bot.move(0.25, 500)
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(10) # move
        await self.bot.move(1.0, 300)
        await self.bot.attack_technique(6) # move
        await self.bot.move(0.45, 300)
        await self.bot.attack_technique(6) # items
        await self.bot.move(0.0, 300)
        await self.bot.attack_technique(8) # -1TP
        await self.bot.move(0.75, 2500)
        await self.bot.posfix(0.75, 500)
        await self.bot.move(1.6, 2900)
        await self.bot.move(0.0, 300)
        await self.bot.attack_technique(3) # items
        await self.bot.move(1.5, 500)
        await self.bot.move(0.0, 300)
        await self.bot.attack_technique(11) # move
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(3) # -1TP
        await self.bot.move(0.75, 2500)
        await self.bot.posfix(0.75, 500)
        await self.bot.move(1.5, 500)
        await self.bot.attack_technique(8) # +2TP
        # # await self.bot.move(1.25, 1500)
        # await self.bot.posfix(1.25, 500)
        # await self.bot.move(0.5, 1500)
        # await self.bot.move(0.6, 2900)
        # await self.bot.interact() # Gain Bubble Charge
        # await self.bot.move(1.7, 2500)
        # await self.bot.interact() # 
        # TODO: more enemies, very hard to reach


