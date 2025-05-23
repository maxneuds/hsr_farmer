from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra
from datetime import datetime as dt


class Audition_Venue:
    '''
    R2: 2
    '''
    def __init__(self, device):
        self.map = 'Audition Venue'
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
        await self.extra.metrics(self.map, t_start)
    async def teleport(self):
        logger_set_path(self.map, 'Teleport')
        logger.info('---')
        logger.info('--- Map: SoulGlad Scorchsand Audition Venue')
        logger.info('---')
        await self.bot.switch_map_new(world='penacony', y_list=567/1080, scroll_down=True, # Audition Plaza
                                      x=940/2400, y=580/1080, start=1.75, deg=0.5, n=0, confirm=False)
        await self.bot.move(0.5, 500)
        await self.bot.attack_technique(5) # move
        await self.bot.move(0.75, 500)
        await self.bot.attack_technique(1) # items
        await self.bot.move(1.75, 900)
        await self.bot.move(0.1, 300)
        await self.bot.attack_technique(3) # items
        await self.bot.move(0.9, 1500)
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(11) # move
        await self.bot.move(1.8, 1000)
        for _ in range(6): # items
            await self.bot.move(0.5, 300)
            await self.bot.attack_technique(1)
        await self.bot.move(1.0, 1700)
        for _ in range(4): # items
            await self.bot.move(1.5, 300)
            await self.bot.attack_technique(1)
        await self.bot.move(0.55, 300)
        await self.bot.attack_technique(6) # move
        await self.bot.move(0.7, 500)
        await self.bot.posfix(0.75, 500)
        await self.bot.move(1.9, 1200)
        await self.bot.move(0.5, 2000)
        await self.bot.move(1.0, 300)
        await self.bot.attack_technique(2) # items
        await self.bot.move(0.55, 300)
        await self.bot.attack_technique(4) # items
        await self.bot.move(0.0, 300)
        await self.bot.attack_technique(7) # items
    async def path_1(self):
        logger_set_path(self.map, 1)
        await self.bot.teleport(x=749/2400, y=480/1080, start=1.25, deg=0.5, n=2, sub_select={'autoselect': True}) # Dreamplay Fantasia: Action Challenge
        await self.bot.move(0.275, 3100)
        await self.bot.attack_technique(2) # -2TP
        await self.bot.move(1.75, 3000)
        await self.bot.posfix(1.75, 500)
        await self.bot.move(1.05, 3000)
        await self.bot.attack_technique(1) # +2TP
        await self.bot.move(1.6, 500)
        await self.bot.move(1.8, 2000)
        await self.bot.posfix(1.75, 500)
        await self.bot.move(0.95, 1900)
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(5) # items
        await self.bot.move(0.6, 500)
        await self.bot.move(0.75, 1000)
        await self.bot.posfix(0.75, 500)
        await self.bot.move(1.75, 1200)
        await self.bot.move(0.5, 700)
        await self.bot.move(0.6, 500)
        await self.bot.move(0.75, 1000)
        await self.bot.move(1.0, 300)
        await self.bot.attack_technique(4) # -2TP
        await self.bot.move(1.4, 3000)
        await self.bot.move(1.1, 1000)
        await self.bot.restore_tp('trick_snack') # +2TP
        await self.bot.posfix(1.25, 500)
        await self.bot.move(0.25, 1500)
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(7) # move
        await self.bot.move(0.2, 300)
        await self.bot.attack_technique(4) # move
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(8) # -3TP
        await self.bot.move(1.75, 300)
        await self.bot.attack_technique(4) # items
        await self.bot.move(0.0, 2000)
        await self.bot.move(1.75, 1500)
        await self.bot.restore_tp('trick_snack') # +2TP
        await self.bot.move(0.75, 1000)
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(6) # -1TP
        await self.bot.move(1.0, 300)
        await self.bot.attack_technique(3) # -1TP, roamer
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(6) # move
        await self.bot.move(1.0, 300)
        await self.bot.attack_technique(3) # items
        await self.bot.move(0.75, 1500)
        await self.bot.posfix(0.75, 500)
        await self.bot.move(1.75, 1600)
        await self.bot.move(1.5, 300)
        await self.bot.move(1.0, 300)
        await self.bot.attack_technique(5) # move
        await self.bot.move(1.0, 1000)
        await self.bot.move(0.5, 800)
        await self.bot.move(0.1, 300)
        await self.bot.attack_technique(2) # items
        await self.bot.move(0.25, 1500)
        await self.bot.posfix(0.25, 500)
        await self.bot.move(1.25, 1600)
        await self.bot.move(1.5, 300)
        await self.bot.attack_technique(3) # items
    async def path_2(self):
        logger_set_path(self.map, 2)
        await self.bot.teleport(x=610/2400, y=485/1080, start=1.25, deg=0.5, n=2, sub_select={'autoselect': True}) # Dreamplay Fantasia: Acting Challenge
        await self.bot.move(0.5, 900)
        await self.bot.move(1.0, 1600)
        await self.bot.attack() # items
        await self.bot.move(0.125, 2400)
        await self.bot.attack() # +2TP
        await self.bot.move(0.7, 1500)
        await self.bot.move(0.5, 300)
        await self.bot.attack() # items
        await self.bot.move(0.75, 1000)
        await self.bot.move(0.35, 300)
        await self.bot.attack_technique(8) # items
        await self.bot.move(0.0, 1500)
        await self.bot.posfix(0.0, 500)
        await self.bot.move(1.5, 1000)
        await self.bot.move(0.0, 500)
        await self.bot.move(0.5, 2000)
        await self.bot.move(0.8, 1000)
        await self.bot.attack_technique(6) # items
        await self.bot.move(1.9, 300)
        await self.bot.attack_technique(10) # items
        await self.bot.move(1.75, 1500)
        await self.bot.posfix(1.75, 500)
        await self.bot.move(0.75, 1500)
        await self.bot.move(0.5, 1500)
        await self.bot.move(0.7, 300)
        await self.bot.attack_technique(2) # items
        await self.bot.move(0.4, 300)
        await self.bot.attack_technique(7) # items
        await self.bot.move(0.25, 1500)
        await self.bot.posfix(0.25, 500)
        await self.bot.move(1.25, 1500)
        await self.bot.move(1.0, 300)
        await self.bot.attack_technique(10) # move
        await self.bot.move(1.4, 300)
        await self.bot.attack_technique(3) # -2TP
        await self.bot.move(1.9, 300)
        await self.bot.attack_technique(2) # items
    async def path_3(self):
        logger_set_path(self.map, 3)
        await self.bot.teleport(x=805/2400, y=225/1080, start=0.75, deg=1.5, n=3, sub_select={'autoselect': True}) # Superstar Showdown: Arena II
        await self.bot.move(0.3, 300)
        await self.bot.attack_technique(3) # items
        await self.bot.move(0.95, 300)
        await self.bot.attack_technique(5) # items
        await self.bot.move(1.75, 700)
        await self.bot.move(1.5, 300)
        await self.bot.attack_technique(1) # +2TP
        await self.bot.move(0.2, 1150)
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(19) # items
        await self.bot.move(0.35, 300)
        await self.bot.attack_technique(6) # items
        await self.bot.move(0.6, 300)
        await self.bot.attack_technique(6) # items
    async def path_4(self):
        logger_set_path(self.map, 4)
        await self.bot.teleport(x=1316/2400, y=625/1080, start=1.75, deg=0.5, n=3, sub_select={'autoselect': True}) # Gunfire Time: Time Trial
        await self.bot.move(0.3, 800)
        await self.bot.move(0.0, 300)
        await self.bot.attack_technique(5) # -2TP
        await self.bot.move(1.75, 500)
        await self.bot.posfix(1.75, 500)
        await self.bot.move(0.9, 300)
        await self.bot.attack_technique(6) # items
        await self.bot.move(0.75, 1500)
        await self.bot.move(1.95, 1200)
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(6) # move
        await self.bot.move(1.0, 300)
        await self.bot.attack_technique(6) # move
        await self.bot.move(1.25, 300)
        await self.bot.attack_technique(3) # items
        await self.bot.move(1.25, 1000)
        await self.bot.posfix(1.25, 500)
        await self.bot.move(0.3, 300)
        await self.bot.attack_technique(9) # move
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(6) # move
        await self.bot.move(0.6, 300)
        await self.bot.attack_technique(2) # +2TP
        await self.bot.move(1.9, 300)
        await self.bot.attack_technique(6) # items
        await self.bot.move(1.75, 1000)
        await self.bot.posfix(1.75, 500)
        await self.bot.move(0.9, 900)
        await self.bot.move(1.5, 1500)
        await self.bot.move(1.7, 1200)
        await self.bot.move(0.0, 300)
        await self.bot.attack_technique(6) # move
        await self.bot.move(0.25, 1000)
        await self.bot.posfix(0.25, 500)
        await self.bot.move(1.5, 300)
        await self.bot.attack_technique(2) # move
        await self.bot.move(0.0, 300)
        await self.bot.attack_technique(3) # move
        await self.bot.move(0.3, 300)
        await self.bot.attack_technique(4) # -1TP
        await self.bot.move(1.5, 300)
        await self.bot.attack_technique(6) # items
        await self.bot.move(1.0, 300)
        await self.bot.attack_technique(2) # items
    async def path_5(self):
        logger_set_path(self.map, 5)
        await self.bot.teleport(x=1316/2400, y=625/1080, start=1.75, deg=0.5, n=3, sub_select={'x': 1390/2400, 'y': 332/1080}) # Gunfire Time: Time Trial (Posterior)
        await self.bot.move(1.45, 3000)
        await self.bot.attack_technique(6) # items
        await self.bot.move(1.25, 500)
        await self.bot.posfix(1.25, 500)
        await self.bot.move(0.25, 900)
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(8) # +2TP
        await self.bot.move(0.0, 1500)
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(3) # items
        await self.bot.move(0.0, 300)
        await self.bot.attack_technique(8) # move
        await self.bot.move(1.4, 300)
        await self.bot.attack_technique(6) # move
        await self.bot.move(0.1, 500)
        await self.bot.move(0.0, 300)
        await self.bot.attack_technique(7) # move
        await self.bot.move(1.5, 300)
        await self.bot.attack_technique(11) # -2TP
        await self.bot.move(0.25, 300)
        await self.bot.attack_technique(5) # items
    async def path_6(self):
        logger_set_path(self.map, 6)
        await self.bot.teleport(x=665/2400, y=225/1080, start=0.75, deg=1.5, n=3, sub_select={'autoselect': True}) # Superstar Showdown: Arena I
        await self.bot.move(0.8, 300)
        await self.bot.attack_technique(5) # items
        await self.bot.move(0.0, 300)
        await self.bot.attack_technique(9) # items
        await self.bot.move(0.25, 500)
        await self.bot.posfix(0.25, 500)
        await self.bot.move(1.3, 1600)
        await self.bot.attack_technique(1) # +2TP
        await self.bot.move(0.8, 300)
        await self.bot.attack_technique(3) # move
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(18) # move
        await self.bot.move(0.3, 900)
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(2) # items
        await self.bot.move(0.7, 300)
        await self.bot.attack_technique(5) # items
        await self.bot.move(0.35, 300)
        await self.bot.attack_technique(5) # items
    async def path_7(self):
        logger_set_path(self.map, 7)
        await self.bot.teleport(x=974/2400, y=582/1080, start=0.25, deg=1.5, n=1) # Path of the Superstar
        await self.bot.move(1.25, 1100)
        await self.bot.move(1.5, 300)
        await self.bot.attack_technique(8) # items
        await self.bot.move(0.0, 1000)
        await self.bot.attack_technique(2) # items
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(8) # items


