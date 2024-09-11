from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra
from datetime import datetime as dt


class Golden_Hour:
    def __init__(self, device):
        self.map = 'Golden Hour'
        self.bot = Bot(device)
        self.extra = Extra(device)
    async def restore_tp(self, tp):
        logger_set_path(self.map, 'TP Restore')
        logger.info('---')
        logger.info('--- Map: Golden Hour')
        logger.info('---')
        t_start = dt.now()
        if tp == 4.1:
            await self.bot.switch_map(y_list=650/1080, world='penacony',
                                        x=588/2400, y=356/1080, move_x=4, move_y=3,) # Sweet Corner
            await self.bot.move(1.5, 3300)
            await self.bot.attack() # items
            await self.bot.move(1.6, 1000)
            await self.bot.move(1.4, 2800)
            await self.bot.attack() # +2TP
            await self.bot.use_teleporter(815/2400, 245/1080, move_x=0, move_y=2) # Oti Mall
            await self.bot.move(0.7, 2000)
            await self.bot.move(0.9, 4400)
            await self.bot.attack() # +2TP
        elif tp == 4.2:
            await self.bot.switch_map(y_list=650/1080, world='penacony',
                                        x=330/2400, y=498/1080, corner='botright', move_x=0, move_y=0) # The Reverie Hotel Entrance
            await self.bot.move(0.35, 9000)
            await self.bot.move(0.8, 1000)
            await self.bot.attack_technique(3) # +2TP
            await self.bot.use_teleporter(1219/2400, 630/1080, corner='topleft', move_x=0, move_y=0) # Aideen Park
            await self.bot.move(1.5, 3000)
            await self.bot.move(1.6, 3100)
            await self.bot.attack() # items
            await self.bot.move(0.82, 2900)
            await self.bot.attack() # items
            await self.bot.move(1.4, 4000)
            await self.bot.move(1.3, 2400)
            await self.bot.move(0.8, 500)
            await self.bot.attack() # +2TP
        else:
            raise SystemExit(f'no {tp} TP restore available')
        await self.extra.metrics(f'{self.map} TP {tp}', t_start)


