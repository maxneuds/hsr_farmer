from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra
from datetime import datetime as dt


class Clock_Studios_Theme_Park:
    '''
    TP:-4->1
    XP:7648/7648
    Time:???
    '''
    def __init__(self, device):
        self.map = 'Clock Studios Theme Park'
        self.bot = Bot(device)
        self.extra = Extra(device)
    async def farm(self):
        t_start = dt.now()
        await self.teleport()
        await self.path_1()
        await self.path_2()
        await self.path_3()
        await self.path_4()
        await self.extra.restore_tp(tp=4, info='Clock Studios Theme Park 1')
        await self.path_5()
        await self.path_6()
        await self.path_7()
        await self.path_8()
        await self.path_9()
        await self.path_10()
        await self.extra.metrics(self.map, t_start)
    async def teleport(self):
        logger_set_path(self.map, 'Teleport')
        logger.info('---')
        logger.info('--- Map: Clock Studios Theme Park')
        logger.info('---')
        await self.bot.switch_map(y_list=446/1080, world='penacony', scroll_down=True, # Theme Park Entrance
                                    x=1216/2400, y=299/1080, corner='botright', move_x=1, move_y=6, confirm=True)
        await self.bot.move(0.45, 6300)
        await self.bot.attack(2) # items
        await self.bot.move(1.0, 2500)
        await self.bot.attack(2) # items
        await self.bot.move(0.3, 6000)
        await self.bot.attack(3) # items
        await self.bot.move(1.0, 5800)
        await self.bot.attack(3) # items
    async def path_1(self):
        logger_set_path(self.map, 1)
        await self.bot.use_teleporter(1209/2400, 276/1080, move_x=1, move_y=6, confirm=True) # Theme Park Entrance
        await self.bot.move(0.36, 6000)
        await self.bot.move(0.2, 2700)
        await self.bot.move(0.5, 12900)
        await self.bot.move(0.25, 3000)
        await self.bot.move(0.5, 2000)
        await self.bot.move(0.2, 1000)
        await self.bot.move(0.5, 2700)
        await self.bot.move(0.9, 4000)
        await self.bot.move(0.6, 2000)
        await self.bot.move(0.8, 3000)
        await self.bot.move(1.5, 2000)
        await self.bot.move(1.7, 2000)
        await self.bot.move(1.6, 900)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.move(1.25, 2500)
        await self.bot.posfix(1.25, 1000)
        await self.bot.move(0.3, 2500)
        await self.bot.move(0.5, 1500)
        await self.bot.move(0.7, 1300)
        await self.bot.move(1.0, 1500)
        await self.bot.move(1.2, 1500)
        await self.bot.move(1.5, 2000)
        await self.bot.move(1.6, 1800)
        await self.bot.move(1.2, 1000)
        await self.bot.move(0.7, 3200)
        await self.bot.move(0.5, 1500)
        await self.bot.move(0.4, 500)
        await self.bot.attack_technique(3) # -1TP
    async def path_2(self):
        logger_set_path(self.map, 2)
        await self.bot.use_teleporter(731/2400, 494/1080, corner='botright', move_x=1, move_y=6) # Shape of Duty
        await self.bot.move(1.3, 700)
        await self.bot.attack() # +2TP
    async def path_3(self):
        logger_set_path(self.map, 3)
        await self.bot.use_teleporter(539/2400, 455/1080, move_x=1, move_y=1) # Hanu Gang Place
        await self.bot.move(0.8, 3300)
        for _ in range(4): # -1TP, roamer
            await self.bot.move(0.6, 300)
            await self.bot.attack_technique(1)
        for _ in range(6): # items
            await self.bot.move(1.5, 300)
            await self.bot.attack_technique(1)
        await self.bot.move(1.75, 2000)
        await self.bot.posfix(1.75, 1000)
        await self.bot.move(0.6, 3500)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.move(0.8, 1500)
        await self.bot.attack_technique(3) # -1TP
        await self.bot.move(1.45, 300)
        await self.bot.attack_technique(5) # -1TP
        await self.bot.move(1.1, 1000)
        await self.bot.move(1.4, 2000)
        await self.bot.move(1.25, 1000)
        await self.bot.posfix(1.25, 1000)
        await self.bot.move(0.5, 5100)
        await self.bot.move(1.0, 900)
        await self.bot.attack() # +2TP
    async def path_4(self):
        logger_set_path(self.map, 4)
        await self.bot.use_teleporter(539/2400, 455/1080, move_x=1, move_y=1, confirm=True) # Hanu Gang Place
        await self.bot.move(0.49, 7000)
        await self.bot.move(0.01, 5500)
        await self.bot.move(0.5, 500)
        await self.bot.attack() # items
        await self.bot.move(0.52, 4500)
        await self.bot.attack_technique(3) # -2TP
    async def path_5(self):
        logger_set_path(self.map, 5)
        await self.bot.switch_map(y_list=446/1080, world='penacony', scroll_down=True, # Hamster Ball Park
                                    x=490/2400, y=633/1080, corner='topright', move_x=1, move_y=1)
        await self.bot.move(1.58, 7000)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.move(0.0, 1500)
        await self.bot.move(1.3, 3000)
        await self.bot.posfix(1.25, 1000)
        await self.bot.move(0.4, 1000)
        await self.bot.move(0.7, 2800)
        await self.bot.move(1.0, 300)
        await self.bot.attack_technique(8) # -1TP
        await self.bot.move(1.9, 300)
        await self.bot.attack_technique(8) # -1TP
        await self.bot.move(1.0, 300)
        await self.bot.attack_technique(8) # stability
    async def path_6(self):
        logger_set_path(self.map, 6)
        await self.bot.use_teleporter(1100/2400, 423/1080, corner='botright', move_x=3, move_y=3) # Bud of Preservation
        await self.bot.move(1.69, 2500)
        await self.bot.attack() # +2TP
        await self.bot.move(1.2, 4100)
        await self.bot.move(1.1, 1600)
        await self.bot.attack() # items
        await self.bot.move(0.6, 2200)
        await self.bot.move(0.75, 1000)
        await self.bot.attack_technique(5) # -2TP
        await self.bot.move(1.5, 300)
        await self.bot.attack_technique(3) # -1TP
    async def path_7(self):
        logger_set_path(self.map, 7)
        await self.bot.use_teleporter(490/2400, 633/1080, move_x=1, move_y=1, corner='topright', confirm=True) # Hamster Ball Park
        await self.bot.move(0.2, 3000)
        await self.bot.move(1.98, 4500)
        await self.bot.attack() # +2TP
        await self.bot.move(0.4, 300)
        await self.bot.move(0.2, 700)
        await self.bot.move(0.1, 2800)
        await self.bot.attack() # items
        await self.bot.move(1.55, 6000)
        await self.bot.move(1.9, 700)
        await self.bot.attack() # +2TP
    async def path_8(self):
        logger_set_path(self.map, 8)
        await self.bot.use_teleporter(490/2400, 633/1080, move_x=1, move_y=1, corner='topright', confirm=True) # Hamster Ball Park
        await self.bot.move(0.2, 3000)
        await self.bot.move(0.0, 4700)
        await self.bot.move(0.4, 800)
        await self.bot.move(0.6, 500)
        await self.bot.attack_technique(4) # -1TP
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(4) # -1TP
    async def path_9(self):
        logger_set_path(self.map, 9)
        await self.bot.use_teleporter(929/2400, 549/1080, corner='topleft', move_x=0, move_y=7) # Screening Area Entrance
        await self.bot.move(0.6, 2400)
        await self.bot.attack_technique(1) # +2TP
    async def path_10(self):
        logger_set_path(self.map, 10)
        await self.bot.use_teleporter(490/2400, 633/1080, move_x=1, move_y=1, corner='topright', confirm=True) # Hamster Ball Park
        await self.bot.move(0.4, 1000)
        await self.bot.move(0.5, 2000)
        await self.bot.move(0.6, 2000)
        await self.bot.move(0.7, 1500)
        await self.bot.move(0.55, 3300)
        for _ in range(10): # -2TP, 1 roamer
            await self.bot.move(0.05, 300)
            await self.bot.attack_technique(1)
        for _ in range(3): # -1TP
            await self.bot.move(1.55, 300)
            await self.bot.attack_technique(1)
        for _ in range(11): # -1TP, roamer, items
            await self.bot.move(1.05, 300)
            await self.bot.attack_technique(1)


