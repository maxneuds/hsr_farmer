from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra


class Supply_Zone:
    def __init__(self, device):
        self.map = 'Supply Zone'
        self.bot = Bot(device)
    async def farm(self):
        await self.teleport()
        await self.path_1()
        await self.path_2()
        await self.path_3()
    async def teleport(self):
        logger_set_path(self.map, 'Teleport')
        logger.info('---')
        logger.info("--- Map: Supply Zone")
        logger.info('---')
        await self.bot.switch_map(y_list=750/1080, world='herta_space_station', scroll_down=True, # Electrical Room
                                    x=510/2400, y=595/1080, corner='botleft', move_x=0, move_y=0, confirm=True)
        await self.bot.move(0.5, 3000)
        await self.bot.move(0.25, 500)
        await self.bot.attack_technique(5) # -2TP
        await self.bot.move(1.0, 1000)
        await self.bot.move(0.75, 1000)
        await self.bot.posfix(0.75, 1000)
        await self.bot.move(0.1, 1600)
        await self.bot.move(0.5, 1200)
        await self.bot.move(1.0, 3600)
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(10) # -1TP
    async def path_1(self):
        logger_set_path(self.map, 1)
        await self.bot.use_teleporter(x=848/2400, y=376/1080, corner='botleft', move_x=0, move_y=0) # Spare Parts Warehouse
        await self.bot.move(1.5, 2100)
        await self.bot.move(1.7, 500)
        await self.bot.attack() # +2TP
        await self.bot.move(0.7, 700)
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(16) # -1TP
    async def path_2(self):
        logger_set_path(self.map, 2)
        await self.bot.use_teleporter(x=893/2400, y=479/1080, corner='botleft', move_x=0, move_y=0) # Bud of Preservation
        await self.bot.move(1.2, 700)
        await self.bot.attack() # +2TP
        await self.bot.move(1.9, 900)
        await self.bot.attack() # items
        await self.bot.move(1.0, 1200)
        await self.bot.move(1.45, 2300)
        await self.bot.interact()
        await self.bot.wait_for_onmap(min_duration=2)
        await self.bot.move(0.5, 500)
        await self.bot.move(0.0, 5000)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.move(1.5, 1000)
        await self.bot.move(1.75, 1000)
        await self.bot.posfix(1.5, 1000)
        await self.bot.move(0.7, 1000)
        await self.bot.move(1.0, 300)
        await self.bot.attack_technique(20)
        await self.bot.move(0.4, 2500)
        await self.bot.move(0.5, 1200)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.move(0.0, 300)
        await self.bot.attack_technique(3) # items
    async def path_3(self):
        logger_set_path(self.map, 3)
        await self.bot.use_teleporter(x=510/2400, y=595/1080, corner='botleft', move_x=0, move_y=0) # Electrical Room
        await self.bot.move(0.7, 2600)
        await self.bot.attack() # items
        await self.bot.move(0.0, 300)
        await self.bot.attack_technique(7) # +2TP
    async def restore_tp(self, tp):
        logger_set_path(self.map, 'TP Restore')
        logger.info('---')
        logger.info("--- Map: Supply Zone")
        logger.info('---')
        if tp == 4:
            await self.bot.switch_map(y_list=745/1080, world='herta_space_station', scroll_down=False,
                                    x=1315/2400, y=434/1080, corner='botright', move_x=0, move_y=0) # Destruction's Beginning
            await self.bot.move(0.1, 800)
            await self.bot.attack() # +2TP
            await self.bot.use_teleporter(x=1036/2400, y=583/1080, corner='botright', move_x=0, move_y=0) # Railway Platform
            await self.bot.move(0.4, 1500)
            await self.bot.attack() # items
            await self.bot.move(1.4, 4900)
            await self.bot.move(1.0, 5600)
            await self.bot.move(1.3, 500)
            await self.bot.attack() # +2TP
            await self.bot.move(0.59, 2200)
            await self.bot.attack() # items
        else:
            raise SystemExit(f'no {tp} TP restore available')
    

