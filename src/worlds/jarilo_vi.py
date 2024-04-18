from logger import logger, logger_set_path
from sys import exit


class Outlying_Snow_Plains:
    def __init__(self, bot):
        self.bot = bot
    async def teleport(self):
        logger.info('Teleport')
        logger.info('---')
        logger.info("--- Map: Outlying Snow Plains")
        logger.info('---')
        await self.bot.switch_map(y_list=508/1080, world='jarilo_vi', scroll_down=False,
                                    x=1079/2400, y=430/1080, corner='botright', move_x=0, move_y=0) # Bud of Memories
        await self.bot.movepi(1.3, 3000)
        await self.bot.attack_technique(2, wait=False) # +2 TP
        await self.bot.movepi(1.1, 1000)
        await self.bot.attack_technique(10)
    async def path_1(self):
        logger_set_path(1)
        await self.bot.use_teleporter(x=998/2400, y=338/1080, corner='botright', move_x=0, move_y=0, confirm=True) # Long Slope
        await self.bot.movepi(0.21, 2100)
        await self.bot.attack()
        await self.bot.movepi(1.2, 6300)
        await self.bot.attack()
        await self.bot.movepi(0.94, 4500)
        await self.bot.attack_technique(2)
    async def path_2(self):
        logger_set_path(2)
        await self.bot.use_teleporter(x=998/2400, y=338/1080, corner='botright', move_x=0, move_y=0, confirm=True) # Long Slope
        await self.bot.movepi(0.61, 2900)
        await self.bot.attack() # +2 TP
        await self.bot.movepi(0.58, 5400)
        await self.bot.attack() # +2 TP
        await self.bot.movepi(0.65, 9000)
        await self.bot.attack_technique(2, wait=False) # items
        await self.bot.movepi(1.00, 1000)
        await self.bot.movepi(0.6, 100)
        await self.bot.attack_technique(3)
        await self.bot.restore_tp(n=1) # +2 TP
        exit() # check
        await self.bot.movepi(1.4, 5600)
        await self.bot.attack_technique(3, wait=False)
        await self.bot.movepi(1.1, 2000)
        await self.bot.position_fixing(0.75, 2500) # useless
        await self.bot.movepi(0.2, 1000)
        await self.bot.movepi(0.61, 4800)
        await self.bot.attack()
        await self.bot.movepi(0.42, 5200)
        await self.bot.attack_technique(2)


