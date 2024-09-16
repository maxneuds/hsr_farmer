from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra
from datetime import datetime as dt


class The_Shackling_Prison:
    def __init__(self, device):
        self.map = 'The Shackling Prison'
        self.bot = Bot(device)
        self.extra = Extra(device)
    async def farm(self):
        t_start = dt.now()
        await self.teleport()
        await self.path_1()
        await self.path_2()
        await self.path_3()
        await self.path_4()
        await self.path_5()
        await self.path_6()
        await self.path_7()
        await self.path_8()
        await self.path_9()
        await self.path_10()
        await self.path_11()
        await self.extra.restore_tp(tp=4)
        await self.path_12()
        await self.path_13()
        # await self.extra.metrics(self.map, t_start)
    async def dev(self):
        # await self.teleport()
        await self.path_1()
    async def teleport(self):
        logger_set_path(self.map, 'Teleport')
        logger.info('---')
        logger.info('--- Map: The Shackling Prison')
        logger.info('---')
        await self.bot.switch_map(y_list=808/1080, world='the_xianzhou_luofu', scroll_down=True, # Nether Key
                                    x=862/2400, y=640/1080, corner='topright', move_x=6, move_y=6)
        raise SystemExit('check')
        await self.bot.move(1.53, 500)
        await self.bot.attack_technique(4) # items
        await self.bot.move(0.65, 500)
        await self.bot.attack_technique(13) # items
        await self.bot.move(0.35, 500)
        await self.bot.attack_technique(6) # move
        await self.bot.move(0.3, 500)
        await self.bot.attack_technique(4) # items
        await self.bot.move(0.1, 500)
        await self.bot.attack_technique(6) # move
        await self.bot.move(1.9, 500)
        await self.bot.attack_technique(2) # items
        await self.bot.move(1.8, 500)
        await self.bot.attack_technique(6) # move
        await self.bot.move(0.0, 300)
        await self.bot.attack_technique(2) # items
        await self.bot.move(1.5, 500)
        await self.bot.attack_technique(4) # move
        await self.bot.move(1.6, 500)
        await self.bot.attack_technique(3) # move
        await self.bot.move(1.2, 300)
        await self.bot.attack_technique(3) # move
        await self.bot.move(0.53, 300)
        await self.bot.attack_technique(2) # items
    async def path_1(self):
        logger_set_path(self.map, 1)
        await self.bot.use_teleporter(862/2400, 640/1080, corner='topright', move_x=6, move_y=6) # Nether Key
        raise SystemExit('check')
        await self.bot.move(0.65, 500)
        await self.bot.attack_technique(5) # move
        await self.bot.move(0.42, 500)
        await self.bot.attack_technique(8) # -1TP
        await self.bot.move(0.15, 500)
        await self.bot.attack_technique(7) # move
        await self.bot.move(1.8, 300)
        await self.bot.attack_technique(8) # -1TP, roamer
        await self.bot.move(0.1, 1200)
        await self.bot.move(0.25, 2200)
        await self.bot.move(0.5, 1000)
        await self.bot.move(0.75, 3000)
        await self.bot.posfix(0.75, 500)
        await self.bot.move(1.5, 500)
        await self.bot.attack_technique(9) # -1TP
        await self.bot.move(1.55, 300)
        await self.bot.attack_technique(6) # +2TP
        await self.bot.move(1.25, 500)
        await self.bot.attack_technique(12) # items
    async def path_2(self):
        logger_set_path(self.map, 2)
        # await self.bot.use_teleporter(x=1287/2400, y=411/1080, corner='botleft', move_x=3, move_y=3) # Grimfrost Hold (I)
        # raise SystemExit('check: monster gone?')
        await self.bot.move(1.5, 2000)
        await self.bot.attack_technique(3) # items
        await self.bot.move(1.75, 1000)
        await self.bot.posfix(1.75, 500)
        await self.bot.move(0.3, 1500)
        await self.bot.move(1.7, 500)
        await self.bot.attack_technique(4) # items
        await self.bot.move(0.25, 1500)
        await self.bot.posfix(0.25, 500)
        await self.bot.move(1.25, 2000)
        await self.bot.move(1.5, 500)
        await self.bot.attack_technique(3) # items
        await self.bot.move(0.5, 700)
        await self.bot.move(0.0, 500)
        await self.bot.attack_technique(5) # -1TP
    async def path_3(self):
        logger_set_path(self.map, 3)
        await self.bot.use_teleporter(x=1287/2400, y=411/1080, corner='botleft', move_x=3, move_y=3) # Grimfrost Hold (I)
        raise SystemExit('check: monster gone?')
        await self.bot.move(0.4, 500)
        await self.bot.attack_technique(1) # +2TP
        await self.bot.move(1.1, 500)
        await self.bot.attack_technique(3) # items
        await self.bot.move(0.4, 2000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.7, 500)
        await self.bot.move(0.1, 300)
        await self.bot.move(0.6, 500)
        await self.bot.attack_technique(6) # move
        for _ in range(11): # -1TP, roamer
            await self.bot.move(0.45, 300)
            await self.bot.attack_technique(2)
        await self.bot.move(0.6, 2000)
        await self.bot.move(0.75, 1000)
        await self.bot.posfix(0.75, 500)
        await self.bot.move(1.45, 3000)
        await self.bot.move(1.0, 300)
        await self.bot.attack_technique(6) # -1TP
        await self.bot.move(1.6, 800)
        await self.bot.move(1.5, 300)
        await self.bot.attack_technique(4) # items
        await self.bot.move(1.6, 800)
        await self.bot.move(1.5, 300)
        await self.bot.attack_technique(4) # +2TP
        await self.bot.move(0.15, 300)
        await self.bot.attack_technique(10) # items
        await self.bot.move(0.25, 1000)
        await self.bot.posfix(0.25, 500)
        await self.bot.move(1.0, 1000)
        await self.bot.move(0.85, 300)
        await self.bot.attack_technique(8) # items
    async def path_4(self):
        logger_set_path(self.map, 4)
        await self.bot.use_teleporter(x=1287/2400, y=411/1080, corner='botleft', move_x=3, move_y=3) # Grimfrost Hold (I)
        raise SystemExit('monster gone?')
        await self.bot.move(0.6, 500)
        await self.bot.attack_technique(10) # move
        await self.bot.move(0.625, 900)
        await self.bot.interact(wait_for_ready=True)
        await self.bot.move(0.4, 1500)
        await self.bot.move(0.5, 500)
        await self.bot.attack_technique(6) # items
        await self.bot.move(0.9, 300)
        await self.bot.attack_technique(5) # -1TP
        await self.bot.move(0.45, 300)
        await self.bot.attack_technique(3) # -1TP, roamer
        await self.bot.move(1.95, 300)
        await self.bot.attack_technique(5)
        await self.bot.use_teleporter(x=1287/2400, y=411/1080, corner='botleft', move_x=3, move_y=3) # Grimfrost Hold (I)
        await self.bot.move(0.63, 1500)
        await self.bot.attack()
        await self.bot.interact(wait_for_ready=True)
    async def path_5(self):
        logger_set_path(self.map, 5)
        await self.bot.use_teleporter(x=551/2400, y=358/1080, corner='botright', move_x=4, move_y=3) # Grimfrost Hold (II)
        await self.bot.move(0.35, 900)
        await self.bot.attack() # +2TP
        await self.bot.move(1.5, 2000)
        await self.bot.move(1.67, 3600)
        await self.bot.move(1.5, 500)
        await self.bot.attack_technique(10) # items
        await self.bot.move(0.35, 500)
        await self.bot.attack_technique(4) # move
        await self.bot.move(0.0, 500)
        await self.bot.attack_technique(3) # items
        await self.bot.move(0.4, 800)
        await self.bot.move(0.25, 1000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.4, 800)
        await self.bot.move(1.8, 3900)
        await self.bot.interact(wait_for_ready=True)
        await self.bot.move(0.4, 1500)
        await self.bot.move(0.35, 1000)
        await self.bot.move(0.5, 500)
        await self.bot.attack_technique(2) # items
        await self.bot.move(0.25, 1500)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(0.9, 1700)
        await self.bot.move(1.2, 1700)
        await self.bot.move(1.45, 1800)
        await self.bot.move(1.1, 500)
        await self.bot.attack_technique(3) # items
        await self.bot.move(0.5, 1500)
        await self.bot.move(0.25, 1000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.25, 500)
        await self.bot.attack_technique(4) # move
        await self.bot.move(1.65, 500)
        await self.bot.attack_technique(6) # move
        await self.bot.move(0.0, 500)
        await self.bot.attack_technique(8) # move
        await self.bot.move(0.25, 1000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.4, 1800)
        await self.bot.move(1.65, 500)
        await self.bot.attack_technique(18) # items
    async def path_6(self):
        logger_set_path(self.map, 6)
        await self.bot.use_teleporter(x=551/2400, y=358/1080, corner='botright', move_x=4, move_y=3) # Grimfrost Hold (II)
        await self.bot.move(0.5, 500)
        await self.bot.attack_technique(9) # move
        await self.bot.move(0.9, 300)
        await self.bot.attack_technique(4) # -1TP
        await self.bot.move(0.3, 500)
        await self.bot.attack_technique(3) # -1TP
        await self.bot.move(0.0, 100)
        await self.bot.attack_technique(3) # items
        await self.bot.move(0.1, 1500)
        await self.bot.move(0.25, 1000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.3, 2200)
        await self.bot.move(1.0, 500)
        await self.bot.attack_technique(12) # move
        await self.bot.move(1.3, 300)
        await self.bot.attack_technique(6) # -1TP, roamer
        await self.bot.move(1.8, 300)
        await self.bot.attack_technique(3)
        await self.bot.move(1.5, 300)
        await self.bot.attack_technique(3)
    async def path_7(self):
        logger_set_path(self.map, 7)
        await self.bot.use_teleporter(x=575/2400, y=615/1080, corner='topright', move_x=5, move_y=4) # Plankway Front
        await self.bot.move(0.4, 2600)
        await self.bot.attack_technique(1) # items
        await self.bot.move(0.75, 500)
        await self.bot.attack_technique(12) # move
        await self.bot.move(0.6, 500)
        await self.bot.attack_technique(4) # items
        await self.bot.move(0.88, 500)
        await self.bot.attack_technique(8) # +2TP
        await self.bot.move(0.6, 1000)
        await self.bot.move(0.25, 1000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.1, 500)
        await self.bot.attack_technique(7) # items
        await self.bot.move(1.0, 500)
        await self.bot.attack_technique(10) # items
    async def path_8(self):
        logger_set_path(self.map, 8)
        await self.bot.use_teleporter(x=575/2400, y=615/1080, corner='topright', move_x=5, move_y=4) # Plankway Front
        await self.bot.move(1.5, 500)
        await self.bot.attack_technique(16) # items
        await self.bot.move(1.6, 1500)
        await self.bot.posfix(1.6, 500)
        await self.bot.move(0.65, 3900)
        await self.bot.interact(wait_for_ready=True, max_duration=20)
        await self.bot.move(1.3, 2000)
        await self.bot.attack_technique(1) # items
        await self.bot.move(1.25, 1000)
        await self.bot.posfix(1.25, 500)
        await self.bot.move(0.5, 500)
        await self.bot.move(0.9, 500)
        await self.bot.attack_technique(6) # move
        await self.bot.move(0.5, 500)
        await self.bot.attack_technique(7) # -1TP
        await self.bot.move(0.5, 2000)
        await self.bot.move(0.25, 1000)
        await self.bot.posfix(0.25, 500)
        await self.bot.move(1.55, 4000)
        await self.bot.move(1.1, 500)
        await self.bot.attack_technique(4) # items
    async def path_9(self):
        logger_set_path(self.map, 9)
        await self.bot.use_teleporter(x=726/2400, y=248/1080, corner='botright', move_x=2, move_y=5) # Stagnant Shadow
        await self.bot.move(1.6, 500)
        await self.bot.attack_technique(3) # +2TP
        await self.bot.move(1.5, 300)
        await self.bot.attack_technique(2) # move
        await self.bot.move(1.65, 300)
        await self.bot.attack_technique(5) # -2TP
        raise SystemExit()
    async def path_10(self):
        logger_set_path(self.map, 10)
        await self.bot.use_teleporter(x=726/2400, y=248/1080, corner='botright', move_x=2, move_y=5) # Stagnant Shadow
        raise SystemExit('check')
        await self.bot.move(1.4, 500)
        await self.bot.attack_technique(5) # move
        await self.bot.move(1.0, 300)
        await self.bot.attack_technique(2) # items
        await self.bot.move(0.75, 1000)
        await self.bot.posfix(0.75, 500)
        await self.bot.move(1.58, 1100)
        await self.bot.interact(wait_for_ready=True) # teleport to other side
        await self.bot.move(1.5, 300)
        await self.bot.attack_technique(4) # items
        await self.bot.move(1.75, 1000)
        await self.bot.posfix(1.75, 500)
        await self.bot.move(0.6, 1500)
        await self.bot.move(1.0, 300)
        await self.bot.attack_technique(4) # -1TP
        await self.bot.move(0.9, 300)
        await self.bot.attack_technique(5) # -1TP
        await self.bot.move(1.4, 300)
        await self.bot.attack_technique(3) # -1TP
    async def path_11(self):
        logger_set_path(self.map, 11)
        await self.bot.use_teleporter(x=605/2400, y=289/1080, corner='botright', move_x=3, move_y=4) # Pyroscape Hold
        await self.bot.move(1.0, 1400)
        await self.bot.move(1.5, 500)
        await self.bot.attack_technique(10) # move
        await self.bot.posfix(1.75, 1000)
        await self.bot.interact(wait_for_ready=True) # lift bridge
        await self.bot.posfix(1.75, 500)
        await self.bot.move(0.6, 1400)
        await self.bot.move(0.4, 500)
        await self.bot.attack_technique(8) # move
        for _ in range(2): # -2TP, invisible
            await self.bot.move(0.3, 300)
            await self.bot.attack_technique(7)
            await self.bot.move(1.3, 300)
            await self.bot.attack_technique(3)
        await self.bot.move(0.3, 2500)
        await self.bot.move(0.7, 500)
        await self.bot.attack_technique(3) # items, might not always work - it's fine
    async def path_12(self):
        logger_set_path(self.map, 12)
        await self.bot.switch_map(y_list=808/1080, world='the_xianzhou_luofu', scroll_down=True, # Pyroscape Hold
                                    x=605/2400, y=289/1080, corner='botright', move_x=3, move_y=4)
        await self.bot.move(1.0, 2000)
        await self.bot.move(1.1, 500)
        await self.bot.interact(wait_for_ready=True) # lower bridge (default)
        await self.bot.move(0.9, 700)
        await self.bot.move(0.44, 500)
        await self.bot.attack_technique(14)
        await self.bot.move(1.1, 300)
        await self.bot.attack_technique(3) # items
        await self.bot.move(1.3, 1000)
        await self.bot.posfix(1.3, 500)
        await self.bot.move(0.0, 500)
        await self.bot.attack_technique(4)
        await self.bot.move(0.4, 500)
        await self.bot.attack_technique(5) # items
        await self.bot.move(0.55, 2100)
        await self.bot.move(0.7, 1000)
        await self.bot.posfix(0.75, 500)
        await self.bot.move(1.6, 900)
        await self.bot.move(0.35, 300)
        await self.bot.interact(wait_for_ready=True) # take the lift
        await self.bot.move(1.5, 500)
        await self.bot.attack_technique(2) # items
        await self.bot.move(0.5, 1000)
        await self.bot.move(0.25, 500)
        await self.bot.posfix(0.25, 500)
        await self.bot.move(1.7, 1500)
        await self.bot.move(1.5, 1500)
        await self.bot.move(1.25, 1100)
        await self.bot.move(1.0, 500)
        await self.bot.attack_technique(1) # items
        await self.bot.move(1.75, 2000)
        await self.bot.posfix(1.75, 500)
        await self.bot.move(0.35, 2500)
        await self.bot.move(0.0, 400)
        await self.bot.interact(wait_for_ready=True, max_duration=20) # teleport
        await self.bot.move(0.6, 500)
        await self.bot.attack_technique(4) # items
        await self.bot.move(0.0, 500)
        await self.bot.move(0.4, 500)
        await self.bot.attack_technique(8) # items
        await self.bot.attack_technique(2) # move
        await self.bot.move(0.5, 1000)
        await self.bot.posfix(0.5, 500)
        await self.bot.move(1.2, 700)
        await self.bot.move(0.75, 500)
        await self.bot.attack_technique(12) # move
        await self.bot.move(0.5, 500)
        await self.bot.attack_technique(2) # items
        await self.bot.move(0.1, 1100)
        await self.bot.move(0.6, 1500)
        await self.bot.posfix(0.6, 500)
        await self.bot.move(1.9, 1500)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.move(0.6, 1500)
        await self.bot.posfix(0.6, 500)
        await self.bot.move(1.7, 500)
        await self.bot.attack_technique(7) # -1TP
        await self.bot.move(1.0, 1500)
        await self.bot.posfix(1.0, 500)
        await self.bot.move(0.4, 600)
        await self.bot.move(0.7, 1600)
        await self.bot.move(1.1, 500)
        await self.bot.attack_technique(4) # move
        await self.bot.move(1.5, 500)
        await self.bot.attack_technique(4) # +2TP
        await self.bot.move(1.3, 1500)
        await self.bot.posfix(1.25, 500)
        await self.bot.move(0.5, 1200)
        await self.bot.move(1.0, 2000)
        await self.bot.move(1.2, 500)
        await self.bot.attack_technique(3) # -1TP
        await self.bot.move(0.0, 1200)
        for _ in range(3): # -2TP, invisible
            await self.bot.move(1.75, 300)
            await self.bot.attack_technique(6)
            await self.bot.move(0.75, 300)
            await self.bot.attack_technique(4)
    async def path_13(self):
        logger_set_path(self.map, 13)
        await self.bot.use_teleporter(x=605/2400, y=289/1080, corner='botright', move_x=3, move_y=4) # Pyroscape Hold
        raise SystemExit('check, fix last item')
        await self.bot.move(0.8, 300)
        await self.bot.attack_technique(6) # move
        await self.bot.move(0.425, 300)
        await self.bot.attack_technique(16) # +2TP
        await self.bot.move(1.7, 300)
        await self.bot.attack_technique(12) # items


