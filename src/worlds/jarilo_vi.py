from logger import logger, logger_set_path
from automation.bot import Bot


class Init:
    def __init__(self, device):
        self.outlying_snow_plains = Outlying_Snow_Plains(device)
        self.backwater_pass = Backwater_Pass(device)
        self.silvermane_guard = Silvermane_Guard(device)
        self.corridor = Corridor(device)
        self.everwinter_hill = Everwinter_Hill(device)
        self.great_mine = Great_Mine(device)
        self.rivet_town = Rivet_Town(device)
        self.robot_settlement = Robot_Settlement(device)
    async def farm(self):
        '''
        Status  7/7
        TP      5 -> 5
        Items   R2: 0, R4: 0
        XP      19440/19440
        Time    1750
        '''
        await self.outlying_snow_plains.farm()              # TP:-1->4 XP:2052/2052 Time:188
        await self.backwater_pass.farm()                    # TP:+0->4 XP:3024/3024 Time:240
        await self.robot_settlement.farm()                  # TP:+1->5 XP:2592/2592 Time:237
        await self.corridor.farm()                          # TP:-2->3 XP:3672/3672 Time:432
        await self.everwinter_hill.farm()                   # TP:+0->3 XP:1404/1404 Time:119
        await self.robot_settlement.teleport(tp_restore=2)  # TP:+2->5 Time:???
        await self.great_mine.farm()                        # TP:-4->1 XP:4536/4536 Time:326
        await self.rivet_town.farm()                        # TP:+5->5 XP:2160/2160 Time:262
    async def dev(self):
        pass
        

class Outlying_Snow_Plains:
    def __init__(self, device):
        self.bot = Bot(device)
    async def farm(self):
        await self.teleport()
        await self.path_1()
        await self.path_2()
        await self.path_3()
    async def teleport(self):
        logger.info('Teleport')
        logger.info('---')
        logger.info("--- Map: Outlying Snow Plains")
        logger.info('---')
        await self.bot.switch_map(y_list=508/1080, world='jarilo_vi', scroll_down=False, # Long Slope
                                    x=998/2400, y=338/1080, corner='botright', move_x=0, move_y=0, confirm=True)
        await self.bot.move(0.2, 2200)
        await self.bot.attack() # items
        await self.bot.move(0.67, 8200)
        await self.bot.attack() # items
        await self.bot.move(0.9, 1500)
        await self.bot.move(0.6, 5000)
        await self.bot.move(0.55, 2500)
        await self.bot.move(0.78, 800)
        await self.bot.attack() # items
        await self.bot.move(0.9, 800)
        await self.bot.move(0.8, 300)
        await self.bot.attack_technique(3) # -2TP
    async def path_1(self):
        logger_set_path(1)
        await self.bot.use_teleporter(x=1079/2400, y=430/1080, corner='botright', move_x=0, move_y=0) # Bud of Memories
        await self.bot.move(1.3, 3000)
        await self.bot.attack_technique(2) # +2TP
        await self.bot.move(1.1, 1000)
        await self.bot.attack_technique(10) # -1TP
    async def path_2(self):
        logger_set_path(2)
        await self.bot.use_teleporter(x=998/2400, y=338/1080, corner='botright', move_x=0, move_y=0, confirm=True) # Long Slope
        await self.bot.move(1.19, 4600)
        await self.bot.attack() # items
        await self.bot.move(0.94, 4400)
        await self.bot.attack_technique(2) # -1TP
    async def path_3(self):
        logger_set_path(3)
        await self.bot.use_teleporter(x=998/2400, y=338/1080, corner='botright', move_x=0, move_y=0, confirm=True) # Long Slope
        await self.bot.move(0.62, 2900)
        await self.bot.attack() # +2TP
        await self.bot.move(0.55, 4000)
        await self.bot.move(0.8, 9000)
        await self.bot.move(0.9, 2000)
        await self.bot.attack_technique(4) # -3TP
        await self.bot.move(1.3, 3000)
        await self.bot.posfix(0.75, 1000)
        await self.bot.move(0.2, 1000)
        await self.bot.move(0.61, 4800)
        await self.bot.attack() # items
        await self.bot.move(0.425, 5250)
        await self.bot.attack() # +2TP