class Backwater_Pass:
    def __init__(self, bot):
        self.bot = bot
    async def teleport(self):
        logger.info('Teleport')
        logger.info('---')
        logger.info("--- Map: Backwater Pass")
        logger.info('---')
        await self.bot.switch_map(y_list=629/1080, world='jarilo_vi', scroll_down=False,
                                    x=829/2400, y=273/1080, corner='botright', move_x=0, move_y=0) # Transport Hub
        await self.bot.movepi(1.5, 4900)
        await self.bot.movepi(1.0, 300)
        await self.bot.attack() # items
        await self.bot.movepi(1.5, 700)
        await self.bot.movepi(1.03, 2300)
        await self.bot.attack() # items
        await self.bot.movepi(0.97, 2500)
        await self.bot.movepi(1.0, 300)
        await self.bot.attack_technique(3, wait=False)
        await self.bot.position_fixing(1.3, 2000)
        await self.bot.movepi(0.05, 2600)
        await self.bot.movepi(1.5, 5500)
        await self.bot.movepi(1.3, 200)
        await self.bot.attack() # items
        await self.bot.movepi(1.0, 900)
        await self.bot.movepi(1.5, 2500)
        await self.bot.movepi(0.0, 2000)
        await self.bot.movepi(0.22, 2100)
        await self.bot.attack() # items
    async def path_1(self):
        logger_set_path(1)
        await self.bot.use_teleporter(x=829/2400, y=273/1080, corner='botright', move_x=0, move_y=0) # Transport Hub
        await self.bot.movepi(1.5, 6000)
        await self.bot.movepi(1.75, 3200)
        await self.bot.movepi(0.3, 300)
        await self.bot.attack_technique(4, wait=False)
        await self.bot.movepi(0.1, 500)
        await self.bot.attack_technique(8, wait=False)
        await self.bot.movepi(0.6, 1200)
        await self.bot.attack_technique(2) # items
    async def path_2(self):
        logger_set_path(2)
        await self.bot.use_teleporter(x=945/2400, y=715/1080, corner='topright', move_x=0, move_y=1, confirm=True) # Leisure Plaza
        await self.bot.movepi(1.15, 600)
        await self.bot.attack() # +2 TP
        await self.bot.movepi(0.5, 1000)
        await self.bot.movepi(1.0, 3700)
        await self.bot.movepi(0.5, 3500)
        await self.bot.movepi(0.35, 900)
        await self.bot.attack() # items
        await self.bot.movepi(1.0, 3100)
        await self.bot.attack() # items
        await self.bot.movepi(0.05, 2800)
        await self.bot.movepi(0.55, 2500)
        await self.bot.attack() # items
        await self.bot.position_fixing(0.7, 1500)
        await self.bot.movepi(1.7, 600)
        await self.bot.movepi(0.0, 5900)
        await self.bot.attack_technique(2)
    async def path_3(self): # roamer
        logger_set_path(3)
        await self.bot.use_teleporter(x=830/2400, y=360/1080, corner='topright', move_x=0, move_y=1) # Bud of Aether
        await self.bot.movepi(0.68, 900)
        await self.bot.attack() # items
        await self.bot.movepi(1.5, 2700)
        await self.bot.movepi(0.0, 1300)
        await self.bot.attack() # +2 TP
        await self.bot.movepi(1.78, 1600)
        await self.bot.attack() # items
        await self.bot.movepi(0.8, 700)
        await self.bot.movepi(0.85, 3200)
        await self.bot.movepi(1.0, 3100)
        await self.bot.movepi(1.29, 2400)
        await self.bot.attack_technique(3, wait=False)
        for _ in range(2):
            await self.bot.movepi(1.3, 500)
            await self.bot.attack_technique(1, wait=False)
        for _ in range(2):
            await self.bot.movepi(1.0, 500)
            await self.bot.attack_technique(2, wait=False)
        await self.bot.wait_for_onmap(min_duration=4, no_fight=True)    
    async def path_4(self):
        logger_set_path(4)
        await self.bot.use_teleporter(x=829/2400, y=273/1080, corner='botright', move_x=0, move_y=0) # Transport Hub
        await self.bot.movepi(0.8, 700)
        await self.bot.attack() # +2 TP


class Silvermane_Guard:
    def __init__(self, bot):
        self.bot = bot
    async def teleport(self, tp_restore=False):
        logger.info('Teleport')
        logger.info('---')
        logger.info("--- Map: Silvermane Guard Restricted Zone")
        logger.info('---')
        if tp_restore == 0:
            await self.bot.switch_map(y_list=750/1080, world='jarilo_vi', scroll_down=False,
                                        x=659/2400, y=648/1080, corner='botright', move_x=0, move_y=0, confirm=True) # Energy Hub
            await self.bot.movepi(0.5, 2500)
            await self.bot.movepi(0.72, 5200)
            await self.bot.attack() # items
            await self.bot.movepi(0.75, 3900)
            await self.bot.movepi(1.24, 6300)
            await self.bot.attack() # items
            await self.bot.movepi(0.6, 3300)
            await self.bot.movepi(0.3, 2500)
            await self.bot.movepi(0.0, 1100)
            await self.bot.attack() # TP
            await self.bot.movepi(1.2, 1000)
            await self.bot.movepi(0.75, 7000)
            await self.bot.attack() # items
            await self.bot.use_teleporter(x=659/2400, y=648/1080, corner='botright', move_x=0, move_y=0, confirm=True) # Energy Hub
            await self.bot.movepi(1.5, 1200)
            await self.bot.movepi(1.05, 1200)
            await self.bot.attack() # items
        elif tp_restore == 1:
            await self.bot.switch_map(y_list=750/1080, world='jarilo_vi', scroll_down=False,
                                        x=1176/2400, y=738/1080, corner='topright', move_x=0, move_y=2, confirm=True) # Outpost
            await self.bot.movepi(0.5, 3000)
            await self.bot.movepi(0.9, 2000)
            await self.bot.attack() # TP
            await self.bot.movepi(0.1, 2000)
            await self.bot.movepi(0.5, 7800)
            await self.bot.movepi(0.4, 1000)
            await self.bot.attack() # items
            await self.bot.movepi(0.5, 2800)
            await self.bot.movepi(0.0, 1000)
            await self.bot.movepi(0.1, 3000)
            await self.bot.movepi(0.4, 1000)
            await self.bot.attack() # items
        elif tp_restore == 2:
            await self.bot.switch_map(y_list=750/1080, world='jarilo_vi', scroll_down=False,
                                        x=659/2400, y=648/1080, corner='topleft', move_x=0, move_y=1, debug=True) # Shape of Blaze
        else:
            logger.debug('bad parameter')
            exit()


