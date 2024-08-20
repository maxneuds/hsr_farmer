from logger import logger, logger_set_path
from automation.bot import Bot


class Astral_Express:
    '''
    Status: 1/1
    '''
    def __init__(self, device):
        self.parlor_car = Parlor_Car(device)
    async def checkout(self):
        '''
        Time:630
        '''
        await self.base_zone.farm() # XP:432/432 Time:90 TP:0->3
        await self.seclusion_zone.farm() # XP:1620/1620 Time:220 TP:3->3
        await self.storage_zone.farm() # XP:2592/2592 Time:250 TP:3->5
        await self.supply_zone.farm() # XP:2484/2484 Time:281 TP:5->5

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



