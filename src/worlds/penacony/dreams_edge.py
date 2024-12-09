from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra
from datetime import datetime as dt


class Dreams_Edge:
    '''
    TP: -12
    R4: 2 
    '''
    def __init__(self, device):
        self.map = 'Dream\'s Edge'
        self.bot = Bot(device)
        self.extra = Extra(device)
    async def farm(self):
        t_start = dt.now()
        await self.teleport()
        await self.path_1()
        await self.extra.restore_tp(tp=4, info="Dream's Edge 1")
        await self.path_2()
        await self.path_3()
        await self.path_4()
        await self.path_5()
        await self.path_6()
        await self.extra.restore_tp(tp=4, info="Dream's Edge 2")
        await self.path_7()
        await self.path_8()
        await self.extra.metrics(self.map, t_start)
    async def teleport(self):
        logger_set_path(self.map, 'Teleport')
        logger.info('---')
        logger.info("--- Map: Dream's Edge")
        logger.info('---')
        await self.bot.switch_map(y_list=771/1080, world='penacony', scroll_down=False, # Bud of Memories
                                    x=658/2400, y=738/1080, move_x=0, move_y=7, corner='botleft')
        await self.bot.move(1.65, 2300)
        await self.bot.attack_technique(3) # -2TP
        await self.bot.move(1.2, 2000)
        await self.bot.move(1.7, 2000)
        await self.bot.posfix(1.65, 1000)
        await self.bot.move(0.8, 5700)
        await self.bot.attack_technique(1) # items
        await self.bot.move(1.8, 1400)
        await self.bot.move(1.3, 300)
        await self.bot.attack_technique(8) # -1TP
    async def path_1(self):
        logger_set_path(self.map, 1)
        await self.bot.use_teleporter(764/2400, 253/1080, move_x=2, move_y=3, corner='botright') # Rooftop Garden
        await self.bot.move(0.9, 1000)
        await self.bot.attack() # +2TP
        await self.bot.move(1.0, 1600)
        await self.bot.move(0.5, 2400)
        await self.bot.move(0.9, 900)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.move(0.05, 400)
        await self.bot.attack_technique(8) # -2TP
    async def path_2(self):
        logger_set_path(self.map, 2)
        await self.bot.switch_map(y_list=771/1080, world='penacony', scroll_down=False, # Rooftop Garden
                                    x=764/2400, y=253/1080, corner='botright', move_x=2, move_y=3)
        await self.bot.move(0.5, 3500)
        await self.bot.move(0.00, 2500)
        await self.bot.move(1.90, 1400)
        await self.bot.attack_technique(3) # -1TP
        await self.bot.move(0.9, 1100)
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(6) # -1TP
    async def path_3(self):
        logger_set_path(self.map, 3)
        await self.bot.teleport(x=1009/2400, y=614/1080, start=0.75, deg=0.0, n=0, confirm=True) # The Family's Construction Authority
        await self.bot.move(0.25, 3000)
        await self.bot.move(0.5, 8500)
        await self.bot.attack() # +2TP
        await self.bot.move(1.05, 5000)
        await self.bot.attack_technique(11) # -2TP
        await self.bot.move(1.25, 2500)
        await self.bot.posfix(1.25, 1000)
        await self.bot.move(0.5, 3000)
        await self.bot.move(0.9, 2000)
        await self.bot.move(0.67, 1800)
        await self.bot.move(1.0, 500)
        await self.bot.interact()
        await self.bot.move(0.75, 2000)
        await self.bot.posfix(0.75, 1000)
        await self.bot.move(1.4, 900)
        await self.bot.move(0.9, 1700)
        await self.bot.move(0.4, 2500)
        await self.bot.move(0.2, 500)
        await self.bot.move(0.0, 300)
        await self.bot.sleep(0.5)
        await self.bot.interact()
        await self.bot.move(0.25, 2000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.0, 1300)
        await self.bot.move(0.45, 2600)
        await self.bot.move(1.95, 2900)
        await self.bot.move(0.45, 2000)
        await self.bot.attack_technique(2) # +2TP
        await self.bot.move(0.25, 1000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.0, 3000)
        await self.bot.move(0.6, 1500)
        await self.bot.attack_technique(1) # items
        await self.bot.move(0.2, 700)
        await self.bot.attack_technique(2) # items
    async def path_4(self):
        logger_set_path(self.map, 4)
        await self.bot.use_teleporter(764/2400, 253/1080, move_x=2, move_y=3, corner='botright') # Rooftop Garden
        await self.bot.move(0.5, 5000)
        await self.bot.move(0.75, 1500)
        await self.bot.move(0.5, 2000)
        await self.bot.move(0.38, 1800)
        await self.bot.attack() # items
        await self.bot.move(1.0, 500)
        await self.bot.attack_technique(8) # -1TP
    async def path_5(self):
        logger_set_path(self.map, 5)
        await self.bot.teleport(x=932/2400, y=660/1080, start=0.25, deg=1.5, n=1) # Dreamweaver Plaza
        await self.bot.move(1.97, 2000)
        await self.bot.attack_technique(8) # -1TP
    async def path_6(self):
        logger_set_path(self.map, 6)
        await self.bot.teleport(x=932/2400, y=660/1080, start=0.25, deg=1.5, n=1) # Dreamweaver Plaza
        await self.bot.move(0.25, 1500)
        await self.bot.move(0.5, 500)
        await self.bot.attack_technique(7) # move
        await self.bot.move(0.0, 500)
        await self.bot.attack_technique(6) # move
        await self.bot.move(0.5, 500)
        await self.bot.attack_technique(5) # move
        await self.bot.move(0.5, 500)
        await self.bot.move(1.9, 1300)
        await self.bot.attack_technique(1) # items
        await self.bot.move(0.5, 500)
        await self.bot.attack_technique(4) # -1TP
        await self.bot.move(1.0, 300)
        await self.bot.attack_technique(5) # -1TP
    async def path_7(self):
        logger_set_path(self.map, 7)
        await self.bot.switch_map_new(world='penacony', y_list=771/1080, scroll_down=False, # Dreamweaver Plaza
                                      x=932/2400, y=660/1080, start=0.25, deg=1.5, n=1, confirm=False)
        await self.bot.move(0.25, 1500)
        await self.bot.move(0.5, 500)
        await self.bot.attack_technique(7) # move
        await self.bot.move(0.0, 500)
        await self.bot.attack_technique(6) # move
        await self.bot.move(0.5, 500)
        await self.bot.attack_technique(15) # move
        await self.bot.attack_technique(6) # -3TP, roamer
        await self.bot.move(1.2, 300)
        await self.bot.attack_technique(4) # stability
        await self.bot.move(0.2, 300)
        await self.bot.attack_technique(8) # items
    async def path_8(self):
        logger_set_path(self.map, 8)
        await self.bot.use_teleporter(909/2400, 345/1080, move_x=0, move_y=7, corner='botleft') # Shape of Roast
        await self.bot.move(1.5, 3000)
        await self.bot.move(0.05, 1300)
        await self.bot.attack() # +2TP
        await self.bot.move(1.3, 300)
        await self.bot.attack_technique(5) # -3TP, roamer
        await self.bot.move(0.75, 300)
        await self.bot.attack_technique(6)
        await self.bot.move(1.75, 300)
        await self.bot.attack_technique(6)