class Corridor:
    def __init__(self, bot):
        self.bot = bot
    async def teleport(self):
        logger.info('Teleport')
        logger.info('---')
        logger.info("--- Map: Corridor of Fading Echoes")
        logger.info('---')
        await self.bot.switch_map(y_list=869/1080, world='jarilo_vi', scroll_down=False,
                                        x=869/2400, y=351/1080, corner='botright', move_x=0, move_y=3) # Command Center
        await self.bot.movepi(0.3, 4700)
        await self.bot.attack() # items
        await self.bot.movepi(1.0, 700)
        await self.bot.movepi(0.5, 300)
        await self.bot.attack_technique(2, wait=False)
        await self.bot.movepi(0.6, 700)
        await self.bot.attack_technique(4)
    async def path_1(self): # roamer
        logger_set_path(1)
        await self.bot.use_teleporter(x=962/2400, y=502/1080, corner='botright', move_x=0, move_y=0) # Ancient Battlefield: Frontline
        await self.bot.movepi(0.7, 1000)
        await self.bot.attack() # items
        await self.bot.movepi(1.6, 1500)
        await self.bot.movepi(1.5, 4100)
        await self.bot.movepi(1.0, 1000)
        await self.bot.attack_technique(10)
    async def path_2(self): # roamer
        logger_set_path(2)
        await self.bot.use_teleporter(x=962/2400, y=502/1080, corner='botright', move_x=0, move_y=0) # Ancient Battlefield: Frontline
        await self.bot.movepi(1.5, 5000)
        await self.bot.movepi(1.6, 2400)
        await self.bot.attack() # items
        await self.bot.position_fixing(0.9, 2500)
        await self.bot.movepi(1.8, 4000)
        await self.bot.movepi(1.7, 2000)
        await self.bot.movepi(1.8, 700)
        await self.bot.movepi(1.4, 300)
        await self.bot.movepi(1.5, 1000)
        await self.bot.attack_technique(2, wait=False)
        await self.bot.movepi(1.3, 700)
        for _ in range(4):
            await self.bot.movepi(1.5, 500)
            await self.bot.attack_technique(2, wait=False)
        await self.bot.movepi(0.7, 700)
        for _ in range(2):
            await self.bot.movepi(0.95, 500)
            await self.bot.attack_technique(2, wait=False)
        await self.bot.attack_technique(1)
    async def path_3(self):
        logger_set_path(3)
        await self.bot.use_teleporter(x=962/2400, y=502/1080, corner='botright', move_x=0, move_y=0) # Ancient Battlefield: Frontline
        await self.bot.movepi(1.5, 5000)
        await self.bot.movepi(1, 3500)
        await self.bot.movepi(1.51, 6000)
        await self.bot.attack_technique(3, wait=False)
        await self.bot.movepi(0.3, 4000)
        await self.bot.attack() # items
        await self.bot.position_fixing(0.25, 1000)
        await self.bot.movepi(1.5, 1000)
        await self.bot.movepi(1.3, 1200)
        await self.bot.movepi(1.5, 500)
        await self.bot.movepi(1.4, 1000)
        await self.bot.movepi(1.5, 500)
        await self.bot.movepi(1.6, 1500)
        await self.bot.movepi(1.47, 3600)
        await self.bot.attack() # +2 TP
        await self.bot.movepi(1.6, 700)
        await self.bot.movepi(1.4, 1000)
        await self.bot.attack() # items
    async def path_4(self): # roamer
        logger_set_path(4)
        await self.bot.use_teleporter(x=908/2400, y=706/1080, corner='topright', move_x=0, move_y=3) # Stagnant Shadow
        await self.bot.movepi(1.2, 1800)
        await self.bot.movepi(1.0, 6000)
        await self.bot.movepi(1.1, 1500)
        await self.bot.attack() # items
        await self.bot.movepi(0.2, 800)
        await self.bot.movepi(1.0, 1500)
        await self.bot.attack_technique(2, wait=False)
        for _ in range(3):
            await self.bot.movepi(0.65, 500)
            await self.bot.attack_technique(2, wait=False)
        await self.bot.attack_technique(1)
    async def path_4(self): # roamer
        logger_set_path(4)
        await self.bot.use_teleporter(x=908/2400, y=706/1080, corner='topright', move_x=0, move_y=3) # Stagnant Shadow
        await self.bot.movepi(1, 1000)
        await self.bot.movepi(0.72, 2000)
        await self.bot.attack() # +2 TP
        await self.bot.movepi(0.21, 2400)
        await self.bot.attack() # items
        await self.bot.movepi(1.1, 700)
        await self.bot.movepi(1.0, 5000)
        await self.bot.movepi(0.5, 4500)
        await self.bot.attack_technique(2, wait=False)
        for _ in range(4):
            await self.bot.movepi(0.25, 500)
            await self.bot.attack_technique(2, wait=False)
        await self.bot.attack_technique(2)
    async def path_5(self): # roamer
        logger_set_path(5)
        await self.bot.use_teleporter(x=908/2400, y=706/1080, corner='topright', move_x=0, move_y=3) # Stagnant Shadow
        await self.bot.movepi(1, 1000)
        await self.bot.movepi(0.75, 1550)
        await self.bot.movepi(0.5, 1500)
        await self.bot.movepi(1, 3800)
        await self.bot.movepi(0.5, 5500)
        await self.bot.movepi(0.25, 6500)
        await self.bot.movepi(1.75, 500)
        for _ in range(2):
            await self.bot.movepi(1.75, 500)
            await self.bot.attack_technique(2, wait=False)
        await self.bot.movepi(1.0, 500)
        await self.bot.attack_technique(2, wait=False)
        for _ in range(2):
            await self.bot.movepi(1.6, 500)
            await self.bot.attack_technique(2, wait=False)
        for _ in range(3):
            await self.bot.movepi(1.1, 500)
            await self.bot.attack_technique(2, wait=False)
        await self.bot.attack_technique(1)
    async def path_6(self): # roamer
        logger_set_path(6)
        await self.bot.use_teleporter(x=1212/2400, y=444/1080, corner='topright', move_x=0, move_y=3) # Fortified Zone
        await self.bot.movepi(0.15, 700)
        await self.bot.attack() # items
        await self.bot.movepi(0.6, 500)
        await self.bot.movepi(0.5, 500)
        await self.bot.movepi(0.2, 1200)
        await self.bot.movepi(0.5, 3000)
        await self.bot.movepi(0.39, 1700)
        await self.bot.attack() # items
        await self.bot.movepi(0.55, 3000)
        await self.bot.attack_technique(4, wait=False)
        await self.bot.movepi(1.3, 500)
        await self.bot.attack_technique(3, wait=False)
        await self.bot.movepi(0.1, 500)
        await self.bot.attack_technique(1, wait=False)
        await self.bot.attack_technique(2)
    async def path_7(self): # roamer
        logger_set_path(7)
        # await self.bot.use_teleporter(x=1072/2400, y=209/1080, corner='topright', move_x=0, move_y=3) # Cavern of Corrosion
        await self.bot.movepi(1.45, 1900)
        await self.bot.attack() # items
        await self.bot.movepi(0.35, 1700)
        await self.bot.movepi(1.77, 6000)
        await self.bot.movepi(1.39, 800)
        await self.bot.attack() # +2 TP


