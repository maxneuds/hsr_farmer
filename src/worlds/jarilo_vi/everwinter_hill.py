from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra


class Everwinter_Hill:
    def __init__(self, device):
        self.map = 'Everwinter Hill'
        self.bot = Bot(device)
    async def farm(self):
        await self.teleport()
        await self.path_1()
        await self.path_2()
    async def teleport(self):
        logger_set_path(self.map, 'Teleport')
        logger.info('---')
        logger.info("--- Map: Everwinter Hill")
        logger.info('---')
        await self.bot.switch_map(y_list=984/1080, world='jarilo_vi', scroll_down=False,
                                    x=1297/2400, y=394/1080, corner='botleft', move_x=0, move_y=3) # Deck of Creation
        await self.bot.move(0.2, 6000)
        await self.bot.move(0.1, 3100)
        await self.bot.attack() # +2TP
        await self.bot.move(1.5, 5000)
        await self.bot.move(1.9, 1100)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.move(1.9, 1000)
        await self.bot.move(0.0, 1500)
        await self.bot.attack_technique(4) # -2TP
    async def path_1(self):
        logger_set_path(self.map, 1)
        await self.bot.use_teleporter(x=775/2400, y=653/1080, corner='botleft', move_x=0, move_y=3, confirm=True) # Ancient Battlefield: Snow Plains
        await self.bot.move(0.48, 3300)
        await self.bot.move(1.0, 200)
        await self.bot.attack() # +2TP
        await self.bot.move(0.5, 3000)
        await self.bot.move(0.9, 4000)
        await self.bot.move(1.1, 3800)
        await self.bot.attack_technique(2) # -2TP
        await self.bot.move(0.95, 2600)
        await self.bot.attack_technique(1)
        await self.bot.move(0.6, 300)
        await self.bot.attack_technique(1)
        await self.bot.move(0.95, 300)
        await self.bot.attack_technique(8) # -1TP
    async def path_2(self):
        logger_set_path(self.map, 2)
        await self.bot.use_teleporter(x=1297/2400, y=394/1080, corner='botleft', move_x=0, move_y=3) # Deck of Creation
        await self.bot.move(1.5, 4000)
        await self.bot.move(0.0, 2000)
        await self.bot.move(1.75, 2000)
        await self.bot.move(1.4, 700)
        await self.bot.attack() # +2TP