class Backwater_Pass:
    def __init__(self, device):
        self.bot = Bot(device)
    async def farm(self):
        await self.teleport()
        await self.path_1()
        await self.path_2()
        await self.path_3()
        await self.path_4()
    async def teleport(self):
        logger_set_path('Teleport')
        logger.info('Teleport')
        logger.info('---')
        logger.info("--- Map: Backwater Pass")
        logger.info('---')
        await self.bot.switch_map(y_list=629/1080, world='jarilo_vi', scroll_down=False,
                                    x=829/2400, y=273/1080, corner='botright', move_x=0, move_y=0) # Transport Hub
        await self.bot.move(1.5, 4900)
        await self.bot.move(1.0, 300)
        await self.bot.attack() # items
        await self.bot.move(1.5, 700)
        await self.bot.move(1.03, 2300)
        await self.bot.attack() # items
        await self.bot.move(0.97, 2500)
        await self.bot.move(1.0, 300)
        await self.bot.attack_technique(3) # -1TP
        await self.bot.posfix(1.3, 2000)
        await self.bot.move(0.05, 2600)
        await self.bot.move(1.5, 5500)
        await self.bot.move(1.3, 200)
        await self.bot.attack() # items
        await self.bot.move(1.0, 900)
        await self.bot.move(1.5, 2500)
        await self.bot.move(0.0, 2000)
        await self.bot.move(0.22, 2100)
        await self.bot.attack() # +2TP
    async def path_1(self):
        logger_set_path(1)
        await self.bot.use_teleporter(x=829/2400, y=273/1080, corner='botright', move_x=0, move_y=0) # Transport Hub
        await self.bot.move(1.5, 6000)
        await self.bot.move(1.75, 3200)
        await self.bot.move(0.3, 300)
        await self.bot.attack_technique(4) # -2TP
        await self.bot.move(0.1, 500)
        await self.bot.attack_technique(8) # -1TP
        await self.bot.move(0.6, 1200)
        await self.bot.attack_technique(2) # items
    async def path_2(self):
        logger_set_path(2)
        await self.bot.use_teleporter(x=945/2400, y=715/1080, corner='topright', move_x=0, move_y=1, confirm=True) # Leisure Plaza
        await self.bot.move(1.15, 600)
        await self.bot.attack() # +2TP
        await self.bot.move(0.5, 1000)
        await self.bot.move(1.0, 3700)
        await self.bot.move(0.5, 3500)
        await self.bot.move(0.35, 900)
        await self.bot.attack() # items
        await self.bot.move(1.0, 3100)
        await self.bot.attack() # items
        await self.bot.move(0.05, 2800)
        await self.bot.move(0.55, 2300)
        await self.bot.attack() # items
        await self.bot.posfix(0.7, 1500)
        await self.bot.move(1.7, 600)
        await self.bot.move(0.0, 5900)
        await self.bot.attack_technique(2) # -1TP
    async def path_3(self):
        logger_set_path(3)
        await self.bot.use_teleporter(x=830/2400, y=360/1080, corner='topright', move_x=0, move_y=1) # Bud of Aether
        await self.bot.move(0.68, 900)
        await self.bot.attack() # items
        await self.bot.move(1.5, 2700)
        await self.bot.move(0.0, 1300)
        await self.bot.attack() # +2TP
        await self.bot.move(1.78, 1600)
        await self.bot.attack() # items
        await self.bot.move(0.8, 700)
        await self.bot.move(0.85, 3200)
        await self.bot.move(1.0, 3100)
        await self.bot.move(1.29, 2400)
        await self.bot.attack_technique(3) # -2TP
        await self.bot.move(1.3, 700)
        await self.bot.attack_technique(1)
        for _ in range(4): # -1TP, roamer
            await self.bot.move(1.0, 300)
            await self.bot.attack_technique(3)
    async def path_4(self):
        logger_set_path(4)
        await self.bot.use_teleporter(x=829/2400, y=273/1080, corner='botright', move_x=0, move_y=0) # Transport Hub
        await self.bot.move(0.8, 700)
        await self.bot.attack() # +2TP