class Everwinter_Hill:
    def __init__(self, bot):
        self.bot = bot
    async def teleport(self):
        logger.info('Teleport')
        logger.info('---')
        logger.info("--- Map: Everwinter Hill")
        logger.info('---')
        await self.bot.switch_map(y_list=984/1080, world='jarilo_vi', scroll_down=False,
                                    x=1297/2400, y=394/1080, corner='botleft', move_x=0, move_y=3) # Deck of Creation
        await self.bot.movepi(0.2, 6000)
        await self.bot.movepi(0.1, 3100)
        await self.bot.attack() # +2 TP
        await self.bot.movepi(1.5, 5000)
        await self.bot.movepi(1.9, 1100)
        await self.bot.attack_technique(2, wait=False)
        await self.bot.movepi(1.9, 1000)
        await self.bot.movepi(0.0, 1500)
        await self.bot.attack_technique(4)
    async def path_1(self):
        logger_set_path(1)
        await self.bot.use_teleporter(x=775/2400, y=653/1080, corner='botleft', move_x=0, move_y=3, confirm=True) # Ancient Battlefield: Snow Plains
        await self.bot.movepi(0.48, 3300)
        await self.bot.movepi(1.0, 200)
        await self.bot.attack() # +2 TP
        await self.bot.movepi(0.5, 3000)
        await self.bot.movepi(0.9, 4000)
        await self.bot.movepi(1.1, 3800)
        await self.bot.attack_technique(2, wait=False)
        await self.bot.movepi(0.95, 3000)
        await self.bot.movepi(0.6, 700)
        await self.bot.movepi(0.95, 1200)
        await self.bot.attack_technique(5)


