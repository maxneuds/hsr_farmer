from logger import logger, logger_set_path
from automation.bot import Bot


class Init:
    '''
    Status: 1/1
    '''
    def __init__(self, device):
        self.parlor_car = Parlor_Car(device)
    async def checkout(self):
        '''
        Status: 1/1
        '''
        await self.parlor_car.teleport()


class Parlor_Car:
    def __init__(self, device):
        self.bot = Bot(device)
    async def teleport(self):
        logger_set_path('Teleport')
        logger.info('---')
        logger.info("--- Map: Parlor Car")
        logger.info('---')
        await self.bot.switch_map(y_list=266/1080, world='herta_space_station', scroll_down=False,
                                    x=923/2400, y=206/1080, corner='botleft', move_x=0, move_y=0) # Pom-Pom