class Silvermane_Guard:
    def __init__(self, device):
        self.bot = Bot(device)
    async def restore_tp(self, tp):
        logger_set_path('Teleport: TP Restore')
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


class Corridor:
    def __init__(self, device):
        self.bot = Bot(device)
    async def farm(self):
        await self.teleport()
        await self.path_1()
        await self.path_2()
        await self.path_3()
        await self.path_4()
        await self.path_5()
        await self.path_6()
        await self.path_7()
        await self.path_8()
    async def teleport(self):
        logger_set_path('Teleport')
        logger.info('Teleport')
        logger.info('---')
        logger.info("--- Map: Corridor of Fading Echoes")
        logger.info('---')
        await self.bot.switch_map(y_list=869/1080, world='jarilo_vi', scroll_down=False,
                                        x=869/2400, y=351/1080, corner='botright', move_x=0, move_y=3) # Command Center
        await self.bot.move(0.3, 4700)
        await self.bot.attack() # items
        await self.bot.move(1.0, 700)
        await self.bot.move(0.6, 300)
        await self.bot.attack_technique(3) # -2TP
        await self.bot.move(0.6, 500)
        await self.bot.attack_technique(3) # -1TP
        await self.bot.move(1.6, 500)
        await self.bot.attack_technique(3)
        await self.bot.move(0.7, 500)
        await self.bot.attack_technique(3)
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(3)
    async def path_1(self): # roamer
        logger_set_path(1)
        await self.bot.use_teleporter(x=962/2400, y=502/1080, corner='botright', move_x=0, move_y=0) # Ancient Battlefield: Frontline
        await self.bot.move(0.7, 1000)
        await self.bot.attack() # +2TP
        await self.bot.move(1.6, 1500)
        await self.bot.move(1.5, 4100)
        await self.bot.move(1.0, 1000)
        await self.bot.attack_technique(10) # -1TP
    async def path_2(self): # roamer
        logger_set_path(2)
        await self.bot.use_teleporter(x=962/2400, y=502/1080, corner='botright', move_x=0, move_y=0) # Ancient Battlefield: Frontline
        await self.bot.move(1.5, 5000)
        await self.bot.move(1.6, 2400)
        await self.bot.attack() # items
        await self.bot.posfix(0.9, 2500)
        await self.bot.move(1.8, 4000)
        await self.bot.move(1.7, 2000)
        await self.bot.move(1.8, 700)
        await self.bot.move(1.4, 300)
        await self.bot.move(1.5, 1000)
        await self.bot.attack_technique(2) # +2TP
        await self.bot.move(1.3, 700)
        for _ in range(4): # -1TP
            await self.bot.move(1.5, 500)
            await self.bot.attack_technique(2)
        await self.bot.move(0.7, 700)
        for _ in range(2):
            await self.bot.move(0.95, 500)
            await self.bot.attack_technique(2)
    async def path_3(self):
        logger_set_path(3)
        await self.bot.use_teleporter(x=962/2400, y=502/1080, corner='botright', move_x=0, move_y=0) # Ancient Battlefield: Frontline
        await self.bot.move(1.5, 5000)
        await self.bot.move(1, 3500)
        await self.bot.move(1.51, 5900)
        await self.bot.attack_technique(4) # -3TP
        await self.bot.move(0.3, 4000)
        await self.bot.attack() # items
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.5, 1000)
        await self.bot.move(1.3, 1200)
        await self.bot.move(1.5, 500)
        await self.bot.move(1.4, 1000)
        await self.bot.move(1.5, 500)
        await self.bot.move(1.6, 1500)
        await self.bot.move(1.47, 3600)
        await self.bot.attack() # +2TP
        await self.bot.move(1.6, 700)
        await self.bot.move(1.4, 1000)
        await self.bot.attack() # items
    async def path_4(self): # roamer
        logger_set_path(4)
        await self.bot.use_teleporter(x=908/2400, y=706/1080, corner='topright', move_x=0, move_y=3) # Stagnant Shadow
        await self.bot.move(1.2, 1800)
        await self.bot.move(1.0, 6000)
        await self.bot.move(1.1, 1500)
        await self.bot.attack() # items
        await self.bot.move(0.2, 800)
        await self.bot.move(1.0, 1500)
        await self.bot.attack_technique(2) # -1TP
        for _ in range(3):
            await self.bot.move(0.7, 500)
            await self.bot.attack_technique(2)
        await self.bot.attack_technique(1)
    async def path_5(self): # roamer
        logger_set_path(5)
        await self.bot.use_teleporter(x=908/2400, y=706/1080, corner='topright', move_x=0, move_y=3) # Stagnant Shadow
        await self.bot.move(1, 1000)
        await self.bot.move(0.72, 2000)
        await self.bot.attack() # +2TP
        await self.bot.move(0.21, 2400)
        await self.bot.attack() # items
        await self.bot.move(1.1, 700)
        await self.bot.move(1.0, 5000)
        await self.bot.move(0.5, 4500)
        await self.bot.attack_technique(2) # -1TP
        for _ in range(4):
            await self.bot.move(0.25, 500)
            await self.bot.attack_technique(2)
        await self.bot.attack_technique(2)
    async def path_6(self): # roamer
        logger_set_path(6)
        await self.bot.use_teleporter(x=908/2400, y=706/1080, corner='topright', move_x=0, move_y=3) # Stagnant Shadow
        await self.bot.move(1, 1000)
        await self.bot.move(0.75, 1550)
        await self.bot.move(0.5, 1500)
        await self.bot.move(1, 3800)
        await self.bot.move(0.5, 5500)
        await self.bot.move(0.25, 6500)
        await self.bot.move(1.75, 500)
        for _ in range(2): # -1TP
            await self.bot.move(1.75, 500)
            await self.bot.attack_technique(2)
        await self.bot.move(1.0, 500)
        await self.bot.attack_technique(2)
        for _ in range(2):
            await self.bot.move(1.6, 500)
            await self.bot.attack_technique(2)
        for _ in range(3):
            await self.bot.move(1.1, 500)
            await self.bot.attack_technique(2)
        await self.bot.attack_technique(1)
    async def path_7(self): # roamer
        logger_set_path(7)
        await self.bot.use_teleporter(x=1072/2400, y=209/1080, corner='topright', move_x=0, move_y=3) # Cavern of Corrosion
        await self.bot.move(1.45, 1900)
        await self.bot.attack() # items
        await self.bot.move(0.35, 1700)
        await self.bot.move(1.77, 6000)
        await self.bot.move(1.39, 800)
        await self.bot.attack_technique(2) # +2TP
        await self.bot.move(0.3, 500)
        await self.bot.attack_technique(4) # -1TP
        await self.bot.move(1.7, 300)
        await self.bot.attack_technique(3)
        await self.bot.move(1.2, 500)
        await self.bot.attack_technique(4)
    async def path_8(self):
        logger_set_path(8)
        await self.bot.use_teleporter(x=1212/2400, y=444/1080, corner='topright', move_x=0, move_y=3) # Fortified Zone
        await self.bot.move(0.15, 700)
        await self.bot.attack() # items
        await self.bot.move(0.6, 500)
        await self.bot.move(0.5, 500)
        await self.bot.move(0.2, 1200)
        await self.bot.move(0.5, 3000)
        await self.bot.move(0.39, 1700)
        await self.bot.attack() # items