class Great_Mine:
    def __init__(self, bot):
        self.bot = bot
    async def teleport(self):
        logger.info('Teleport')
        logger.info('---')
        logger.info("--- Map: Great Mine")
        logger.info('---')
        await self.bot.switch_map(y_list=687/1080, world='jarilo_vi', scroll_down=True,
                                    x=665/2400, y=435/1080, corner='topleft', move_x=0, move_y=0, confirm=True) # Entrance
        await self.bot.movepi(0.2, 1500)
        await self.bot.attack() # +2 TP
    async def path_1(self): # roamer
        logger_set_path(1)
        await self.bot.use_teleporter(x=1220/2400, y=328/1080, corner='topright', move_x=0, move_y=3) # Vagrant Shelter
        await self.bot.movepi(0.9, 2000)
        await self.bot.movepi(1.2, 900)
        await self.bot.attack() # items
        await self.bot.movepi(1.1, 500)
        await self.bot.movepi(0.9, 1000)
        await self.bot.movepi(1.0, 1000)
        await self.bot.movepi(1.2, 1700)
        await self.bot.movepi(1.07, 4000)
        await self.bot.attack() # items
        await self.bot.movepi(0.5, 900)
        await self.bot.movepi(1.0, 2700)
        await self.bot.movepi(1.45, 2500)
        await self.bot.movepi(1.8, 1000)
        await self.bot.attack_technique(8)
    async def path_2(self):
        logger_set_path(2)
        await self.bot.use_teleporter(x=956/2400, y=610/1080, corner='botright', move_x=0, move_y=0, confirm=True) # Overlook
        await self.bot.movepi(1.8, 2000)
        await self.bot.movepi(0.1, 4700)
        await self.bot.movepi(0.2, 1000)
        await self.bot.attack_technique(2, wait=False)
        await self.bot.attack_technique(1)
    async def path_3(self): # roamer
        logger_set_path(3)
        await self.bot.use_teleporter(x=1296/2400, y=600/1080, corner='botright', move_x=0, move_y=0) # Shape of Scorch
        await self.bot.movepi(1.23, 1700)
        await self.bot.attack() # items
        await self.bot.movepi(1.23, 2000)
        await self.bot.attack() # +2 TP
        await self.bot.movepi(1.15, 1200)
        await self.bot.movepi(0.75, 1800)
        await self.bot.movepi(0.33, 3800)
        await self.bot.attack() # items
        await self.bot.movepi(1.33, 4700)
        await self.bot.movepi(1.1, 1500)
        await self.bot.movepi(1.2, 700)
        await self.bot.movepi(1.0, 400)
        await self.bot.attack_technique(2, wait=False)
        await self.bot.movepi(1.1, 500)
        await self.bot.attack_technique(2, wait=False)
        await self.bot.movepi(1.3, 500)
        await self.bot.attack_technique(2, wait=False)
        await self.bot.movepi(1.0, 500)
        await self.bot.attack_technique(4)
    async def path_x(self): # roamer
        logger_set_path(4)
        await self.bot.use_teleporter(x=912/2400, y=755/1080, corner='botright', move_x=0, move_y=0) # Main Mine Shaft
        await self.bot.movepi(1.02, 2700)
        await self.bot.attack() # +2 TP
        await self.bot.movepi(1.1, 4000)
        await self.bot.movepi(0.9, 700)
        await self.bot.attack_technique(1, wait=False)
        await self.bot.movepi(1.5, 500)
        await self.bot.attack_technique(2, wait=False)
        await self.bot.position_fixing(1.25, 1000)
        await self.bot.movepi(0.49, 800)
        await self.bot.movepi(0.85, 2300)
        await self.bot.attack_technique(1, wait=False)
        await self.bot.movepi(0.95, 1000)
        await self.bot.movepi(0.4, 1500)
        await self.bot.movepi(0.25, 3000)
        await self.bot.position_fixing(0.25, 1000)
        await self.bot.movepi(1.75, 2000)
        await self.bot.movepi(1.9, 1000)
        await self.bot.movepi(0.0, 600)
        await self.bot.movepi(0.25, 600)
        await self.bot.movepi(0.3, 2100)
        await self.bot.attack() # items
        await self.bot.movepi(0.55, 1000)
        await self.bot.attack_technique(1)
        await self.bot.restore_tp(n=1) # +2 TP
    async def path_5(self): # roamer
        logger_set_path(5)
        await self.bot.use_teleporter(x=951/2400, y=480/1080, corner='botright', move_x=0, move_y=0) # Shape of Spike
        await self.bot.movepi(1.8, 1500)
        await self.bot.attack() # +2 TP
        await self.bot.movepi(0.8, 3000)
        await self.bot.movepi(0.9, 1000)
        await self.bot.movepi(1.05, 3000)
        await self.bot.movepi(1.2, 1000)
        await self.bot.attack_technique(3, wait=False)
        for _ in range(2):
            await self.bot.movepi(0.49, 500)
            await self.bot.attack_technique(2, wait=False)
        await self.bot.attack_technique(1)
        await self.bot.restore_tp(n=1) # +2 TP
    async def path_x(self):
        logger_set_path(6)
        await self.bot.use_teleporter(x=951/2400, y=480/1080, corner='botright', move_x=0, move_y=0) # Shape of Spike
        await self.bot.movepi(0.8, 1500)
        await self.bot.movepi(0.9, 1000)
        await self.bot.movepi(1.0, 3000)
        await self.bot.movepi(1.05, 1500)
        await self.bot.movepi(0.55, 3000)
        await self.bot.movepi(0.25, 1900)
        await self.bot.attack_technique(2)


