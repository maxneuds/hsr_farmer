from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra


class Storage_Zone:
    def __init__(self, device):
        self.map = 'Storage Zone'
        self.bot = Bot(device)
    async def farm(self):
        await self.teleport()
        await self.path_1()
        await self.path_2()
        await self.path_3()
        await self.path_4()
        await self.path_5()
    async def teleport(self):
        logger_set_path(self.map, 'Teleport')
        logger.info('---')
        logger.info("--- Map: Storage Zone")
        logger.info('---')
        await self.bot.switch_map(y_list=630/1080, world='herta_space_station', scroll_down=False, # Special Purpose Lab
                                x=1068/2400, y=647/1080, corner='botright', move_x=0, move_y=0)
        await self.bot.move(1.3, 1900)
        await self.bot.move(1.0, 4500)
        await self.bot.move(0.61, 6500)
        await self.bot.move(0.1, 200)
        await self.bot.attack_technique(6) # -1TP
    async def path_1(self):
        logger_set_path(self.map, 1)
        await self.bot.use_teleporter(510/2400, 507/1080, move_x=0, move_y=0, corner='botright') # Bud of Destruction
        await self.bot.move(1.5, 4000)
        await self.bot.attack_technique(4) # -1TP
        await self.bot.move(1.75, 2000)
        await self.bot.posfix(1.75, 1000)
        await self.bot.move(0.8, 1000)
        await self.bot.move(1.0, 2800)
        await self.bot.move(0.5, 6400)
        await self.bot.move(1.0, 2200)
        await self.bot.move(1.5, 1500)
        for _ in range(2): # -1TP
            await self.bot.move(1.5, 300)
            await self.bot.attack_technique(2)
        for _ in range(2):
            await self.bot.move(1.25, 300)
            await self.bot.attack_technique(2)
    async def path_2(self):
        logger_set_path(self.map, 2)
        await self.bot.use_teleporter(576/2400, 569/1080, move_x=0, move_y=0, corner='botright') # Outside the Control Center
        await self.bot.move(1.3, 400)
        await self.bot.attack() # items
        await self.bot.move(1.6, 300)
        await self.bot.attack_technique(3) # -1TP
        await self.bot.posfix(1.75, 1000)
        await self.bot.move(1.0, 600)
        await self.bot.move(1.4, 1500)
        await self.bot.move(1.6, 500)
        await self.bot.attack() # +2TP
        await self.bot.move(0.6, 800)
        await self.bot.move(0.4, 1500)
        await self.bot.move(0.5, 4000)
        await self.bot.move(0.2, 500)
        await self.bot.attack() # +2TP
        await self.bot.move(0.25, 500)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.0, 600)
        await self.bot.move(0.7, 2200)
        await self.bot.move(1.1, 800)
        await self.bot.attack_technique(4) # -1TP
    async def path_3(self):
        logger_set_path(self.map, 3)
        await self.bot.use_teleporter(895/2400, 530/1080, move_x=0, move_y=0, corner='botright', confirm=True) # Courtyard
        await self.bot.move(1.5, 1500)
        await self.bot.move(1.75, 500)
        await self.bot.attack_technique(8) # -1TP, roamer
    async def path_4(self):
        logger_set_path(self.map, 4)
        await self.bot.use_teleporter(895/2400, 530/1080, move_x=0, move_y=0, corner='botright', confirm=True) # Courtyard
        await self.bot.move(0.35, 2000)
        await self.bot.attack() # +2TP
        await self.bot.move(1.35, 3100)
        await self.bot.move(1.0, 1500)
        await self.bot.move(0.88, 1200)
        await self.bot.attack() # items
        await self.bot.move(1.05, 3000)
        await self.bot.attack_technique(5) # -2TP
    async def path_5(self):
        logger_set_path(self.map, 5)
        await self.bot.use_teleporter(1172/2400, 556/1080, move_x=0, move_y=0, corner='botright') # Path of Gelid Wind
        await self.bot.move(1.2, 600)
        await self.bot.attack() # +2TP
    async def restore_tp(self, tp):
        logger_set_path(self.map, 'TP Restore')
        logger.info('---')
        logger.info("--- Map: Storage Zone")
        logger.info('---')
        if tp == 4:
            await self.bot.switch_map(y_list=630/1080, world='herta_space_station', scroll_down=False, # Bud of Destruction
                                    x=510/2400, y=507/1080, corner='botright', move_x=0, move_y=0)
            await self.bot.move(1.6, 700)
            await self.bot.attack() # +2TP
            await self.bot.use_teleporter(1068/2400, 647/1080, corner='botright', move_x=0, move_y=0) # Special Purpose Lab
            await self.bot.move(0.5, 1900)
            await self.bot.move(0.1, 3300)
            await self.bot.move(0.6, 500)
            await self.bot.attack_technique(8) # move
            await self.bot.move(0.4, 2000)
            await self.bot.move(0.5, 1000)
            await self.bot.move(0.6, 1000)
            await self.bot.move(0.9, 3000)
            await self.bot.move(0.7, 1000)
            await self.bot.move(0.6, 500)
            await self.bot.attack_technique(7) # +2TP
        else:
            raise SystemExit(f'no {tp} TP restore available')
        