class Everwinter_Hill:
    def __init__(self, device):
        self.bot = Bot(device)
    async def farm(self):
        await self.teleport()
        await self.path_1()
        await self.path_2()
    async def teleport(self):
        logger_set_path('Teleport')
        logger.info('---')
        logger.info("--- Map: Everwinter Hill")
        logger.info('---')
        await self.bot.switch_map(y_list=984/1080, world='jarilo_vi', scroll_down=False,
                                    x=1297/2400, y=394/1080, corner='botleft', move_x=0, move_y=3) # Deck of Creation
        await self.bot.move(0.2, 6000)
        await self.bot.move(0.1, 3100)
        await self.bot.attack() # +2TP
        await self.bot.move(1.5, 5000)
        await self.bot.move(1.9, 1100)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.move(1.9, 1000)
        await self.bot.move(0.0, 1500)
        await self.bot.attack_technique(4) # -2TP
    async def path_1(self):
        logger_set_path(1)
        await self.bot.use_teleporter(x=775/2400, y=653/1080, corner='botleft', move_x=0, move_y=3, confirm=True) # Ancient Battlefield: Snow Plains
        await self.bot.move(0.48, 3300)
        await self.bot.move(1.0, 200)
        await self.bot.attack() # +2TP
        await self.bot.move(0.5, 3000)
        await self.bot.move(0.9, 4000)
        await self.bot.move(1.1, 3800)
        await self.bot.attack_technique(2) # -2TP
        await self.bot.move(0.95, 2600)
        await self.bot.attack_technique(1)
        await self.bot.move(0.6, 300)
        await self.bot.attack_technique(1)
        await self.bot.move(0.95, 300)
        await self.bot.attack_technique(8) # -1TP
    async def path_2(self):
        logger_set_path(2)
        await self.bot.use_teleporter(x=1297/2400, y=394/1080, corner='botleft', move_x=0, move_y=3) # Deck of Creation
        await self.bot.move(1.5, 4000)
        await self.bot.move(0.0, 2000)
        await self.bot.move(1.75, 2000)
        await self.bot.move(1.4, 700)
        await self.bot.attack() # +2TP