class Rivet_Town:
    def __init__(self, bot):
        self.bot = bot
    async def teleport(self):
        logger.info('Teleport')
        logger.info('---')
        logger.info("--- Map: Rivet Town")
        logger.info('---')
        await self.bot.switch_map(y_list=808/1080, world='jarilo_vi', scroll_down=True,
                                    x=832/2400, y=597/1080, corner='topleft', move_x=0, move_y=0) # Abandoned Market
        await self.bot.movepi(0.9, 700)
        await self.bot.attack() # +2 TP
    async def path_x(self):
        logger_set_path(1)
        # await self.bot.use_teleporter(x=998/2400, y=393/1080, corner='topright', move_x=0, move_y=0) # Orphanage
        await self.bot.movepi(1.6, 1500)
        await self.bot.movepi(1.25, 1000)
        await self.bot.movepi(1.1, 1000)
        await self.bot.movepi(1.0, 2800)
        await self.bot.movepi(0.88, 1000)
        await self.bot.attack_technique(2)


# async def farm_rivet_town(self):
#     logger('farm: Rivet Town')
#     await self.bot.switch_map(807/1080, scroll_down=True)
#     logger('### group 1 ###')
#     await self.bot.use_teleporter(1001/2400, 281/1080, open_map=False) # Orphanage
#     await self.bot.attack()
#     await self.bot.wait_for_onmap()
#     logger('### group 2 ###')
#     await self.bot.use_teleporter(999/2400, 394/1080) # Orphanage
#     await self.bot.movepi(1.6, 1500)
#     await self.bot.movepi(1.25, 1000)
#     await self.bot.movepi(1.1, 1000)
#     await self.bot.movepi(1.0, 2800)
#     await self.bot.movepi(0.58, 5000)
#     await self.bot.movepi(0.50, 8000)
#     await self.bot.movepi(1.0, 1500)
#     await self.bot.movepi(0.5, 4000)
#     await self.bot.attack()
#     await self.bot.wait_for_onmap()
#     logger('### group 3 ###')
#     await self.bot.use_teleporter(1016/2400, 775/1080, confirm=True)
#     await self.bot.movepi(0.5, 2500)
#     await self.bot.movepi(0.0, 2400)
#     await self.bot.movepi(0.25, 500)
#     await self.bot.movepi(0.75, 700)
#     await self.bot.movepi(1.0, 7800)
#     await self.bot.movepi(0.5, 2400)
#     await self.bot.attack()
#     await self.bot.wait_for_onmap()
#     logger('### group 4 ###') # roamer
#     await self.bot.movepi(0.7, 4000)
#     await self.bot.attack()
#     await self.bot.wait_for_onmap()
    

