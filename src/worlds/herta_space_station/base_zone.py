from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra


class Base_Zone:
    def __init__(self, device):
        self.map = 'Base Zone'
        self.bot = Bot(device)
    async def farm(self):
        await self.teleport()
    async def teleport(self):
        logger_set_path(self.map, 'Teleport')
        logger.info('---')
        logger.info("--- Map: Base Zone")
        logger.info('---')
        await self.bot.switch_map(y_list=508/1080, world='herta_space_station', scroll_down=True, # Monitoring Room
                                    x=1044/2400, y=405/1080, corner='topright', move_x=0, move_y=0)
        await self.bot.move(1.5, 500)
        await self.bot.attack_technique(8) # -1TP
        await self.bot.move(1.3, 500)
        await self.bot.attack_technique(3) # items
    async def restore_tp(self, tp):
        logger_set_path(self.map, f'TP Restore {tp}')
        logger.info('---')
        logger.info("--- Map: Base Zone")
        logger.info('---')
        if tp == 4.1:
            await self.bot.switch_map(y_list=508/1080, world='herta_space_station', scroll_down=True, # Monitoring Room
                                        x=1044/2400, y=405/1080, corner='topright', move_x=0, move_y=0)
            await self.bot.move(1.0, 500)
            await self.bot.attack_technique(3) # +2TP
            await self.bot.move(0.75, 1500)
            await self.bot.posfix(0.75, 500)
            await self.bot.move(1.9, 2050)
            await self.bot.move(1.5, 500)
            await self.bot.attack_technique(10) # move
            await self.bot.move(1.6, 500)
            await self.bot.attack_technique(3) # +2TP
            await self.bot.move(1.25, 500)
            await self.bot.attack_technique(4) # items
            await self.bot.move(1.2, 500)
            await self.bot.attack_technique(3) # move
            await self.bot.move(1.4, 500)
            await self.bot.attack_technique(4) # items
        elif tp == 4.2:
            await self.bot.switch_map(y_list=508/1080, world='herta_space_station', scroll_down=True, # Stagnant Shadow
                                        x=924/2400, y=726/1080, corner='botleft', move_x=0, move_y=0, confirm=True)
            await self.bot.move(0.0, 1500)
            await self.bot.attack_technique(2) # +2TP
            await self.bot.use_teleporter(x=865/2400, y=177/1080, corner='botleft', move_x=0, move_y=0) # Reception Center
            await self.bot.move(0.625, 3400)
            await self.bot.move(0.7, 2000)
            await self.bot.move(0.4, 300)
            await self.bot.attack_technique(2) # +2TP
        else:
            raise SystemExit(f'no {tp} TP restore available')


