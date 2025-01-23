from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra
from datetime import datetime as dt


class Okhema:
    '''
    R2: 2
    '''
    def __init__(self, device):
        self.map = 'Okhema'
        self.bot = Bot(device)
        self.extra = Extra(device)
    async def farm(self):
        t_start = dt.now()
        await self.teleport()
        # await self.path_1()
        # await self.extra.metrics(self.map, t_start)
    async def teleport(self):
        logger_set_path(self.map, 'Teleport')
        logger.info('---')
        logger.info('--- Map: "Eternal Holy City" Okhema')
        logger.info('---')
        await self.bot.switch_map_new(world='amphoreus', y_list=567/1080, scroll_down=False, # ???
                                      x=940/2400, y=580/1080, start=1.75, deg=0.5, n=0, confirm=False, debug=True)
    async def path_1(self):
        logger_set_path(self.map, 1)
        await self.bot.teleport(x=749/2400, y=480/1080, start=1.25, deg=0.5, n=2, sub_select={'autoselect': True}) # ???
        await self.bot.move(0.275, 3100)
        await self.bot.attack_technique(2) # -2TP
        

# await self.bot.move(0.5, 500)
# await self.bot.posfix(0.5, 500)
# await self.bot.attack_technique(2) # -2TP