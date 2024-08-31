from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra


class Childs_Dream:
    '''
    TP:-3
    '''
    def __init__(self, device):
        self.map = 'Childs Dream'
        self.bot = Bot(device)
        self.extra = Extra(device)
    async def farm(self):
        await self.teleport()
        await self.path_1()
        await self.path_2()
        await self.path_3()
        await self.extra.restore_tp(tp=4)
        await self.path_4()
        await self.extra.restore_tp(tp=4)
        await self.path_5()
    async def teleport(self):
        logger_set_path(self.map, 'Teleport')
        logger.info('---')
        logger.info("--- Map: Childs's Dream")
        logger.info('---')
        await self.bot.switch_map(y_list=893/1080, world='penacony', scroll_down=False, # Corridor of Memories
                                    x=1010/2400, y=304/1080, corner='botright', move_x=0, move_y=4)
        await self.bot.move(0.25, 2000)
        await self.bot.move(0.0, 1900)
        await self.bot.move(0.5, 3300)
        await self.bot.attack() # items
        await self.bot.move(1.8, 300)
        await self.bot.attack_technique(8) # -2TP
    async def path_1(self):
        logger_set_path(self.map, 1)
        await self.bot.use_teleporter(962/2400, 356/1080, move_x=0, move_y=0, corner='botright') # Eddying Dreamscape
        await self.bot.move(1.9, 1600)
        await self.bot.attack() # +2TP
        await self.bot.move(1.1, 1700)
        await self.bot.move(1.5, 2900)
        await self.bot.move(1.9, 700)
        await self.bot.attack_technique(3) # -2TP
    async def path_2(self):
        logger_set_path(self.map, 2)
        await self.bot.use_teleporter(962/2400, 519/1080, move_x=0, move_y=0, corner='botright') # Bud of Aether
        await self.bot.move(1.45, 2200)
        await self.bot.move(1.88, 9400)
        await self.bot.interact()
        await self.bot.move(1.95, 2900)
        await self.bot.action_button()
        await self.bot.move(0.00, 3000)
        await self.bot.move(1.5, 2000)
        await self.bot.move(1.25, 500)
        await self.bot.attack_technique(5) # -1TP
    async def path_3(self):
        logger_set_path(self.map, 3)
        await self.bot.use_teleporter(1122/2400, 617/1080, move_x=0, move_y=0, corner='botright') # Clock Factory
        await self.bot.move(0.5, 5000)
        await self.bot.move(1.0, 600)
        await self.bot.attack() # items
        await self.bot.move(1.3, 800)
        await self.bot.move(1.0, 500)
        await self.bot.attack_technique(5) # -1TP
    async def path_4(self):
        logger_set_path(self.map, 4)
        await self.bot.switch_map(y_list=893/1080, world='penacony', scroll_down=False, # Eddying Dreamscape
                                    x=962/2400, y=356/1080, corner='botright', move_x=0, move_y=0)
        await self.bot.move(0.5, 9000)
        await self.bot.move(1.0, 3200)
        await self.bot.move(0.6, 300)
        await self.bot.move(0.5, 500)
        await self.bot.attack() # items
        await self.bot.move(1.5, 800)
        await self.bot.move(1.0, 3000)
        for _ in range(2): # -3TP
            await self.bot.move(0.5, 300)
            await self.bot.attack_technique(2)
        for _ in range(2):
            await self.bot.move(1.5, 300)
            await self.bot.attack_technique(2)
        await self.bot.move(0.7, 2200)
        await self.bot.move(0.5, 1500)
        await self.bot.move(0.0, 1500)
        await self.bot.interact()
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.25, 2500)
        await self.bot.action_button()
        await self.bot.move(1.0, 2600)
        await self.bot.move(0.5, 2300)
        await self.bot.attack() # items
        await self.bot.move(1.0, 1300)
        await self.bot.move(0.5, 2200)
        await self.bot.action_button()
        await self.bot.move(0.5, 2200)
        await self.bot.move(0.0, 300)
        await self.bot.attack_technique(8) # +2TP
        await self.bot.move(1.9, 3000)
        await self.bot.posfix(1.75, 1000)
        await self.bot.move(0.95, 4800)
        await self.bot.move(0.5, 2000)
        await self.bot.move(0.0, 1400)
        await self.bot.action_button()
        await self.bot.move(0.0, 3000)
        await self.bot.move(0.5, 5000)
        await self.bot.move(1.0, 1300)
        await self.bot.move(0.5, 3800)
        await self.bot.attack_technique(3) # -2TP
        await self.bot.move(0.35, 2000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.4, 2500)
        await self.bot.move(1.0, 700)
        await self.bot.interact()
        await self.bot.move(1.2, 1100)
        await self.bot.action_button()
        await self.bot.move(1.0, 2700)
        await self.bot.move(0.5, 3000)
        await self.bot.action_button()
        await self.bot.move(0.5, 2000)
        await self.bot.move(1.0, 1600)
        await self.bot.move(1.5, 3000)
        await self.bot.attack_technique(3) # -1TP
    async def path_5(self):
        logger_set_path(self.map, 5)
        await self.bot.switch_map(y_list=893/1080, world='penacony', scroll_down=False, # Corridor of Memories
                                    x=1010/2400, y=304/1080, corner='botright', move_x=0, move_y=4)
        await self.bot.move(1.5, 9300)
        await self.bot.move(1.0, 7000)
        await self.bot.attack() # items
        await self.bot.move(1.5, 500)
        await self.bot.attack_technique(6) # -3TP