class Great_Mine:
    def __init__(self, device):
        self.bot = Bot(device)
    async def farm(self):
        await self.teleport()
        await self.path_1()
        await self.path_2() # TODO: path1+2 might be combined
        await self.path_3()
        await self.path_4()
        await self.path_5()
        await self.path_6()
        # TODO: get items along the bridge path
    async def teleport(self):
        logger_set_path('Teleport')
        logger.info('---')
        logger.info("--- Map: Great Mine")
        logger.info('---')
        await self.bot.switch_map(y_list=687/1080, world='jarilo_vi', scroll_down=True, # Vagrant Shelter
                                    x=1220/2400, y=328/1080, corner='topright', move_x=0, move_y=3)
        await self.bot.move(0.9, 2000)
        await self.bot.move(1.2, 900)
        await self.bot.attack() # items
        await self.bot.move(1.1, 500)
        await self.bot.move(0.9, 1000)
        await self.bot.move(1.0, 1000)
        await self.bot.move(1.2, 1700)
        await self.bot.move(1.07, 4000)
        await self.bot.attack() # items
        await self.bot.move(0.5, 900)
        await self.bot.move(1.0, 2700)
        await self.bot.move(1.45, 2500)
        await self.bot.move(1.8, 1000)
        await self.bot.attack_technique(6) # -1TP
        await self.bot.move(0.25, 4000) # stability move
    async def path_1(self):
        logger_set_path(1)
        await self.bot.use_teleporter(x=956/2400, y=610/1080, corner='botright', move_x=0, move_y=0, confirm=True) # Overlook
        await self.bot.move(1.8, 2000)
        await self.bot.move(0.1, 4600)
        await self.bot.move(0.2, 900)
        await self.bot.attack_technique(3) # -1TP
    async def path_2(self): # roamer
        logger_set_path(2)
        await self.bot.use_teleporter(x=912/2400, y=755/1080, corner='botright', move_x=0, move_y=0) # Main Mine Shaft
        await self.bot.move(1.02, 2700)
        await self.bot.attack() # +2TP
        await self.bot.move(1.1, 4000)
        await self.bot.move(0.9, 700)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.move(1.5, 500)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.posfix(1.25, 4000)
        await self.bot.move(0.49, 800)
        await self.bot.move(0.85, 2300)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.move(1.1, 700)
        await self.bot.attack_technique(2) # items
        await self.bot.move(1.8, 2000)
        await self.bot.posfix(1.75, 1500)
        await self.bot.move(0.5, 2000)
        await self.bot.move(0.1, 2000)
        await self.bot.move(1.85, 3000)
        await self.bot.move(1.9, 1000)
        await self.bot.move(0.0, 600)
        await self.bot.move(0.25, 600)
        await self.bot.move(0.3, 1900)
        await self.bot.attack_technique(1) # items
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(3) # -1TP
    async def path_3(self):
        logger_set_path(3)
        await self.bot.use_teleporter(x=665/2400, y=435/1080, corner='topleft', move_x=0, move_y=0, confirm=True) # Entrance
        await self.bot.move(0.2, 1500)
        await self.bot.attack() # +2TP
    async def path_4(self): # roamer
        logger_set_path(4)
        await self.bot.use_teleporter(x=1296/2400, y=600/1080, corner='botright', move_x=0, move_y=0) # Shape of Scorch
        await self.bot.move(1.23, 1700)
        await self.bot.attack() # items
        await self.bot.move(1.23, 2000)
        await self.bot.attack() # +2TP
        await self.bot.move(1.15, 1200)
        await self.bot.move(0.75, 1800)
        await self.bot.move(0.33, 3800)
        await self.bot.attack() # items
        await self.bot.move(1.33, 4700)
        await self.bot.move(1.1, 1500)
        await self.bot.move(1.2, 700)
        await self.bot.move(1.0, 400)
        await self.bot.attack_technique(2) # -2TP
        await self.bot.move(1.1, 500)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.move(1.3, 500)
        await self.bot.attack_technique(2)
        await self.bot.move(1.0, 500)
        await self.bot.attack_technique(5)
    async def path_5(self): # roamer
        logger_set_path(5)
        await self.bot.use_teleporter(x=951/2400, y=480/1080, corner='botright', move_x=0, move_y=0) # Shape of Spike
        await self.bot.move(1.8, 1500)
        await self.bot.attack() # +2TP
        await self.bot.move(0.8, 3000)
        await self.bot.move(0.9, 1000)
        await self.bot.move(1.05, 3000)
        await self.bot.move(1.2, 1000)
        await self.bot.attack_technique(3) # -2TP
        for _ in range(2): # -1TP
            await self.bot.move(0.49, 500)
            await self.bot.attack_technique(2)
    async def path_6(self):
        logger_set_path(6)
        await self.bot.use_teleporter(x=951/2400, y=480/1080, corner='botright', move_x=0, move_y=0) # Shape of Spike
        await self.bot.move(0.8, 1500)
        await self.bot.move(0.9, 1000)
        await self.bot.move(1.0, 5500)
        await self.bot.move(1.05, 1000)
        await self.bot.move(0.9, 1000)
        await self.bot.move(0.5, 200)
        await self.bot.attack() # +2TP
        await self.bot.move(0.5, 1000)
        await self.bot.move(0.0, 1500)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.5, 1000)
        await self.bot.move(0.0, 1800)
        await self.bot.move(0.55, 2200)
        await self.bot.move(0.2, 1900)
        await self.bot.attack_technique(2) # -2TP


