from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra


class Parlor_Car:
    def __init__(self, device):
        self.map = 'Parlor Car'
        self.bot = Bot(device)
    async def teleport(self):
        logger_set_path(self.map, 'Teleport')
        logger.info('---')
        logger.info("--- Map: Parlor Car")
        logger.info('---')
        await self.bot.switch_map(y_list=266/1080, world='herta_space_station', scroll_down=False, # Pom-Pom
                                    x=923/2400, y=206/1080, corner='botleft', move_x=0, move_y=0)


