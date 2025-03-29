from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra
from datetime import datetime as dt


class Robot_Settlement:
    def __init__(self, device):
        self.map = 'Robot Settlement'
        self.bot = Bot(device)
        self.extra = Extra(device)
    async def farm(self):
        t_start = dt.now()
        await self.teleport()
        await self.path_1()
        await self.path_2()
        await self.path_3()
        await self.path_4()
        await self.extra.metrics(self.map, t_start)
    async def teleport(self):
        logger_set_path(self.map, 'Teleport')
        logger.info('---')
        logger.info("--- Map: Robot Settlement")
        logger.info('---')
        await self.bot.switch_map(y_list=927/1080, world='jarilo_vi', scroll_down=True, # Vagrant Camp
                                    x=944/2400, y=268/1080, corner='botleft', move_x=0, move_y=3)
        await self.bot.move(0.5, 1500)
        await self.bot.move(0.72, 3450)
        await self.bot.attack() # items
        await self.bot.move(0.33, 5450)
        await self.bot.attack() # items
        await self.bot.move(1.6, 900)
        await self.bot.move(0.2, 600)
        await self.bot.move(0.0, 3600)
        await self.bot.move(0.4, 500)
        await self.bot.attack() # items
        await self.bot.move(0.5, 1000)
        await self.bot.posfix(0.75, 1500)
        await self.bot.move(1.6, 3000)
        await self.bot.attack() # items
        await self.bot.move(1.4, 3900)
        await self.bot.move(1.05, 2000)
        await self.bot.move(1.0, 100)
        await self.bot.attack() # items
    async def path_1(self):
        logger_set_path(self.map, 1)
        await self.bot.use_teleporter(x=625/2400, y=757/1080, corner='botright', move_x=0, move_y=3) # Bud of Harmony
        await self.bot.move(1.7, 1700)
        await self.bot.attack_technique(3) # -2TP
    async def path_2(self):
        logger_set_path(self.map, 2)
        await self.bot.use_teleporter(x=765/2400, y=371/1080, corner='botright', move_x=0, move_y=0) # Energy Conversation Station
        await self.bot.move(1.7, 900)
        await self.bot.move(1.9, 1200)
        await self.bot.move(0.0, 500)
        await self.bot.attack() # items
        await self.bot.move(1.9, 2000)
        await self.bot.move(0.0, 1000)
        for _ in range(3): # -1TP
            await self.bot.move(0.0, 300)
            await self.bot.attack_technique(2)
        for _ in range(3):
            await self.bot.move(1.5, 300)
            await self.bot.attack_technique(2)
        await self.bot.attack_technique(1) # +2TP
    async def path_3(self):
        logger_set_path(self.map, 3)
        await self.bot.use_teleporter(x=765/2400, y=371/1080, corner='botright', move_x=0, move_y=0) # Energy Conversation Station
        raise SystemExit("Stability Problem. More Posfix needed")
        await self.bot.move(1.75, 1900)
        await self.bot.move(1.95, 1400)
        await self.bot.move(1.4, 4900)
        await self.bot.move(1.1, 300)
        await self.bot.attack() # items
        await self.bot.move(0.7, 2000)
        await self.bot.posfix(0.75, 1500)
        await self.bot.move(1.6, 1000)
        await self.bot.move(1.5, 2000)
        await self.bot.move(1.3, 1500)
        await self.bot.move(1.5, 1900)
        await self.bot.move(1.4, 1500)
        await self.bot.move(1.2, 1000)
        await self.bot.move(1.3, 1900)
        await self.bot.attack() # +2TP
        await self.bot.posfix(1.25, 1500)
        await self.bot.move(0.0, 400)
        await self.bot.move(1.6, 2300)
        await self.bot.move(1.3, 900)
        await self.bot.move(1.1, 2500)
        await self.bot.move(1.6, 300)
        await self.bot.attack_technique(4) # -1TP
        await self.bot.move(0.0, 1000)
        await self.bot.posfix(1.75, 1000)
        await self.bot.move(0.55, 1500)
        await self.bot.move(0.2, 2500)
        await self.bot.move(0.2, 1400)
        await self.bot.move(0.0, 200)
        await self.bot.attack_technique(2) # -2TP
        await self.bot.move(0.1, 1300)
        await self.bot.move(0.5, 500)
        await self.bot.attack_technique(5) # -1TP
        await self.bot.move(0.75, 1000)
        await self.bot.posfix(0.75, 1000)
        await self.bot.move(1.5, 2900)
        await self.bot.attack_technique(2)
        await self.bot.move(1.6, 1500)
        await self.bot.attack_technique(2) # +2TP
    async def path_4(self):
        logger_set_path(self.map, 4)
        await self.bot.use_teleporter(x=942/2400, y=346/1080, corner='botright', move_x=0, move_y=0) # Svarog's Base
        await self.bot.move(1.6, 2300)
        await self.bot.attack() # +2TP
    async def restore_tp(self, tp):
        logger_set_path(self.map, 'TP Restore')
        logger.info('---')
        logger.info("--- Map: Robot Settlement")
        logger.info('---')
        if tp == 2:
            await self.bot.switch_map(y_list=927/1080, world='jarilo_vi', scroll_down=True, # Svarog's Base
                                        x=944/2400, y=343/1080, corner='botright', move_x=0, move_y=0)
            await self.bot.move(0.5, 300)
            await self.bot.attack_technique(12)
            await self.bot.move(0.6, 300)
            await self.bot.attack_technique(8) # +2TP
            await self.bot.move(0.45, 300)
            await self.bot.attack_technique(7) # items
            await self.bot.move(0.2, 300)
            await self.bot.attack_technique(4)
            await self.bot.move(1.8, 300)
            await self.bot.attack_technique(7) # items
        else:
            raise SystemExit(f'no {tp} TP restore available')


