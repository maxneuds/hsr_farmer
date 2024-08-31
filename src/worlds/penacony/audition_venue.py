from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra


class Audition_Venue:
    def __init__(self, device):
        self.map = 'Audition Venue'
        self.bot = Bot(device)
    async def teleport(self):
        logger_set_path(self.map, 'Teleport')
        logger.info('---')
        logger.info('--- Map: Audition Venue')
        logger.info('---')

    # Soulgrad: y=686
    # class Penacony_Grand_Theater:
    #     def __init__(self, device):
    #         self.bot = Bot(device)
    #     async def teleport(self): # 1->3
    #         logger_set_path('Teleport')
    #         logger.info('---')
    #         logger.info('--- Map: Penacony Grand Theater')
    #         logger.info('---')
    #         await self.bot.switch_map(y_list=807/1080, world='penacony', scroll_down=True,
    #                                     x=787/2400, y=717/1080, corner='topleft', move_x=3, move_y=7)

            
