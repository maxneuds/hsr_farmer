from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra
from datetime import datetime as dt


class The_Soaring_Clock_Hand:
    def __init__(self, device):
        self.map = 'The Soaring Clock Hand'
        self.bot = Bot(device)
        self.extra = Extra(device)
    async def restore_tp(self, tp, info=None):
        if info is None:
            logger_set_path(self.map, 'TP Restore')
        else:
            logger_set_path(info, 'TP Restore')
        logger.info('---')
        logger.info('--- Map: The Soaring Clock Hand')
        logger.info('---')
        t_start = dt.now()
        if tp == 4:
            await self.bot.switch_map(y_list=807/1080, world='penacony', scroll_down=True,
                                        x=974/2400, y=417/1080, corner='topright', move_x=0, move_y=0, confirm=True)
            await self.bot.move(0.35, 3000)
            await self.bot.move(0.5, 2000)
            await self.bot.move(0.86, 2000)
            await self.bot.attack_technique(2) # +2TP
            await self.bot.use_teleporter(917/2400, 648/1080, move_x=0, move_y=0, swipe=0, corner='botright') # Aft Pool
            await self.bot.move(0.75, 3200)
            await self.bot.move(0.5, 3200)
            await self.bot.move(1.0, 300)
            await self.bot.attack_technique(2) # items
            await self.bot.move(1.1, 2000)
            await self.bot.posfix(1.25, 1000)
            await self.bot.move(0.0, 2000)
            await self.bot.move(1.7, 500)
            await self.bot.attack_technique(2) # items
            await self.bot.move(1.25, 2000)
            await self.bot.posfix(1.25, 1000)
            await self.bot.move(0.55, 3000)
            await self.bot.move(1.0, 900)
            await self.bot.attack_technique(6) # items
            await self.bot.move(1.25, 2000)
            await self.bot.posfix(1.25, 1000)
            await self.bot.move(0.3, 3000)
            await self.bot.move(0.2, 1000)
            await self.bot.move(0.5, 300)
            await self.bot.attack_technique(4) # +2TP
        else:
            raise SystemExit(f'no {tp} TP restore available')
        await self.extra.metrics(f'{self.map} TP {tp}', t_start)


