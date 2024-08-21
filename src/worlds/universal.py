from logger import logger, logger_set_path
from automation.bot import Bot


class Init:
    '''
    Status: 1/1
    Time:
    '''
    def __init__(self, device):
        self.bot = Bot(device)
    async def crafting(self):
        logger_set_path('craft tp restore items')
        await self.bot.craft_item('trick_snack', all=True)
        await self.bot.craft_item('punitive_energy', all=True)