class Robot_Settlement:
    def __init__(self, bot):
        self.bot = bot
    async def teleport(self):
        logger.info('Teleport')
        logger.info('---')
        logger.info("--- Map: Robot Settlement")
        logger.info('---')


# async def farm_robot_settlement(self):
#     logger('farm: Robot Settlement')
#     await self.bot.switch_map(927/1080, scroll_down=True)
#     logger('### group 1 ###')
#     await self.bot.use_teleporter(626/2400, 678/1080, open_map=False) # Bud of Harmony
#     await self.bot.movepi(1.75, 1700)
#     await self.bot.attack()
#     await self.bot.wait_for_onmap()
#     logger('### group 2 ###')
#     await self.bot.use_teleporter(766/2400, 533/1080) # Energy Conversion Station
#     await self.bot.movepi(1.75, 1900)
#     await self.bot.movepi(1.95, 3500)
#     await self.bot.movepi(1.75, 1200)
#     await self.bot.attack()
#     await self.bot.wait_for_onmap()
#     await self.bot.movepi(0.0, 800)
#     await self.bot.attack()
#     await self.bot.sleep(1)
#     logger('### group 3 ###')
#     await self.bot.use_teleporter(767/2400, 682/1080) # Energy Conversion Station
#     await self.bot.movepi(1.75, 1900)
#     await self.bot.movepi(1.95, 1400)
#     await self.bot.movepi(1.4, 4000)
#     await self.bot.movepi(1.5, 2000)
#     await self.bot.movepi(1.37, 5000)
#     await self.bot.movepi(1.5, 1300)
#     await self.bot.movepi(1.3, 1600)
#     await self.bot.movepi(1.5, 800)
#     await self.bot.movepi(1.25, 300)
#     await self.bot.attack()
#     await self.bot.sleep(0.5)
#     await self.bot.movepi(1.6, 2300)
#     await self.bot.movepi(1.4, 1000)
#     await self.bot.movepi(1.25, 2100)
#     await self.bot.attack()
#     await self.bot.sleep(1.0)
#     await self.bot.movepi(1.25, 700)
#     await self.bot.attack()
#     await self.bot.wait_for_onmap()
#     logger('### group 4 ###')
#     await self.bot.use_teleporter(768/2400, 576/1080) # Energy Conversion Station
#     await self.bot.movepi(1.75, 1900)
#     await self.bot.movepi(1.95, 1400)
#     await self.bot.movepi(1.4, 4000)
#     await self.bot.movepi(1.5, 2000)
#     await self.bot.movepi(1.37, 5000)
#     await self.bot.movepi(1.5, 1300)
#     await self.bot.movepi(1.3, 1600)
#     await self.bot.movepi(1.5, 800)
#     await self.bot.movepi(1.25, 300)
#     await self.bot.movepi(1.6, 2400)
#     await self.bot.movepi(1.88, 1400)
#     await self.bot.attack()
#     await self.bot.wait_for_onmap()
#     logger('### group 4, part 2 ###')
#     await self.bot.movepi(1.75, 1200)
#     await self.bot.movepi(0.4, 1800)
#     await self.bot.attack()
#     await self.bot.wait_for_onmap()