class Rivet_Town:
    def __init__(self, device):
        self.bot = Bot(device)
    async def farm(self):
        await self.teleport()
        await self.path_1()
        await self.path_2()
        await self.path_3()
        await self.path_4()
        await self.path_5()
    async def teleport(self):
        logger_set_path('Teleport')
        logger.info('---')
        logger.info("--- Map: Rivet Town")
        logger.info('---')
        await self.bot.switch_map(y_list=808/1080, world='jarilo_vi', scroll_down=True,
                                    x=832/2400, y=597/1080, corner='topleft', move_x=0, move_y=0) # Abandoned Market
        await self.bot.move(0.9, 700)
        await self.bot.attack() # +2TP
    async def path_1(self):
        logger_set_path(1)
        await self.bot.use_teleporter(x=998/2400, y=393/1080, corner='topright', move_x=0, move_y=0, confirm=True) # Orphanage
        await self.bot.move(1.6, 1500)
        await self.bot.move(1.25, 1000)
        await self.bot.move(1.1, 1000)
        await self.bot.move(1.0, 2800)
        await self.bot.move(0.88, 1000)
        await self.bot.attack_technique(2) # -2TP
        await self.bot.move(0.9, 2000)
        await self.bot.move(1.25, 2000)
        await self.bot.posfix(1.25, 1500)
        await self.bot.move(0.25, 2500)
        await self.bot.move(0.5, 2900)
        await self.bot.move(1.9, 600)
        await self.bot.move(1.6, 200)
        await self.bot.attack() # items
        await self.bot.move(0.5, 1000)
        await self.bot.move(0.25, 2300)
        await self.bot.move(0.5, 100)
        await self.bot.attack() # +2TP
        await self.bot.move(1.75, 3000)
        await self.bot.posfix(1.75, 1500)
        await self.bot.move(0.75, 1000)
        await self.bot.move(1.1, 3000)
        await self.bot.move(1.0, 400)
        await self.bot.move(0.5, 4400)
        await self.bot.move(0.98, 1900)
        await self.bot.attack() # items
        await self.bot.move(0.75, 1000)
        await self.bot.posfix(0.75, 1500)
        await self.bot.move(0.0, 2000)
        await self.bot.move(0.5, 1900)
        await self.bot.move(0.3, 2500)
        await self.bot.move(0.5, 500)
        await self.bot.attack() # items
        await self.bot.posfix(0.5, 1500)
        await self.bot.move(1.5, 700)
        await self.bot.move(1.3, 2500)
        await self.bot.move(0.9, 1300)
        await self.bot.move(0.5, 300)
        for _ in range(6): # -2TP
            await self.bot.move(0.5, 300)
            await self.bot.attack_technique(2)
        await self.bot.move(0.1, 2500)
        await self.bot.move(0.0, 2900)
        await self.bot.attack() # +2TP
    async def path_2(self):
        logger_set_path(2)
        await self.bot.use_teleporter(x=1017/2400, y=744/1080, corner='botright', move_x=0, move_y=0, confirm=True) # Entrance
        await self.bot.move(0.69, 1800)
        await self.bot.attack() # items
        await self.bot.move(0.4, 200)
        await self.bot.move(0.5, 1100)
        await self.bot.attack() # +2TP
    async def path_3(self):
        logger_set_path(3)
        await self.bot.use_teleporter(x=1017/2400, y=744/1080, corner='botright', move_x=0, move_y=0, confirm=True) # Entrance
        await self.bot.move(0.5, 2500)
        await self.bot.move(0.0, 2400)
        await self.bot.move(0.25, 500)
        await self.bot.move(0.75, 700)
        await self.bot.move(1.0, 7800)
        await self.bot.move(0.5, 1700)
        await self.bot.move(0.65, 300)
        await self.bot.attack_technique(4) # -2TP
        await self.bot.move(0.5, 1200)
        for _ in range(5): # -1TP
            await self.bot.move(0.75, 300)
            await self.bot.attack_technique(2)
    async def path_4(self):
        logger_set_path(4)
        await self.bot.use_teleporter(x=975/2400, y=599/1080, corner='topleft', move_x=0, move_y=0) # Shape of Gust
        await self.bot.move(1.65, 4000)
        await self.bot.attack() # +2TP
    async def path_5(self):
        logger_set_path(5)
        await self.bot.use_teleporter(x=975/2400, y=599/1080, corner='topleft', move_x=0, move_y=0) # Shape of Gust
        await self.bot.move(1.0, 2500)
        await self.bot.move(0.8, 500)
        await self.bot.attack() # items
        await self.bot.move(1.5, 1000)
        await self.bot.move(1.2, 1300)
        await self.bot.move(1.5, 1000)
        await self.bot.move(1.4, 2000)
        await self.bot.attack_technique(2) # +2TP


class Robot_Settlement:
    def __init__(self, device):
        self.bot = Bot(device)
    async def farm(self):
        await self.teleport()
        await self.path_1()
        await self.path_2()
        await self.path_3()
        await self.path_4()
    async def teleport(self):
        logger_set_path('Teleport')
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
        logger_set_path(1)
        await self.bot.use_teleporter(x=625/2400, y=757/1080, corner='botright', move_x=0, move_y=3) # Bud of Harmony
        await self.bot.move(1.7, 1700)
        await self.bot.attack_technique(3) # -2TP
    async def path_2(self):
        logger_set_path(2)
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
        logger_set_path(3)
        await self.bot.use_teleporter(x=765/2400, y=371/1080, corner='botright', move_x=0, move_y=0) # Energy Conversation Station
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
        logger_set_path(4)
        await self.bot.use_teleporter(x=942/2400, y=346/1080, corner='botright', move_x=0, move_y=0) # Svarog's Base
        await self.bot.move(1.6, 2300)
        await self.bot.attack() # +2TP
    async def restore_tp(self, tp):
        logger_set_path('Teleport: TP Restore')
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



