from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra


class Outlying_Snow_Plains:
    def __init__(self, device):
        self.map = 'Outlying Snow Plains'
        self.bot = Bot(device)
    async def farm(self):
        await self.teleport()
        await self.path_1()
        await self.path_2()
        await self.path_3()
    async def teleport(self):
        logger.info('Teleport')
        logger.info('---')
        logger.info("--- Map: Outlying Snow Plains")
        logger.info('---')
        await self.bot.switch_map(y_list=508/1080, world='jarilo_vi', scroll_down=False, # Long Slope
                                    x=998/2400, y=338/1080, corner='botright', move_x=0, move_y=0, confirm=True)
        await self.bot.move(0.2, 2200)
        await self.bot.attack() # items
        await self.bot.move(0.67, 8200)
        await self.bot.attack() # items
        await self.bot.move(0.9, 1500)
        await self.bot.move(0.6, 5000)
        await self.bot.move(0.55, 2500)
        await self.bot.move(0.78, 800)
        await self.bot.attack() # items
        await self.bot.move(0.9, 800)
        await self.bot.move(0.8, 300)
        await self.bot.attack_technique(3) # -2TP
    async def path_1(self):
        logger_set_path(self.map, 1)
        await self.bot.use_teleporter(x=1079/2400, y=430/1080, corner='botright', move_x=0, move_y=0) # Bud of Memories
        await self.bot.move(1.3, 3000)
        await self.bot.attack_technique(2) # +2TP
        await self.bot.move(1.1, 1000)
        await self.bot.attack_technique(10) # -1TP
    async def path_2(self):
        logger_set_path(self.map, 2)
        await self.bot.use_teleporter(x=998/2400, y=338/1080, corner='botright', move_x=0, move_y=0, confirm=True) # Long Slope
        await self.bot.move(1.19, 4600)
        await self.bot.attack() # items
        await self.bot.move(0.94, 4400)
        await self.bot.attack_technique(2) # -1TP
    async def path_3(self):
        logger_set_path(self.map, 3)
        await self.bot.use_teleporter(x=998/2400, y=338/1080, corner='botright', move_x=0, move_y=0, confirm=True) # Long Slope
        await self.bot.move(0.62, 2900)
        await self.bot.attack() # +2TP
        await self.bot.move(0.55, 4000)
        await self.bot.move(0.8, 9000)
        await self.bot.move(0.9, 2000)
        await self.bot.attack_technique(4) # -3TP
        await self.bot.move(1.3, 3000)
        await self.bot.posfix(0.75, 1000)
        await self.bot.move(0.2, 1000)
        await self.bot.move(0.61, 4800)
        await self.bot.attack() # items
        await self.bot.move(0.425, 5250)
        await self.bot.attack() # +2TP


