from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra
from datetime import datetime as dt


class Paperfold_University:
    def __init__(self, device):
        self.map = 'Paperfold University'
        self.bot = Bot(device)
        self.extra = Extra(device)
    async def restore_tp(self, tp):
        logger_set_path(self.map, f'TP Restore: Paperfold University, {tp}tp')
        logger.info('---')
        logger.info(f'--- Map: {self.map}')
        logger.info('---')
        t_start = dt.now()
        if tp == 4:
            await self.bot.switch_map_new(world='penacony', y_list=928/1080, scroll_down=True, # Chromasweven Avenue
                                      x=785/2400, y=785/1080, start=1.75, deg=0.0, n=0, confirm=False)
            await self.bot.move(0.7, 500)
            await self.bot.attack_technique(3) # items
            await self.bot.move(0.2, 1900)
            await self.bot.move(0.5, 300)
            await self.bot.attack_technique(9) # move
            await self.bot.move(1.1, 300)
            await self.bot.attack_technique(6) # +2TP
            # await self.bot.teleport(x=1163/2400, y=577/1080, start=0.25, deg=0.0, n=0) # Cultural Corridor
            # await self.bot.move(0.55, 1000)
            # await self.bot.attack_technique(7) # +2TP
            # await self.bot.teleport(x=793/2400, y=550/1080, start=0.25, deg=0.0, n=0, debug=True) # Central Stage
            # raise SystemExit()
            # await self.bot.use_teleporter(817/2400, 266/1080, move_x=0, move_y=0, swipe=0, corner='botright') # Wardance Arena Sub-Floor
            # await self.bot.move(1.5, 500)
            # await self.bot.attack_technique(5) # +2TP
            # await self.bot.move(0.5, 300)
            # await self.bot.attack_technique(9) # items
        else:
            raise SystemExit(f'no {tp} TP restore available')
        await self.extra.metrics(f'{self.map} TP {tp}', t_start)


