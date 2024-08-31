from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra


class Silvermane_Guard:
    def __init__(self, device):
        self.map = 'Silvermane Guard Restricted Zone'
        self.bot = Bot(device)
    async def restore_tp(self, tp):
        logger_set_path(self.map, 'TP Restore')
        logger.info('---')
        logger.info("--- Map: Silvermane Guard Restricted Zone")
        logger.info('---')
        if tp == 4.1:
            await self.bot.switch_map(y_list=750/1080, world='jarilo_vi', scroll_down=False, # Energy Hub
                                        x=659/2400, y=648/1080, corner='botright', move_x=0, move_y=0, confirm=True)
            await self.bot.move(1.5, 1200)
            await self.bot.move(1.05, 1200)
            await self.bot.move(0.5, 500)
            await self.bot.attack() # items
            await self.bot.move(0.5, 500)
            await self.bot.posfix(0.25, 1000)
            await self.bot.move(1.5, 800)
            await self.bot.move(0.0, 1200)
            await self.bot.move(0.5, 3500)
            await self.bot.move(0.72, 5100)
            await self.bot.attack() # items
            await self.bot.move(0.75, 3900)
            await self.bot.move(1.24, 6300)
            await self.bot.attack() # items
            await self.bot.move(0.6, 3300)
            await self.bot.move(0.3, 2500)
            await self.bot.move(0.0, 1100)
            await self.bot.attack() # +2TP
            await self.bot.move(1.2, 1000)
            await self.bot.move(0.75, 7000)
            await self.bot.attack() # items
            await self.bot.use_teleporter(x=991/2400, y=521/1080, corner='topleft', move_x=0, move_y=4) # Frontline
            await self.bot.move(1.5, 4600)
            await self.bot.move(0.0, 1100)
            await self.bot.move(0.4, 300)
            await self.bot.attack_technique(2) # +2TP
        elif tp == 4.2:
            await self.bot.switch_map(y_list=750/1080, world='jarilo_vi', scroll_down=False, # Outpost
                                        x=1176/2400, y=738/1080, corner='topright', move_x=0, move_y=2, confirm=True)
            await self.bot.move(0.5, 3000)
            await self.bot.move(0.9, 2000)
            await self.bot.attack() # +2TP
            await self.bot.move(0.1, 2000)
            await self.bot.move(0.5, 7800)
            await self.bot.move(0.4, 1000)
            await self.bot.attack() # items
            await self.bot.move(0.5, 2800)
            await self.bot.move(0.0, 1000)
            await self.bot.move(0.1, 3000)
            await self.bot.move(0.4, 1000)
            await self.bot.attack() # items
            await self.bot.use_teleporter(x=896/2400, y=669/1080, corner='topleft', move_x=0, move_y=1) # Shape of Blaze
            await self.bot.move(1.8, 600)
            await self.bot.attack() # items
            await self.bot.move(1.1, 800)
            await self.bot.attack() # +2TP
        else:
            raise SystemExit(f'no {tp} TP restore available')


