from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra
from datetime import datetime as dt


class Okhema:
    def __init__(self, device):
        self.map = 'Okhema'
        self.bot = Bot(device)
        self.extra = Extra(device)
    async def restore_tp(self, tp):
        logger_set_path(self.map, f'TP Restore {tp}')
        logger.info('---')
        logger.info('--- Map: "Eternal Holy City" Okhema')
        logger.info('---')
        t_start = dt.now()
        if tp == 4.1:
            await self.bot.switch_map_new(world='amphoreus', y_list=485/1080, scroll_down=False, # ???
                                            x=810/2400, y=650/1080, start=0.25, deg=1.25, n=2, m=6, confirm=False)
        # await self.extra.metrics(self.map, t_start)
        

# await self.bot.move(0.5, 500)
# await self.bot.posfix(0.5, 500)
# await self.bot.attack_technique(2) # -2TP