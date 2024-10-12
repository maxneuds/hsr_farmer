from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra
from datetime import datetime as dt


class Skysplitter:
    def __init__(self, device):
        self.map = 'Skysplitter'
        self.bot = Bot(device)
        self.extra = Extra(device)
    async def farm(self):
        t_start = dt.now()
        await self.teleport() 
        await self.path_1()
        await self.extra.metrics(self.map, t_start)
    async def restore_tp(self, tp):
        logger_set_path(self.map, f'TP Restore {tp}')
        logger.info('---')
        logger.info(f'--- Map: {self.map}')
        logger.info('---')
        t_start = dt.now()
        if tp == 4.1:
            await self.bot.switch_map(y_list=925/1080, world='the_xianzhou_luofu', scroll_down=True, # Echo of War
                                        x=940/2400, y=201/1080, corner='botright', move_x=0, move_y=0)
            await self.bot.move(1.9, 500)
            await self.bot.attack_technique(2) # +2TP
            await self.bot.use_teleporter(817/2400, 266/1080, move_x=0, move_y=0, swipe=0, corner='botright') # Wardance Arena Sub-Floor
            await self.bot.move(1.5, 500)
            await self.bot.attack_technique(5) # +2TP
        elif tp == 4.2:
            await self.bot.switch_map(y_list=925/1080, world='the_xianzhou_luofu', scroll_down=True, # Reception Hall
                                        x=1180/2400, y=496/1080, corner='botright', move_x=0, move_y=0)
            await self.bot.move(1.05, 500)
            await self.bot.attack_technique(4) # items
            await self.bot.move(0.6, 1600)
            await self.bot.move(0.5, 300)
            await self.bot.attack_technique(1) # items
            await self.bot.move(1.1, 300)
            await self.bot.attack_technique(5) # +2TP
            await self.bot.use_teleporter(729/2400, 876/1080, move_x=0, move_y=0, swipe=0, corner='topleft', confirm=True) # Tactics Board
            await self.bot.move(1.2, 1000)
            await self.bot.move(1.0, 1000)
            await self.bot.move(0.575, 300)
            await self.bot.attack_technique(9) # items
            await self.bot.move(1.9, 300)
            await self.bot.attack_technique(8) # items
            await self.bot.move(0.0, 300)
            await self.bot.attack_technique(6) # items
            await self.bot.move(0.2, 600)
            await self.bot.move(0.0, 300)
            await self.bot.attack_technique(4) # move
            await self.bot.move(1.9, 300)
            await self.bot.attack_technique(7) # items
            await self.bot.move(0.5, 300)
            await self.bot.attack_technique(3) # +2TP
            await self.bot.move(1.6, 600)
            await self.bot.move(0.0, 600)
            await self.bot.attack_technique(6) # items
            await self.bot.move(0.5, 300)
            await self.bot.attack_technique(8) # items
            await self.bot.move(0.25, 1500)
            await self.bot.posfix(0.25, 500)
            await self.bot.move(1.4, 2000)
            await self.bot.move(1.0, 300)
            await self.bot.attack_technique(11) # items
            await self.bot.move(1.25, 1000)
            await self.bot.move(0.3, 1100)
            await self.bot.move(0.5, 300)
            await self.bot.attack_technique(9) # items
        else:
            raise SystemExit(f'no {tp} TP restore available')
        await self.extra.metrics(f'{self.map} TP {tp}', t_start)


