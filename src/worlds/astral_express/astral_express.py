from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.astral_express.parlor_car import Parlor_Car


class Astral_Express:
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


